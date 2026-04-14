# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src', 'src'),
        ('.env', '.'),
        ('requirements.txt', '.'),
        ('SETUP_GUIDE.md', '.'),
        ('xampp_test_inserts.sql', '.'),
        ('check_table_structure.sql', '.'),
    ],
    hiddenimports=[
        'customtkinter',
        'tkinter',
        'PIL',
        'PIL._tkinter_finder',
        'mysql.connector',
        'bcrypt',
        'tkcalendar',
        'babel.numbers',
        'src.models',
        'src.controllers',
        'src.views',
        'src.data',
        'src.utils',
        'src.reports',
        'src.views.dialogs',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyd_name = 'PIL._tkinter_finder.py'
pyd = next((item for item in a.pure if item[0] == pyd_name), None)
if pyd:
    a.pure.remove(pyd)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='HospitalManagementSystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to False to hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you have one: 'src/assets/icon.ico'
)
