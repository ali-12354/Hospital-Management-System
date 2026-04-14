-- ============================================================
-- XAMPP MySQL Database Test Insert Queries
-- Hospital Management System
-- Run these queries in phpMyAdmin SQL tab to test connection
-- ============================================================

-- First, verify the database exists and check table structures
USE hospital_System;

-- STEP 1: Check your actual column names by running these first!
-- Uncomment and run ONE section at a time to see your table structure:

-- DESCRIBE Doctors;
-- DESCRIBE Patients;
-- DESCRIBE Appointments;
-- DESCRIBE Billing;

-- ============================================================
-- 1. INSERT TEST DOCTORS
-- ============================================================
-- If you get column errors, adjust the column names below to match your DESCRIBE output
-- Common variations: full_name, phone vs contact, schedule vs consulting_hours

INSERT INTO Doctors (full_name, specialization, contact, email, schedule) VALUES
('Dr. John Smith', 'Cardiology', '5551234567', 'dr.smith@hospital.com', 'Mon-Fri 9AM-5PM'),
('Dr. Priya Patel', 'Pediatrics', '5551234568', 'dr.patel@hospital.com', 'Mon-Wed 8AM-4PM'),
('Dr. Maria Garcia', 'Orthopedics', '5551234569', 'dr.garcia@hospital.com', 'Tue-Sat 10AM-6PM'),
('Dr. Robert Williams', 'Neurology', '5551234570', 'dr.williams@hospital.com', 'Mon-Fri 8AM-3PM');

-- ============================================================
-- 2. INSERT TEST PATIENTS
-- ============================================================
-- Common column variations to check:
-- - contact vs phone vs phone_number vs contact_number
-- - dob vs date_of_birth
-- - address vs patient_address

INSERT INTO Patients (first_name, last_name, gender, dob, contact, email, blood_group, address, medical_history) VALUES
('David', 'Johnson', 'Male', '1985-05-15', '5551112222', 'david@example.com', 'A+', '123 Main St', 'Asthma, seasonal allergies'),
('Sarah', 'Williams', 'Female', '1990-08-22', '5552223333', 'sarah@example.com', 'O-', '456 Oak Ave', 'No chronic conditions'),
('Michael', 'Brown', 'Male', '1978-12-10', '5553334444', 'michael@example.com', 'B+', '789 Pine Rd', 'Diabetes Type 2'),
('Emily', 'Chen', 'Female', '1995-03-18', '5554445555', 'emily@example.com', 'AB+', '321 Elm St', 'None'),
('John', 'Smith', 'Male', '1982-07-25', '555-0101', 'john.smith@email.com', 'A+', '100 First St', 'Hypertension'),
('Emma', 'Johnson', 'Female', '1988-11-30', '555-0102', 'emma.j@email.com', 'B+', '200 Second Ave', 'None'),
('Michael', 'Williams', 'Male', '1975-04-12', '555-0103', 'mike.w@email.com', 'O+', '300 Third Blvd', 'High cholesterol'),
('Sophia', 'Brown', 'Female', '1992-09-08', '555-0104', 'sophia.b@email.com', 'A+', '400 Fourth Ln', 'Asthma'),
('William', 'Davis', 'Male', '1980-01-20', '555-0105', 'william.d@email.com', 'AB+', '500 Fifth Dr', 'None'),
('Olivia', 'Miller', 'Female', '1987-06-15', '555-0106', 'olivia.m@email.com', 'O-', '600 Sixth Ct', 'Allergies');

-- ============================================================
-- 3. INSERT TEST APPOINTMENTS
-- ============================================================
-- Note: Make sure the patient_id and doctor_id match the IDs from above inserts
INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time, status, reason) VALUES
(1, 1, '2025-11-05', '10:00:00', 'Scheduled', 'Regular checkup'),
(2, 2, '2025-11-05', '11:30:00', 'Scheduled', 'Child vaccination'),
(3, 3, '2025-11-06', '14:00:00', 'Scheduled', 'Knee pain consultation'),
(4, 4, '2025-11-06', '09:00:00', 'Scheduled', 'Headache follow-up'),
(5, 1, '2025-11-07', '10:30:00', 'Scheduled', 'Blood pressure check'),
(6, 2, '2025-11-08', '15:00:00', 'Scheduled', 'Annual physical');

-- ============================================================
-- 4. INSERT TEST BILLING/INVOICES
-- ============================================================
-- Note: Adjust table name if your billing table is named differently (Billing vs Invoices)
INSERT INTO Billing (patient_id, amount, bill_date, status, description) VALUES
(1, 150.00, '2025-11-01', 'Pending', 'Consultation fee'),
(1, 75.50, '2025-11-02', 'Pending', 'Lab tests'),
(2, 200.00, '2025-11-01', 'Pending', 'Vaccination charges'),
(3, 300.00, '2025-10-28', 'Pending', 'X-ray and consultation'),
(5, 125.00, '2025-10-30', 'Pending', 'Blood pressure monitoring'),
(6, 180.00, '2025-10-29', 'Paid', 'Annual checkup package');

-- ============================================================
-- 5. VERIFICATION QUERIES - Run these to check data was inserted
-- ============================================================

-- Check Doctors
SELECT COUNT(*) as doctor_count FROM Doctors;
SELECT * FROM Doctors;

-- Check Patients  
SELECT COUNT(*) as patient_count FROM Patients;
SELECT patient_id, first_name, last_name, blood_group FROM Patients;

-- Check Appointments
SELECT COUNT(*) as appointment_count FROM Appointments;
SELECT a.appointment_id, p.first_name as patient_name, d.full_name as doctor_name, 
       a.appointment_date, a.status 
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id;

-- Check Billing
SELECT COUNT(*) as bill_count FROM Billing;
SELECT b.billing_id, p.first_name, p.last_name, b.amount, b.status, b.bill_date
FROM Billing b
JOIN Patients p ON b.patient_id = p.patient_id;

-- ============================================================
-- 6. TEST THE ACTUAL REPORT QUERIES
-- ============================================================

-- Test Appointments Report Query
SELECT 
    a.appointment_date, 
    a.appointment_time, 
    p.first_name, 
    p.last_name, 
    d.full_name AS doctor_name
FROM Appointments AS a
JOIN Patients AS p ON a.patient_id = p.patient_id
JOIN Doctors AS d ON a.doctor_id = d.doctor_id
WHERE a.status = 'Scheduled'
ORDER BY a.appointment_date, a.appointment_time;

-- Test Doctor Workload Report Query
SELECT 
    d.full_name,
    d.specialization,
    COUNT(a.appointment_id) AS scheduled_appointments
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.full_name, d.specialization
ORDER BY scheduled_appointments DESC;

-- Test Blood Group Report Query (for A+ blood group)
SELECT 
    p1.first_name,
    p1.last_name,
    p1.contact AS contact_number
FROM Patients AS p1
WHERE p1.blood_group = 'A+'
AND EXISTS (
    SELECT 1 FROM Patients p2 
    WHERE p2.blood_group = 'A+' 
    AND p2.patient_id != p1.patient_id
);

-- Test All Patients Pending Bills Query
SELECT 
    p.patient_id,
    p.first_name,
    p.last_name,
    p.contact,
    b.billing_id,
    b.amount,
    b.bill_date,
    b.status
FROM Patients p
LEFT JOIN Billing b ON p.patient_id = b.patient_id
WHERE b.status = 'Pending' OR b.status IS NULL
ORDER BY p.patient_id, b.bill_date DESC;

-- ============================================================
-- NOTES AND TROUBLESHOOTING:
-- ============================================================
-- 1. If you get "Unknown column 'contact'" error for Patients:
--    Your table might use 'phone' or 'phone_number' or 'contact_number'
--    Replace 'contact' with the correct column name from DESCRIBE Patients;
--
-- 2. If you get error for Doctors 'contact':
--    Replace with 'phone' if that's what your table uses
--
-- 3. If you get "Unknown column 'dob'":
--    Replace with 'date_of_birth' or 'birth_date'
--
-- 4. Run this to see exact column names:
--    SHOW COLUMNS FROM Patients;
--    SHOW COLUMNS FROM Doctors;
--
-- ============================================================
-- ALTERNATIVE INSERT QUERIES (if column names are different)
-- ============================================================

-- IF Patients table uses 'phone' instead of 'contact':
/*
INSERT INTO Patients (first_name, last_name, gender, dob, phone, email, blood_group, address, medical_history) VALUES
('David', 'Johnson', 'Male', '1985-05-15', '5551112222', 'david@example.com', 'A+', '123 Main St', 'Asthma, seasonal allergies');
-- ... (repeat for all patients)
*/

-- IF Patients table uses 'date_of_birth' instead of 'dob':
/*
INSERT INTO Patients (first_name, last_name, gender, date_of_birth, contact, email, blood_group, address, medical_history) VALUES
('David', 'Johnson', 'Male', '1985-05-15', '5551112222', 'david@example.com', 'A+', '123 Main St', 'Asthma, seasonal allergies');
-- ... (repeat for all patients)
*/

-- IF Patients table uses 'phone_number' instead of 'contact':
/*
INSERT INTO Patients (first_name, last_name, gender, dob, phone_number, email, blood_group, address, medical_history) VALUES
('David', 'Johnson', 'Male', '1985-05-15', '5551112222', 'david@example.com', 'A+', '123 Main St', 'Asthma, seasonal allergies');
-- ... (repeat for all patients)
*/

-- ============================================================
