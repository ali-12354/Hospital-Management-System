"""
Reset and initialize the database with admin account
"""
import os
import sqlite3
import logging
from pathlib import Path
from src.utils.helpers import hash_password

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_database():
    """Initialize database and create admin account"""
    try:
        # Create data directory if it doesn't exist
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Database path
        db_path = data_dir / "hospital_management.db"
        
        # Delete existing database if it exists
        if db_path.exists():
            db_path.unlink()
            logger.info("Existing database deleted")
        
        # Create new database connection
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
        """)
        
        # Create admin account
        admin_password = hash_password("Admin@123")
        cursor.execute("""
        INSERT INTO users (username, password, role, is_active)
        VALUES (?, ?, ?, ?)
        """, ("admin", admin_password, "admin", True))
        
        # Create patients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            blood_group TEXT,
            contact TEXT NOT NULL,
            email TEXT,
            address TEXT,
            medical_history TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)
        
        conn.commit()
        logger.info("Database initialized and admin account created successfully")
        conn.close()
        
        # Update .env file
        with open(".env", "w") as f:
            f.write(f"DB_FILE={db_path}\n")
            f.write("APP_SECRET_KEY=your_secret_key_here\n")
            f.write("DEBUG=True\n")
        
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

if __name__ == "__main__":
    init_database()