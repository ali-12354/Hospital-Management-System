# Hospital-Management-System
Hospital Management System (Python Desktop App) — Project Overview I built a complete Hospital Management System as a desktop application using Python + CustomTkinter (modern UI on top of Tkinter). 
Key Features
Secure Authentication (Role-Based)
Login screen with role selection (Patient / Administrator)
Password handling uses bcrypt hashing (not plain-text)
Input validations (strong password rules, email + phone validation)
Activity logging to app logs for auditing/debugging
Patient Registration + Profile
New patients can create an account directly from the login screen
Registration form includes: name, gender, DOB (calendar picker), blood group, contact, email, address, medical history
Patients can view and manage their profile info from their dashboard
Doctor Management (Admin)
Admin can add, update, and delete doctor profiles
Doctors include specialization, contact info, and other details used during appointment booking
Appointment Scheduling (Patient)
Patients can schedule appointments by selecting:
Doctor
Date (with a calendar picker)
Time slot (9 AM – 5 PM time slots)
Reason for visit
The system automatically prevents booking already-occupied time slots for the same doctor/date
Appointment status handling (Scheduled / Completed / Cancelled)
Billing Module
Billing records are linked to appointments/patients
Bills can be created and viewed inside the system (useful for tracking pending/paid billing flow in a hospital)
Feedback System (Patient)
Patients can submit feedback for an appointment
Star rating (1–5) + optional comments
Helps simulate service quality tracking for doctors/hospital staff
