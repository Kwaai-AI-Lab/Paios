from uuid import uuid4
import backend.db as db

class AssetsManager:
    def __init__(self):
        db.init_db()

    async def create_asset(self, user_id, title, creator, subject, description):
        id = str(uuid4())
        query = 'INSERT INTO asset (id, user_id, title, creator, subject, description) VALUES (?, ?, ?, ?, ?, ?)'
        await db.execute_query(query, (id, user_id, title, creator, subject, description))
        return id

    async def update_asset(self, id, user_id, title, creator, subject, description):
        query = 'INSERT OR REPLACE INTO asset (id, user_id, title, creator, subject, description) VALUES (?, ?, ?, ?, ?, ?)'
        return await db.execute_query(query, (id, user_id, title, creator, subject, description))

    async def delete_asset(self, id):
        query = 'DELETE FROM asset WHERE id = ?'
        return await db.execute_query(query, (id,))

    async def retrieve_asset(self, id):
        query = 'SELECT user_id, title, creator, subject, description FROM asset WHERE id = ?'
        result = await db.execute_query(query, (id,))
        if result:
            return {'id': id, 'user_id': result[0][0], 'title': result[0][1], 'creator': result[0][2], 'subject': result[0][3], 'description': result[0][4]}
        return None

    async def retrieve_assets(self, offset=0, limit=100, sort_by=None, sort_order='asc', filters=None, query=None):
        base_query = 'SELECT id, user_id, title, creator, subject, description FROM asset'
        query_params = []

        # Apply filters
        filter_clauses = []
        if filters:
            for key, value in filters.items():
                if isinstance(value, list):
                    placeholders = ', '.join(['?'] * len(value))
                    filter_clauses.append(f"{key} IN ({placeholders})")
                    query_params.extend(value)
                else:
                    filter_clauses.append(f"{key} = ?")
                    query_params.append(value)

        # Apply free text search
        if query:
            query_clause = "(title LIKE ? OR description LIKE ? OR creator LIKE ? OR subject LIKE ?)"
            query_params.extend([f"%{query}%"] * 4)
            filter_clauses.append(query_clause)

        if filter_clauses:
            base_query += ' WHERE ' + ' AND '.join(filter_clauses)

        # Validate and apply sorting
        valid_sort_columns = ['id', 'user_id', 'title', 'creator', 'subject', 'description']
        if sort_by and sort_by in valid_sort_columns:
            sort_order = 'DESC' if sort_order.lower() == 'desc' else 'ASC'
            base_query += f' ORDER BY {sort_by} {sort_order}'

        # Apply pagination
        base_query += ' LIMIT ? OFFSET ?'
        query_params.extend([limit, offset])

        # Execute the main query
        results = await db.execute_query(base_query, tuple(query_params))
        
        assets = [{'id': result[0], 'user_id': result[1], 'title': result[2], 'creator': result[3], 'subject': result[4], 'description': result[5]} for result in results]

        # Get the total count of assets
        total_count_query = 'SELECT COUNT(*) FROM asset'
        total_count_params = query_params[:-2]  # Exclude limit and offset for the count query
        if filter_clauses:
            total_count_query += ' WHERE ' + ' AND '.join(filter_clauses)
        total_count_result = await db.execute_query(total_count_query, tuple(total_count_params))
        total_count = total_count_result[0][0] if total_count_result else 0

        return assets, total_count
