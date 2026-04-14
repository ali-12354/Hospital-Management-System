=================================================================
    HOSPITAL MANAGEMENT SYSTEM - INSTALLATION GUIDE
=================================================================

Thank you for installing Hospital Management System!

SYSTEM REQUIREMENTS
-------------------
- Windows 7/8/10/11 (64-bit)
- 4 GB RAM (minimum)
- 500 MB free disk space
- Internet connection (for initial setup only)

INSTALLATION STEPS
------------------

Step 1: Install XAMPP
   1. Download XAMPP from: https://www.apachefriends.org/
   2. Install XAMPP (default settings are fine)
   3. Start XAMPP Control Panel
   4. Click "Start" for MySQL service
   5. Make sure MySQL is running (green indicator)

Step 2: Create Database
   1. Open web browser
   2. Go to: http://localhost/phpmyadmin
   3. Click "New" in left sidebar
   4. Database name: hospital_system
   5. Collation: utf8mb4_general_ci
   6. Click "Create"

Step 3: Configure Database Connection
   1. Open the folder where you extracted the application
   2. Find the ".env" file
   3. Open it with Notepad
   4. Edit these settings:
      
      DB_HOST=localhost
      DB_USER=root
      DB_PASSWORD=              (leave empty if no password)
      DB_NAME=hospital_system
      DB_PORT=3306
   
   5. Save and close the file

Step 4: Run the Application
   1. Double-click "HospitalManagementSystem.exe"
   2. The application will automatically create database tables
   3. Login with default credentials:
      Username: admin
      Password: admin
   
   4. IMPORTANT: Change admin password after first login!

DEFAULT LOGIN CREDENTIALS
--------------------------
Admin Account:
   Username: admin
   Password: admin

TROUBLESHOOTING
---------------

Problem: "Cannot connect to database"
Solution:
   - Make sure XAMPP MySQL is running
   - Check .env file has correct settings
   - Verify database 'hospital_system' exists in phpMyAdmin
   - Try restarting MySQL in XAMPP

Problem: "Application won't start"
Solution:
   - Make sure all files are in the same folder
   - Check if .env file exists
   - Try running as Administrator
   - Check Windows Firewall settings

Problem: "Missing DLL error"
Solution:
   - Install Microsoft Visual C++ Redistributable
   - Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe

Problem: Application shows black screen or freezes
Solution:
   - Update graphics drivers
   - Try running in compatibility mode (Windows 7/8)
   - Disable antivirus temporarily

FEATURES
--------
✓ User Management (Admin, Doctors, Patients)
✓ Appointment Scheduling
✓ Patient Records Management
✓ Doctor Management
✓ Billing System
✓ Reports and Analytics
✓ Secure Authentication

SAMPLE TEST DATA (Optional)
---------------------------
If you want to test the system with sample data:

1. Open phpMyAdmin (http://localhost/phpmyadmin)
2. Select 'hospital_system' database
3. Click "Import" tab
4. Choose "xampp_test_inserts.sql" file
5. Click "Go"

This will add:
- 4 sample doctors
- 10 sample patients
- 6 appointments
- 6 billing records

GETTING STARTED
---------------
After installation:

1. Login as admin (admin/admin)
2. Go to "Manage Doctors" to add doctors
3. Register patients or let them self-register
4. Start scheduling appointments
5. Generate reports from Admin panel

IMPORTANT NOTES
---------------
⚠ Change the default admin password immediately
⚠ Backup database regularly from phpMyAdmin
⚠ Keep XAMPP MySQL running when using the application
⚠ Do not delete the .env file
⚠ Each user needs their own XAMPP installation

DATA STORAGE
------------
All data is stored in MySQL database. To backup:
1. Open phpMyAdmin
2. Select 'hospital_system' database
3. Click "Export" tab
4. Choose "Quick" export method
5. Click "Go" to download backup

SUPPORT
-------
For issues or questions:
- Check BUILD_INSTRUCTIONS.md for technical details
- Check SETUP_GUIDE.md for setup information
- Review app.log file for error messages

SECURITY
--------
⚠ This application is for educational/internal use
⚠ Not recommended for production/public internet use
⚠ Use strong passwords for all accounts
⚠ Keep your database credentials secure

=================================================================
                    Installation Complete!
             You can now run HospitalManagementSystem.exe
=================================================================
