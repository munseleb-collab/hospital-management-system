# Hospital Management System

## Project Description

The Hospital Management System is a Python-based application developed to help manage common hospital operations efficiently.

The system uses **SQLite** for database management and provides functionality for managing patients, doctors, appointments, billing, prescriptions, medical history, reports, and hospital analytics.

The project also includes a self-generated hospital dataset containing **550 patient records** and related hospital records. The dataset is designed to realistically simulate hospital operations for data analysis and system demonstration.

---

## Dataset Information

The project uses a **self-generated dataset that realistically simulates real-world hospital conditions**.

The final dataset contains:

| Dataset       |   Records |
| ------------- | --------: |
| Patients      |       550 |
| Doctors       |        20 |
| Appointments  |       550 |
| Bills         |       550 |
| Prescriptions |       550 |
| **Total**     | **2,220** |

The dataset satisfies the requirement of having at least **500 records**.

The data is stored in both the SQLite database and CSV files.

### Dataset Files

* `patients.csv`
* `doctors.csv`
* `appointments.csv`
* `bills.csv`
* `prescriptions.csv`

---

## Features

### User Management

* User registration
* Login authentication
* Password hashing
* Role-based access functionality

### Patient Management

* Register patients
* View patients
* Search patient records
* Update patient information
* Delete patient records
* Patient medical history

### Doctor Management

* Register doctors
* View doctors
* Doctor specialization management

### Appointment Management

* Book appointments
* Store appointment dates and times
* Record appointment reasons
* Link appointments to patients and doctors

### Billing

* Create patient bills
* Record hospital services
* Record bill amounts
* Track payment status
* Calculate total hospital revenue

### Prescription Management

* Add prescriptions
* Record medicines
* Record dosage
* Record medication instructions
* Link prescriptions to patients and doctors

### Reports

* Generate patient PDF reports
* View hospital records
* Generate analytical reports

### Analytics

* Patient gender analysis
* Patient age-group analysis
* Diagnosis analysis
* Doctor specialization analysis
* Appointment analysis
* Billing and revenue analysis
* Payment status analysis
* Prescription and medicine analysis
* Data visualizations using Matplotlib

### Database

* SQLite database
* Database backup functionality
* Related tables for hospital operations

### Dataset Export

The system can export the database tables into CSV files for analysis and submission.

---

## Technologies Used

* **Python** – Application development
* **SQLite** – Database management
* **Pandas** – Data analysis and CSV processing
* **Matplotlib** – Data visualization
* **ReportLab** – PDF report generation
* **Git** – Version control

---

## Database Structure

The SQLite database contains the following main tables:

```text
users
patients
doctors
appointments
bills
prescriptions
```

The tables are related through patient and doctor IDs.

For example:

```text
Patients
   │
   ├── Appointments
   │
   ├── Bills
   │
   └── Prescriptions
          │
          └── Doctors
```

All generated appointments, bills, and prescriptions use valid patient and doctor IDs.

---

## Project Structure

| File                        | Description                                    |
| --------------------------- | ---------------------------------------------- |
| `main.py`                   | Main system menu                               |
| `database.py`               | Database creation and connection               |
| `patient.py`                | Patient registration                           |
| `doctor.py`                 | Doctor management                              |
| `appointment.py`            | Appointment booking                            |
| `billing.py`                | Billing management                             |
| `prescription.py`           | Prescription management                        |
| `medical_history.py`        | Patient medical history                        |
| `patient_report.py`         | PDF patient report generation                  |
| `dashboard.py`              | Hospital analytics dashboard                   |
| `analysis.py`               | Dataset analysis and visualization             |
| `export_dataset.py`         | Exports database tables to CSV                 |
| `generate_dataset.py`       | Generates the 550-patient dataset              |
| `generate_hospital_data.py` | Generates doctors and related hospital records |
| `database_backup.py`        | Database backup                                |
| `login.py`                  | User login                                     |
| `users.py`                  | User management                                |
| `search_patient.py`         | Patient search                                 |
| `update_patient.py`         | Patient information updates                    |
| `delete_patient.py`         | Patient deletion                               |
| `view_patients.py`          | Displays patient records                       |
| `view_doctors.py`           | Displays doctor records                        |
| `view_appointments.py`      | Displays appointments                          |
| `view_bills.py`             | Displays bills                                 |
| `view_prescriptions.py`     | Displays prescriptions                         |
| `hospital.db`               | Main SQLite database                           |
| `patients.csv`              | 550 patient records                            |
| `doctors.csv`               | 20 doctor records                              |
| `appointments.csv`          | 550 appointment records                        |
| `bills.csv`                 | 550 billing records                            |
| `prescriptions.csv`         | 550 prescription records                       |

---

## How to Run

### 1. Clone or download the project

Open the project folder in a terminal.

### 2. Install the required Python libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Hospital Management System

```bash
python main.py
```

### 4. Run the analytics

```bash
python analysis.py
```

### 5. Run the dashboard

```bash
python dashboard.py
```

### 6. Export the dataset

```bash
python export_dataset.py
```

This creates the following CSV files:

```text
patients.csv
doctors.csv
appointments.csv
bills.csv
prescriptions.csv
```

---

## Dataset Generation

The dataset was self-generated using Python to realistically simulate hospital operations.

The main patient dataset contains **550 records**, satisfying the minimum requirement of 500 records.

The supporting datasets contain:

* 20 doctors
* 550 appointments
* 550 bills
* 550 prescriptions

The generated data includes realistic fields such as:

* Patient names
* Age
* Gender
* Phone numbers
* Addresses
* Diagnoses
* Doctor specializations
* Appointment dates
* Appointment reasons
* Hospital services
* Bill amounts
* Payment statuses
* Medicines
* Dosages
* Prescription instructions

---

## Data Analysis Results

The dataset was analyzed using Pandas and Matplotlib.

Some of the findings include:

* Total patients: **550**
* Male patients: **277**
* Female patients: **273**
* Average patient age: **42.57 years**
* Most common diagnosis: **Gastritis**
* Total doctors: **20**
* Total appointments: **550**
* Total bills: **550**
* Total prescriptions: **550**
* Total recorded billing revenue: **ZMW 691,970.90**
* Average bill: **ZMW 1,258.13**
* Most prescribed medicine: **Azithromycin**

The project generates charts showing patient demographics, diagnoses, doctor specializations, appointment reasons, payment status, hospital revenue, and prescribed medicines.

---

## Security

The system includes password hashing for user authentication.

Passwords are not stored directly as plain text in the database.

---

## Database Backup

Database backup functionality is included to help protect hospital records.

Backups can be created before making major changes to the database.

---

## Purpose of the Project

The main purpose of this project is to demonstrate how a hospital management system can be developed using Python and SQLite while applying database management, data analysis, visualization, authentication, reporting, and version-control concepts.

The project also demonstrates how a self-generated dataset can be used to simulate real-world hospital data for analysis.

---

## Author

**Beatrice Munsele**

Hospital Management System Project
