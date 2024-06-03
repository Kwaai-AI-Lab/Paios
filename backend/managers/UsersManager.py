from uuid import uuid4
import backend.db as db

class UsersManager:
    def __init__(self):
        db.init_db()

    async def create_user(self, name, email):
        id = str(uuid4())
        query = 'INSERT INTO user (id, name, email) VALUES (?, ?, ?)'
        await db.execute_query(query, (id, name, email))
        return id

    async def retrieve_user(self, id):
        query = 'SELECT name, email FROM user WHERE id = ?'
        result = await db.execute_query(query, (id,))
        if result:
            return {'id': id, 'name': result[0][0], 'email': result[0][1]}
        return None

    async def update_user(self, id, name, email):
        query = 'INSERT OR REPLACE INTO user (id, name, email) VALUES (?, ?, ?)'
        return await db.execute_query(query, (id, name, email))

    async def delete_user(self, id):
        query = 'DELETE FROM user WHERE id = ?'
        return await db.execute_query(query, (id,))

    async def retrieve_all_users(self, offset=0, limit=100, sort_by=None, sort_order='asc', filters=None):
        base_query = 'SELECT id, name, email FROM user'
        query_params = []

        # Apply filters
        if filters:
            filter_clauses = []
            for key, value in filters.items():
                filter_clauses.append(f"{key} = ?")
                query_params.append(value)
            base_query += ' WHERE ' + ' AND '.join(filter_clauses)

        # Validate and apply sorting
        valid_sort_columns = ['id', 'name', 'email']
        if sort_by and sort_by in valid_sort_columns:
            sort_order = 'DESC' if sort_order.lower() == 'desc' else 'ASC'
            base_query += f' ORDER BY {sort_by} {sort_order}'

        # Apply pagination
        base_query += ' LIMIT ? OFFSET ?'
        query_params.extend([limit, offset])

        results = await db.execute_query(base_query, tuple(query_params))
        
        users = []
        for result in results:
            users.append({'id': result[0], 'name': result[1], 'email': result[2]})
        
        # Assuming you have a way to get the total count of users
        total_count_query = 'SELECT COUNT(*) FROM user'
        if filters:
            total_count_query += ' WHERE ' + ' AND '.join(filter_clauses)
        total_count_result = await db.execute_query(total_count_query, tuple(query_params[:len(filters)] if filters else ()))
        total_count = total_count_result[0][0] if total_count_result else 0

        return users, total_count
    