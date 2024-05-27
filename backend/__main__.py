#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from flask import Flask

def check_env():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Running in a virtual environment ({})".format(sys.prefix))
    else:
        print("Error: Running under the system python ({})\n".format(sys.prefix))
        venv_path = Path(__file__).resolve().parent.parent / '.venv'
        if not venv_path.exists():
            print("No virtual environment found at {} so you will need to create one.".format(venv_path))
            if os.name == "posix": # Linux/Mac
                print("\nYou can use the scripts/setup_environment.sh script to do this, or do it manually:")
                print("    python3 -m venv .venv")
                print("    source .venv/bin/activate")
                print("    pip install -r backend/requirements.txt")
            elif os.name == "nt": # Windows
                print("\nYou can use the scripts\\setup_environment.ps1 script to do this, or do it manually from the root directory:\n")
                print("    python -m venv .venv")
                print("    .venv\\Scripts\\activate")
                print("    pip install -r backend\\requirements.txt\n")
            sys.exit(1)
        else:
            print(f"Virtual environment found at {venv_path}. You can activate it with:\n")
            if os.name == "posix": # Linux/Mac
                print(f"    source {venv_path}/bin/activate")
            elif os.name == "nt": # Windows
                print(f"    {venv_path}\\Scripts\\activate.ps1")
            print(f"\nOnce you have activated the virtual environment, run this again.")
            sys.exit(1)

    required_modules = ['connexion', 'flask_cors']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Required module {module} is not installed.")
            sys.exit(1)

    return True

if __name__ == '__main__':
    try:
        from backend.blueprint import create_and_register_backend
    except ImportError:
        from blueprint import create_and_register_backend

    check_env()
    app = Flask(__name__)

    # Register the backend blueprint at /api
    create_and_register_backend(app, '/api')

    app.run(host='localhost', port=3080)
