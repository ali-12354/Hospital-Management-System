"""
Hospital Management System - Main Application
"""
import sys
import os
import customtkinter as ctk
from src.views.login_view import LoginView
from src.utils.config import load_config
from src.data.memory_store import MemoryStore

def main():
    # Set up logging with more details
    import logging
    import sys
    
    # Configure root logger to show all logs
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Also output to console for debugging
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
    logging.info("Starting application...")
    
    try:
        # Set appearance mode and default theme
        logging.info("Setting appearance mode...")
        ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
        logging.info("Setting color theme...")
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
        
        # Configure scaling - helps with high DPI displays and ensures consistent appearance
        ctk.set_widget_scaling(1.0)  # Adjust if UI elements appear too small/large
        ctk.set_window_scaling(1.0)  # Adjust if window size is not appropriate
        
        # Enable detailed error reporting for CTk
        ctk.deactivate_automatic_dpi_awareness()
        
        logging.info("Theme setup complete.")
    except Exception as e:
        logging.error(f"Error during startup: {str(e)}")
        raise
    
    # Load configuration
    load_config()
    
    # Initialize memory store (this creates the default admin user)
    memory_store = MemoryStore()
    
    # Create manual test data
    logging.info("Creating test data manually...")
    
    # Create test doctors
    from src.controllers.doctor_controller import DoctorController
    
    # Clear any existing doctors with these usernames
    existing_users = [user.username for user in memory_store.users.values()]
    logging.info(f"Existing users: {existing_users}")
    
    # Create multiple test doctors
    test_doctors = [
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
        },
        {
            "username": "dr.williams",
            "password": "Doctor@123",
            "first_name": "Robert",
            "last_name": "Williams",
            "specialization": "Orthopedics",
            "contact_number": "5554567890",
            "email": "dr.williams@hospital.com"
        }
    ]
    
    # Create each doctor if they don't exist
    for doctor_data in test_doctors:
        if doctor_data["username"] not in existing_users:
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
                logging.info(f"Created test doctor: Dr. {result.first_name} {result.last_name}")
            else:
                logging.warning(f"Failed to create test doctor {doctor_data['username']}: {result}")
    
    # Create multiple test patients
    from src.controllers.patient_controller import PatientController
    from datetime import datetime, timedelta
    
    test_patients = [
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
            "medical_history": "Asthma, seasonal allergies"
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
            "blood_group": "O-",
            "address": "456 Oak Ave",
            "medical_history": "No chronic conditions"
        },
        {
            "username": "patient3",
            "password": "Patient@123",
            "first_name": "Michael",
            "last_name": "Brown",
            "gender": "Male",
            "date_of_birth": datetime(1978, 11, 30),
            "contact_number": "5553334444",
            "email": "michael@example.com",
            "blood_group": "B+",
            "address": "789 Pine St",
            "medical_history": "Hypertension, type 2 diabetes"
        },
        {
            "username": "patient4",
            "password": "Patient@123",
            "first_name": "Emily",
            "last_name": "Chen",
            "gender": "Female",
            "date_of_birth": datetime(1995, 3, 12),
            "contact_number": "5554445555",
            "email": "emily@example.com",
            "blood_group": "AB+",
            "address": "101 Maple Dr",
            "medical_history": "Allergic to penicillin"
        }
    ]
    
    # Create each patient if they don't exist
    for patient_data in test_patients:
        if patient_data["username"] not in existing_users:
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
                logging.info(f"Created test patient: {result.first_name} {result.last_name}")
            else:
                logging.warning(f"Failed to create test patient {patient_data['username']}: {result}")
    
    # Verify we have doctors and patients
    doctors = DoctorController.get_all_doctors()
    patients = PatientController.get_all_patients()
    
    logging.info(f"Total doctors in system: {len(doctors)}")
    for d in doctors:
        logging.info(f"Doctor: {d.doctor_id} - {d.first_name} {d.last_name}")
        
    logging.info(f"Total patients in system: {len(patients)}")
    for p in patients:
        logging.info(f"Patient: {p.patient_id} - {p.first_name} {p.last_name}")
    
    # We won't create appointments automatically since they'll be created through the UI
    logging.info("Test data initialization completed")
    
    # Create application instance
    # Use the original LoginView (full UI) instead of the simplified LoginScreen
    app = LoginView()
    
    # Set window icon if exists
    icon_path = os.path.join("src", "assets", "icon.png")
    if os.path.exists(icon_path):
        app.iconbitmap(icon_path)
    
    # Start the application
    app.mainloop()

if __name__ == "__main__":
    main()