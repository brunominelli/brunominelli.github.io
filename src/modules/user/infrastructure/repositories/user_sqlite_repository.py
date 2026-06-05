import os, sqlite3
from src.modules.user.domain.entities.user import User
from src.modules.user.domain.repositories.i_user_repository import IUserRepository

class UserSqliteRepository(IUserRepository):
    def __init__(self, db_path:str="db/app.db"):
        self.db_path = db_path
        self._ensure_db()

    def _connect(self):
        return sqlite3.connect(database=self.db_path)

    def _ensure_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE,
                password_hash TEXT,
                role TEXT
            )
        """)

        conn.commit()
        conn.close()

    def _to_entity(self, row):
        if not row:
            return None
        
        return User(
            id=row[0],
            name=row[1],
            email=row[2],
            password_hash=row[3],
            role=row[4]
        )

    def create(self, user:User) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO users (id, name, email, password_hash, role)
                VALUES (?, ?, ?, ?, ?)
            """, (
                user.id,
                user.name,
                user.email,
                user.password_hash,
                user.role
            ))

            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise Exception("Usuário j[a cadastrado]")
        
        conn.close()   
 
    def read_all(self) -> list[User]:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        conn.close()

        return [self._to_entity(row=row) for row in rows]
    
    def read_by_email(self, email:str) -> User:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()

        conn.close()

        return self._to_entity(row=row)
    
    def read_by_id(self, user_id:str) -> User:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()

        conn.close()

        return self._to_entity(row=row)
    
    def update(self, user:User) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE leads
            SET
                name = ?, 
                email = ?, 
                password_hash = ?, 
                role = ?
            WHERE id = ?
            """, (
                user.name, 
                user.email, 
                user.password_hash, 
                user.role, 
                user.id,
        ))

        conn.commit()
        conn.close()
    
    def delete(self, user_id:str) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id))

        conn.commit()
        conn.close()