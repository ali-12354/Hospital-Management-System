"""
Initialize the application database and create default admin account
"""
import os
import sqlite3
import logging
from pathlib import Path
from src.utils.helpers import hash_password

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def get_db_path():
    """Get the database file path"""
    db_dir = Path("data")
    db_dir.mkdir(exist_ok=True)
    return db_dir / "hospital.db"

def init_database():
    """Initialize the database and create admin account"""
    db_path = get_db_path()
    
    # Create tables
    with sqlite3.connect(db_path) as conn:
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
        
        # Check if admin exists
        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        admin_exists = cursor.fetchone()
        
        if not admin_exists:
            # Create admin account
            admin_password = hash_password("Admin@123")
            cursor.execute("""
            INSERT INTO users (username, password, role, is_active)
            VALUES (?, ?, ?, ?)
            """, ("admin", admin_password, "admin", True))
            
            logger.info("Admin account created successfully")
        else:
            logger.info("Admin account already exists")
        
        conn.commit()

if __name__ == "__main__":
    try:
        logger.info("Initializing database...")
        init_database()
        logger.info("Database initialization completed successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise