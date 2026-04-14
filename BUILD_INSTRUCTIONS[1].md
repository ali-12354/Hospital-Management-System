# Hospital Management System - Build Instructions

## Creating Executable (.exe) File

### Prerequisites

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Build Steps

#### Method 1: Using the spec file (Recommended)

```bash
pyinstaller HospitalManagementSystem.spec
```

This will create:
- `dist/HospitalManagementSystem.exe` - The standalone executable

#### Method 2: Simple command line build

```bash
pyinstaller --name="HospitalManagementSystem" --onefile --windowed --add-data "src;src" --add-data ".env;." main.py
```

### Build Options Explained

- `--onefile` - Creates a single executable file
- `--windowed` - Hides the console window (GUI only)
- `--add-data` - Includes necessary folders and files
- `--icon` - Adds an icon (optional, if you have an .ico file)

### What Gets Included

The executable includes:
- ✅ All Python code (src folder)
- ✅ Configuration file (.env)
- ✅ SQL scripts
- ✅ Setup guide
- ✅ All dependencies (customtkinter, mysql-connector, etc.)

### Distribution Package

After building, create a distribution folder with:

```
HospitalManagementSystem/
├── HospitalManagementSystem.exe    (The main executable)
├── .env                            (Database configuration)
├── SETUP_GUIDE.md                  (Setup instructions)
├── xampp_test_inserts.sql          (Sample data SQL)
└── README_INSTALLATION.txt         (Installation guide for users)
```

### For Group Members

**What they need:**

1. **XAMPP installed** with MySQL running
2. **Database created** in phpMyAdmin:
   - Create database: `hospital_system`
3. **Extract the distribution package** to any folder
4. **Edit .env file** with their database credentials
5. **Run** `HospitalManagementSystem.exe`

### Important Notes

⚠️ **First Run:**
- The application will create necessary database tables automatically
- Default admin login: username=`admin`, password=`admin`

⚠️ **Database Connection:**
- Each user must have XAMPP installed and running
- Each user must configure their own `.env` file
- The database connection is NOT embedded (requires local MySQL)

⚠️ **File Size:**
- The .exe will be approximately 150-250 MB (includes all dependencies)
- This is normal for Python GUI applications with many libraries

### Troubleshooting Build Issues

**Issue: Module not found**
```bash
# Add the missing module to hiddenimports in the .spec file
```

**Issue: Files not included**
```bash
# Add to datas in the .spec file:
datas=[('file_or_folder', 'destination')],
```

**Issue: Build fails**
```bash
# Try cleaning and rebuilding:
rmdir /s /q build dist
pyinstaller HospitalManagementSystem.spec
```

### Testing the Executable

Before distributing:

1. Test on your machine:
   ```bash
   cd dist
   .\HospitalManagementSystem.exe
   ```

2. Test on a clean Windows machine (if possible)

3. Verify:
   - Database connection works
   - All features work (login, appointments, reports, etc.)
   - No console errors

### Creating an Installer (Optional)

For a professional installer, use **Inno Setup**:

1. Download Inno Setup: https://jrsoftware.org/isinfo.php
2. Create an installer script (.iss file)
3. This will create a proper Windows installer with:
   - Installation wizard
   - Desktop shortcut creation
   - Start menu integration
   - Uninstaller

I can help create the Inno Setup script if needed!

---

## Quick Start for Group Members

**Simple 3-Step Installation:**

1. Install XAMPP and start MySQL
2. Create database `hospital_system` in phpMyAdmin
3. Run `HospitalManagementSystem.exe`

That's it! The application handles the rest.
