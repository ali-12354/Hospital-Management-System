"""
Hospital Management System - Setup Script
This script will:
1. Check database connection
2. Create necessary database tables if they don't exist
3. Initialize default admin user
4. Create sample test data (optional)
"""

import sys
import os
from database import create_connection
from src.utils.config import load_config
from src.data.memory_store import MemoryStore
from src.controllers.doctor_controller import DoctorController
from src.controllers.patient_controller import PatientController
from datetime import datetime

def check_database_connection():
    """Check if database connection is working"""
    print("=" * 60)
    print("STEP 1: Checking Database Connection")
    print("=" * 60)
    
    try:
        conn = create_connection()
        if conn is None:
            print("❌ Database connection failed!")
            print("\nPlease check:")
            print("  1. XAMPP MySQL is running")
            print("  2. Database credentials in .env file are correct")
            print("  3. Database 'hospital_System' exists")
            return False
        
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"✅ Connected to database: {db_name}")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return False

def create_database_tables():
    """Create necessary database tables"""
    print("\n" + "=" * 60)
    print("STEP 2: Creating Database Tables")
    print("=" * 60)
    
    try:
        conn = create_connection()
        if conn is None:
            print("❌ Cannot create tables - no database connection")
            return False
        
        cursor = conn.cursor()
        
        # Create Users table
        print("Creating Users table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                role ENUM('admin', 'doctor', 'patient') NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("✅ Users table created/verified")
        
        # Create Doctors table
        print("Creating Doctors table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctors (
                doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                full_name VARCHAR(100) NOT NULL,
                specialization VARCHAR(100) NOT NULL,
                contact VARCHAR(20) NOT NULL,
                email VARCHAR(100),
                gender VARCHAR(20) DEFAULT 'Not specified',
                qualification VARCHAR(100) DEFAULT 'Medical Doctor',
                consulting_hours VARCHAR(50) DEFAULT '9:00 AM - 5:00 PM',
                fees DECIMAL(10, 2) DEFAULT 0.00,
                FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
            )
        """)
        print("✅ Doctors table created/verified")
        
        # Create Patients table
        print("Creating Patients table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                gender VARCHAR(20) NOT NULL,
                dob DATE NOT NULL,
                contact VARCHAR(20) NOT NULL,
                email VARCHAR(100),
                blood_group VARCHAR(10),
                address TEXT,
                medical_history TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
            )
        """)
        print("✅ Patients table created/verified")
        
        # Create Appointments table
        print("Creating Appointments table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointments (
                appointment_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT NOT NULL,
                doctor_id INT NOT NULL,
                appointment_date DATE NOT NULL,
                appointment_time TIME NOT NULL,
                reason TEXT,
                status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
                FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE
            )
        """)
        print("✅ Appointments table created/verified")
        
        # Create Billing table
        print("Creating Billing table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Billing (
                billing_id INT AUTO_INCREMENT PRIMARY KEY,
                appointment_id INT NOT NULL,
                patient_id INT NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                description TEXT,
                status ENUM('pending', 'paid', 'cancelled') DEFAULT 'pending',
                bill_date DATE NOT NULL,
                payment_date DATE,
                FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE
            )
        """)
        print("✅ Billing table created/verified")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n✅ All database tables created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

def initialize_memory_store():
    """Initialize in-memory data store with default admin user"""
    print("\n" + "=" * 60)
    print("STEP 3: Initializing Memory Store")
    print("=" * 60)
    
    try:
        store = MemoryStore()
        print("✅ Memory store initialized")
        print(f"   - Default admin user created (username: admin, password: admin)")
        return True
    except Exception as e:
        print(f"❌ Error initializing memory store: {e}")
        return False

def create_sample_data():
    """Create sample doctors and patients for testing"""
    print("\n" + "=" * 60)
    print("STEP 4: Creating Sample Test Data")
    print("=" * 60)
    
    response = input("\nDo you want to create sample test data? (y/n): ").strip().lower()
    if response != 'y':
        print("⏭️  Skipping sample data creation")
        return True
    
    try:
        store = MemoryStore()
        
        # Create sample doctors
        print("\nCreating sample doctors...")
        doctors_data = [
            {
                "username": "dr.smith",
                "password": "Doctor@123",
                "first_name": "John",
                "last_name": "Smith",
                "specialization": "Cardiology",
                "contact_number": "5551234567",
                "email": "dr.smith@hospital.com"
            },
            {
                "username": "dr.patel",
                "password": "Doctor@123",
                "first_name": "Priya",
                "last_name": "Patel",
                "specialization": "Neurology",
                "contact_number": "5552345678",
                "email": "dr.patel@hospital.com"
            },
            {
                "username": "dr.garcia",
                "password": "Doctor@123",
                "first_name": "Maria",
                "last_name": "Garcia",
                "specialization": "Pediatrics",
                "contact_number": "5553456789",
                "email": "dr.garcia@hospital.com"
            }
        ]
        
        doctors_created = 0
        for doctor_data in doctors_data:
            success, result = DoctorController.create_doctor(
                username=doctor_data["username"],
                password=doctor_data["password"],
                first_name=doctor_data["first_name"],
                last_name=doctor_data["last_name"],
                specialization=doctor_data["specialization"],
                contact_number=doctor_data["contact_number"],
                email=doctor_data["email"]
            )
            if success:
                doctors_created += 1
                print(f"   ✅ Created: Dr. {result.first_name} {result.last_name}")
            else:
                print(f"   ⚠️  {result}")
        
        print(f"\n✅ Created {doctors_created} sample doctors")
        
        # Create sample patients
        print("\nCreating sample patients...")
        patients_data = [
            {
                "username": "patient1",
                "password": "Patient@123",
                "first_name": "David",
                "last_name": "Johnson",
                "gender": "Male",
                "date_of_birth": datetime(1985, 5, 15),
                "contact_number": "5551112222",
                "email": "david@example.com",
                "blood_group": "A+",
                "address": "123 Main St",
                "medical_history": "No major health issues"
            },
            {
                "username": "patient2",
                "password": "Patient@123",
                "first_name": "Sarah",
                "last_name": "Williams",
                "gender": "Female",
                "date_of_birth": datetime(1990, 8, 22),
                "contact_number": "5552223333",
                "email": "sarah@example.com",
                "blood_group": "O+",
                "address": "456 Oak Ave",
                "medical_history": "Allergic to penicillin"
            }
        ]
        
        patients_created = 0
        for patient_data in patients_data:
            success, result = PatientController.register_patient(
                username=patient_data["username"],
                password=patient_data["password"],
                first_name=patient_data["first_name"],
                last_name=patient_data["last_name"],
                gender=patient_data["gender"],
                date_of_birth=patient_data["date_of_birth"],
                contact_number=patient_data["contact_number"],
                email=patient_data["email"],
                blood_group=patient_data["blood_group"],
                address=patient_data["address"],
                medical_history=patient_data["medical_history"]
            )
            if success:
                patients_created += 1
                print(f"   ✅ Created: {result.first_name} {result.last_name}")
            else:
                print(f"   ⚠️  {result}")
        
        print(f"\n✅ Created {patients_created} sample patients")
        
        # Summary
        print("\n" + "-" * 60)
        print("Sample Data Summary:")
        print(f"  - Total Doctors: {len(store.get_all_doctors())}")
        print(f"  - Total Patients: {len(store.get_all_patients())}")
        print("-" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        return False

def main():
    """Main setup function"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  Hospital Management System - Setup Wizard".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print("\n")
    
    # Load configuration
    load_config()
    
    # Step 1: Check database connection
    if not check_database_connection():
        print("\n❌ Setup failed: Cannot connect to database")
        print("\nPlease fix the database connection and run setup again.")
        sys.exit(1)
    
    # Step 2: Create database tables
    if not create_database_tables():
        print("\n❌ Setup failed: Cannot create database tables")
        sys.exit(1)
    
    # Step 3: Initialize memory store
    if not initialize_memory_store():
        print("\n❌ Setup failed: Cannot initialize memory store")
        sys.exit(1)
    
    # Step 4: Create sample data (optional)
    create_sample_data()
    
    # Final summary
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("\n✅ Database is connected and configured")
    print("✅ All tables are created")
    print("✅ Default admin user is ready")
    print("\nDefault Login Credentials:")
    print("  Username: admin")
    print("  Password: admin")
    print("\nYou can now run the application:")
    print("  python main.py")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
