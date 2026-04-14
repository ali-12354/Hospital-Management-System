# Hospital Management System - Setup Guide

## Prerequisites

Before running the setup, make sure you have:

1. **Python 3.8+** installed
2. **XAMPP** installed and running
   - MySQL service must be running
3. **Database created** in phpMyAdmin:
   - Database name: `hospital_system` (or update in `.env` file)

## Initial Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure Database Connection

Edit the `.env` file with your database credentials:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=hospital_system
DB_PORT=3306
```

### Step 3: Run Setup Script

```bash
python setup.py
```

The setup script will:
- ✅ Check database connection
- ✅ Create all necessary tables (Users, Doctors, Patients, Appointments, Billing)
- ✅ Initialize the in-memory data store
- ✅ Create default admin user
- ✅ Optionally create sample test data (3 doctors, 2 patients)

## What the Setup Does

### Database Connection Verification
The setup checks if it can connect to your MySQL database and verifies the database name.

### Database Tables Created

1. **Users** - Stores login credentials for admin, doctors, and patients
2. **Doctors** - Doctor profiles with specialization, contact info
3. **Patients** - Patient profiles with medical history
4. **Appointments** - Scheduled appointments between patients and doctors
5. **Billing** - Bills and invoices for appointments

### Default Admin Account

After setup, you can login with:
- **Username:** `admin`
- **Password:** `admin`

⚠️ **Important:** Change the admin password after first login!

## Running the Application

After setup is complete, run:

```bash
python main.py
```

## Sample Test Data (Optional)

If you chose to create sample data during setup, you'll have:

**Sample Doctors:**
- Dr. John Smith (Cardiology) - Username: `dr.smith`, Password: `Doctor@123`
- Dr. Priya Patel (Neurology) - Username: `dr.patel`, Password: `Doctor@123`
- Dr. Maria Garcia (Pediatrics) - Username: `dr.garcia`, Password: `Doctor@123`

**Sample Patients:**
- David Johnson - Username: `patient1`, Password: `Patient@123`
- Sarah Williams - Username: `patient2`, Password: `Patient@123`

## Troubleshooting

### Database Connection Failed

If you see "❌ Database connection failed!", check:

1. XAMPP MySQL is running
2. Database `hospital_system` exists in phpMyAdmin
3. `.env` file has correct credentials
4. Port 3306 is not blocked by firewall

### Table Creation Failed

If tables fail to create:

1. Check MySQL user has CREATE TABLE permissions
2. Verify database exists and is accessible
3. Check for syntax errors in MySQL version compatibility

### Re-running Setup

The setup script is safe to run multiple times. It will:
- Skip existing tables (using `CREATE TABLE IF NOT EXISTS`)
- Skip existing users (will show warnings but continue)

## Database Connection Status

**✅ YES** - The database IS connected when you run `setup.py`

The setup script:
1. Tests the connection first
2. Creates tables using that connection
3. Verifies everything is working

After setup, the main application (`main.py`) will also connect to the same database.

## Manual Database Population

If you want to populate the database with more test data manually, you can run the SQL scripts:

```sql
-- In phpMyAdmin, select hospital_system database and run:
source xampp_test_inserts.sql
```

This will insert:
- 4 doctors
- 10 patients  
- 6 appointments
- 6 billing records

## Notes

- **Memory Store**: The application uses an in-memory data store for runtime data. Data in memory does not persist between application restarts unless saved to the database.
- **Database vs Memory**: Currently, the application primarily uses memory storage. Database tables are created for potential persistence features.
- **Reports**: Reports work with data from the in-memory store, showing appointments, doctor workloads, patient bills, etc.

## Support

For issues or questions, check the application logs:
- `app.log` - Contains detailed application logs

---

**Setup created and verified:** The database connection is working and all tables are created successfully! ✅
