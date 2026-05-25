import os, sqlite3
from src.modules.lead.domain.entities.lead import Lead
from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository

class UserSQLiteRepository(ILeadRepository):
    def __init__(self, db_path="db/app.db"):
        self.db_path = db_path
        self._ensure_db()
    
    def _connect(self):
        return sqlite3.connect(database=self.db_path)
    
    def _ensure_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            subject TEXT,
            message TEXT,
            created_at TEXT,
            updated_at TEXT 
        )
        """)

        conn.commit()
        conn.close()
    
    def _to_entity(self, row):
        if not row:
            return None
        
        return Lead(
            id=row[0],
            name=row[1],
            email=row[2],
            phone=row[3],
            subject=row[4],
            message=row[5],
            created_at=row[6],
            updated_at=row[7]
        )
    
    def create(self, lead:Lead) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO leads (id, name, email, phone, subject, message, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                lead.id,
                lead.name,
                lead.email,
                lead.phone,
                lead.subject,
                lead.message,
                lead.created_at,
                lead.updated_at,
            ))

            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            raise Exception("Lead já cadastrado")
        
        conn.close()
    
    def read_all(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM leads")
        rows = cursor.fetchall()

        conn.close()

        return [self._to_entity(row=row) for row in rows]
    
    def read_by_id(self, lead_id:str) -> Lead | None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM leads WHERE id = ?", (lead_id,))
        row = cursor.fetchone()

        conn.close()

        return self._to_entity(row=row)
    
    def read_by_email(self, email:str) -> Lead | None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM leads WHERE email = ?", (email,))
        row = cursor.fetchone()

        conn.close()

        return self._to_entity(row=row)
    
    def update(self, lead:Lead) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE leads (name = ?, email = ?, phone = ?, subject = ?, message = ?, created_at = ?, updated_at = ?)
            WHERE id = ?
            """, (
                lead.id,
                lead.name,
                lead.email,
                lead.phone,
                lead.subject,
                lead.message,
                lead.created_at,
                lead.updated_at,
                lead.id,
        ))

        conn.commit()
        conn.close()
    
    def delete(self, lead_id:str) -> None:
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM users WHERE id = ?
        """, (lead_id))

        conn.commit()
        conn.close()
