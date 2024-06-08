import json
import re
import os
import signal
import asyncio
from backend.paths import abilities_dir
from backend.utils import remove_null_fields
from enum import Enum
from pathlib import Path
from backend.dependencies.PythonDependency import PythonDependency
from backend.dependencies.ResourceDependency import ResourceDependency
from backend.dependencies.LinuxDependency import LinuxDependency
from backend.dependencies.ContainerDependency import ContainerDependency

import logging
logger = logging.getLogger(__name__)

class AbilityState(Enum):
    AVAILABLE = "available"
    INSTALLING = "installing"
    INSTALLED = "installed"
    UPGRADING = "upgrading"
    UNINSTALLING = "uninstalling"

class AbilitiesManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AbilitiesManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
            cls._instance.__init__(*args, **kwargs)  # Explicitly call __init__
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self._load_abilities()
        self._initialize_dependency_managers()

    def _initialize_dependency_managers(self):
        self.dependency_managers = {
            'python': PythonDependency(),
            'resource': ResourceDependency(),
            'linux': LinuxDependency(),
            'container': ContainerDependency()
        }

    def _load_abilities(self):
        self.abilities = self._fetch_abilities_from_directory()

    def _fetch_abilities_from_directory(self):
        abilities = []
        for ability_path in abilities_dir.iterdir():
            if ability_path.is_dir():
                versions_info = self._get_versions_info(ability_path)
                version_to_load = versions_info.get('installed') or versions_info.get('latest')
                if version_to_load:
                    ability_data = self._fetch_ability_from_directory(ability_path, version_to_load)
                    if ability_data:
                        if 'versions' in ability_data:
                            ability_data['versions'].update(versions_info)
                        else:
                            ability_data['versions'] = versions_info
                        abilities.append(ability_data)
        return abilities

    def _fetch_ability_from_directory(self, ability_path, version):
        version_dir = ability_path / version
        metadata_file = version_dir / 'metadata.json'
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
                return metadata
        return None

    def _get_versions_info(self, ability_path):
        semver_pattern = re.compile(r'^\d+\.\d+\.\d+$')
        versions = []
        installed_version = None

        for version_dir in ability_path.iterdir():
            if version_dir.is_dir() and semver_pattern.match(version_dir.name):
                versions.append(version_dir.name)
            elif version_dir.is_file() and version_dir.name == 'installed':
                with open(version_dir, 'r') as f:
                    installed_version = f.read().strip()

        latest_version = max(versions, key=lambda v: list(map(int, v.split('.'))), default=None)

        versions_info = {
            'available': versions,
            'latest': latest_version,
        }
        if installed_version:
            versions_info['installed'] = installed_version

        return versions_info

    def get_ability(self, id, version=None, refresh=True):
        for ability in self.abilities:
            if ability.get('id') == id and (version is None or ability.get('version') == version):
                if refresh:
                    self._refresh_dependencies(ability)
                return remove_null_fields(ability)
        return None

    def _refresh_dependencies(self, ability):
        dependencies = ability.get('dependencies', [])
        for dependency in dependencies:
            dependency_manager = self.dependency_managers.get(dependency.get('type'))
            if dependency_manager:
                dependency_manager.refresh_status(ability, dependency)

    def retrieve_abilities(self, offset=0, limit=100, sort_by=None, sort_order='asc', filters=None, query=None):
        filtered_abilities = self._apply_filters(self.abilities, filters)
        if query:
            filtered_abilities = self._apply_query(filtered_abilities, query)
        sorted_abilities = self._apply_sorting(filtered_abilities, sort_by, sort_order)
        total_count = len(sorted_abilities)
        paginated_abilities = sorted_abilities[offset:offset + limit]

        # Apply remove_null_fields to each ability in the paginated list
        paginated_abilities = [remove_null_fields(ability) for ability in paginated_abilities]

        return paginated_abilities, total_count

    def _apply_filters(self, abilities, filters):
        if not filters:
            return abilities
        filtered_abilities = []
        for ability in abilities:
            if all(ability.get(key) == value for key, value in filters.items()):
                filtered_abilities.append(ability)
        return filtered_abilities

    def _apply_query(self, abilities, query):
        query = query.lower()
        filtered_abilities = []
        for ability in abilities:
            if query in ability.get('id', '').lower() or query in ability.get('description', '').lower():
                filtered_abilities.append(ability)
        return filtered_abilities

    def _apply_sorting(self, abilities, sort_by, sort_order):
        if not sort_by:
            return abilities
        sorted_abilities = sorted(
            abilities,
            key=lambda x: x.get(sort_by),
            reverse=(sort_order == 'desc')
        )
        return sorted_abilities

    def refresh_abilities(self):
        self._load_abilities()

    def install_ability(self, id, version=None):
        print(f"Installing ability {id} version {version}")
        for ability in self.abilities:
            if ability['id'] == id:
                # Installation logic here
                pass

    def uninstall_ability(self, id):
        print(f"Uninstalling ability {id}")
        for ability in self.abilities:
            if ability['id'] == id:
                # Uninstallation logic here
                pass

    def start_ability(self, ability_id):
        import stat
        import os
        import sys
        import subprocess
        import shlex
        from backend.paths import abilities_dir, abilities_data_dir, venv_bin_dir

        print(f"Starting ability {ability_id}")
        ability = self.get_ability(ability_id)
        if ability is None:
            return {"error": "Ability not found"}, 404

        start_script = ability.get('scripts', {}).get('start', '')
        if start_script is None:
            return {"error": "Ability start script not set"}, 404

        start_script_parts = shlex.split(start_script)

        if start_script_parts is None:
            return {"error": "Unable to determine start script executable"}, 500

        search_paths = [abilities_dir / ability_id, abilities_data_dir / ability_id, venv_bin_dir]
        script_found = False
        for path in search_paths:
            start_script_candidate = os.path.join(path, start_script_parts[0])
            if os.path.exists(start_script_candidate):
                start_script_cwd = path
                start_script_parts[0] = start_script_candidate
                script_found = True
                break
        if not script_found:
            return {"error": f"Start script {start_script_parts[0]} not found in {search_paths}"}, 404

        if os.name == "posix":
            if not os.access(start_script_parts[0], os.X_OK):
                current_permissions = stat.S_IMODE(os.lstat(start_script_parts[0]).st_mode)
                try:
                    os.chmod(start_script_parts[0], current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except Exception as e:
                    print(f"Warning: Failed to set execute bit on start script: {e}")

        if start_script_parts[0].endswith('.py'):
            python_executable = str(Path(sys.executable))
            start_script_parts.insert(0, python_executable)

        stdout_file_path = Path(start_script_cwd) / f"{ability_id}_stdout.log"
        stderr_file_path = Path(start_script_cwd) / f"{ability_id}_stderr.log"

        stdout_file = open(stdout_file_path, 'w')
        stderr_file = open(stderr_file_path, 'w')

        process = subprocess.Popen(start_script_parts, cwd=start_script_cwd, shell=False, stdout=stdout_file, stderr=stderr_file, text=True)
        ability['pid'] = process.pid
        return self.ok()

    def stop_ability(self, ability_id):
        ability = self.get_ability(ability_id)
        if not ability:
            return {"error": "Ability not found"}, 404
        if 'pid' in ability:
            try:
                os.kill(ability['pid'], signal.SIGTERM)
            except ProcessLookupError:
                return {"error": "Ability not running"}, 404
            del ability['pid']
            return self.ok()
        else:
            return {"error": "Ability not running"}, 404

    async def install_dependency(self, ability_id: str, dependency_id: str):
        ability = self.get_ability(ability_id)
        if not ability:
            raise ValueError("Ability not found")

        dependency = next((dep for dep in ability.get('dependencies', []) if dep.get('id') == dependency_id), None)
        if not dependency:
            raise ValueError("Dependency not found")

        dependency_manager = self.dependency_managers.get(dependency.get('type'))
        if not dependency_manager:
            raise ValueError("Unsupported dependency type")

        async def callback(result):
            if isinstance(result, dict) and 'message' in result:
                logger.info(result['message'])
            else:
                logger.error(f"Unexpected result: {result}")
            # Reload the ability or update versions here if needed
            self.refresh_abilities()

        await dependency_manager.install_in_background(ability, dependency, callback)
        return {"message": f"Installation of dependency {dependency_id} started"}
