import { useRecordContext } from "react-admin";
import { Edit, Create, List, Datagrid, TextField, TextInput, ReferenceField, ReferenceInput, SimpleForm, EditButton } from "react-admin";

const AssetTitle = () => {
    const record = useRecordContext();
    return <span>Asset {record ? `- ${record.title}` : ""}</span>;
};

const assetFilters = [
    <TextInput source="q" label="Search" alwaysOn />,
    <ReferenceInput source="user_id" label="User" reference="users" />,
];

export const AssetList = () => (
    <List filters={assetFilters}>
        <Datagrid rowClick="edit">
            <TextField source="title" />
            <ReferenceField source="user_id" reference="users" link="show" />
            <EditButton />
        </Datagrid>
    </List>
);

export const AssetEdit = () => (
    <Edit title={<AssetTitle />}>
        <SimpleForm>
            <ReferenceInput source="user_id" reference="users" optionText="name" />
            <TextInput source="title" />
            <TextInput source="description" multiline rows={5} />
        </SimpleForm>
    </Edit>
);

export const AssetCreate = () => (
    <Create redirect="show">
        <SimpleForm>
            <ReferenceInput source="user_id" reference="users" optionText="name" />
            <TextInput source="title" />
            <TextInput source="description" multiline rows={5} />
        </SimpleForm>
    </Create>
);
