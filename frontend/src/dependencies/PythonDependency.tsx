// PythonDependency.tsx
import { Button, Datagrid, TextField } from 'react-admin';
import { useState, useEffect, useRef } from 'react';
import { CheckedField } from '../components/CheckedField';
import GetAppIcon from '@mui/icons-material/GetApp';
import { useRecordContext, useNotify, useRefresh } from 'react-admin';
import { apiBase, httpClient } from '../apiBackend';

export const PythonDependency = (props: { dependencies: any, ability_id: string }) => {
    return (
        <Datagrid data={props.dependencies} sort={{ field: 'name', order: 'ASC' }}>
            <TextField source="id" />
            <TextField source="name" />
            <TextField source="versions.installed" label="Installed" />
            <TextField source="versions.required" label="Required" />
            <CheckedField source="versions.satisfied" label="Satisfied" />
            <InstallButton ability_id={props.ability_id} />
        </Datagrid>
    );
};

const InstallButton = ({ ability_id }: { ability_id: string }) => {
    const record = useRecordContext();
    const notify = useNotify();
    const refresh = useRefresh();
    const [isInstalling, setIsInstalling] = useState(false);
    const intervalId = useRef<NodeJS.Timeout | null>(null);

    useEffect(() => {
        // Clear any existing interval
        if (intervalId.current) {
            clearInterval(intervalId.current);
            intervalId.current = null;
        }

        // Set a new interval if the package is currently installing
        if (isInstalling) {
            intervalId.current = setInterval(() => {
                refresh();
            }, 5000); // Refresh every 5 seconds
        }

        return () => {
            // Clear the interval when the component is unmounted or the installing state changes
            if (intervalId.current) {
                clearInterval(intervalId.current);
            }
        };
    }, [isInstalling, refresh]);

    const handleInstallClick = (event: React.MouseEvent) => {
        event.stopPropagation();
        setIsInstalling(true);

        httpClient(`${apiBase}/abilities/${ability_id}/dependencies/${record.id}/install`, { method: 'POST' })
            .then(() => {
                notify('Python dependency installation requested');
                refresh();
            })
            .catch((e: any) => {
                notify('Error: Python dependency not installed', { type: 'warning' });
            })
            .finally(() => {
                setIsInstalling(false);
            });
    };

    const buttonLabel = isInstalling ? "Installing" : (record.versions.installed ? (record.versions.satisfied ? "Install" : "Upgrade") : "Install");

    return (
        !record.versions.satisfied && (
            <Button label={buttonLabel} onClick={handleInstallClick} disabled={isInstalling}>
                <GetAppIcon />
            </Button>
        )
    );
};
