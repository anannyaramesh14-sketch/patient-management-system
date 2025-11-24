# Medical Management System

A modular Python application for managing patient records, doctor information, appointments, and medical histories in a clinical setting.

## 🏥 Project Overview

The Medical Management System (MMS) streamlines clinic operations by replacing paper-based recordkeeping with an efficient, menu-driven digital interface.  
This project demonstrates modular program design, practical data handling, and robust error management suitable for first-semester software engineering projects.

---

## ✨ Key Features

- Patient registration, edit/view details
- Doctor profile management and lookup
- Appointment scheduling and calendar
- Patient medical history entry and retrieval
- Search and validation across modules
- Modular separation: patients, doctors, appointments, history, main, shared data
- Informative error messages and menu guidance

---

## 📂 Technologies Used

- Python 3.x
- Standard library only (no external dependencies)
- Modular file structure (six .py modules plus shared data)

---

## ⚡ Quick Start

### 1. Clone or download the repository  
### 2. Make sure Python 3.x is installed  
Test by running:
python --version

### 3. Run the project from the terminal:
python main.py

### 4. Use the interactive menu to:
  - Register/manage patients and doctors
  - Schedule and view appointments
  - Record and review medical histories

---

## 📁 Folder Structure

| File           | Description                        |
| -------------- | ---------------------------------- |
| main.py        | Main menu and routing              |
| patients.py    | Patient registration, data ops     |
| doctors.py     | Doctor management module           |
| appointments.py| Appointment scheduler/viewer       |
| history.py     | Medical history entry/view         |
| data.py        | Central shared data storage        |

---

## 🗄 Data Flow

- All patient, doctor, appointment, and history data managed in memory for simplicity.
- Each module interacts via shared data dictionaries/lists.
- Validations included for all user inputs.

---

## 🚦 Limitations

- **No persistent storage**: All records reset on restart (in-memory only)
- **Single-clinic focus**; not scalable for multiple branches
- **Console-only**: No GUI/web interface yet
- **Minimal security**: No user authentication, open access

---

## 🚀 Future Scope

- Add database (SQLite/MySQL) or file-based persistence
- Implement user authentication (admin access)
- Build GUI (Tkinter/PyQt) or web dashboard
- Enable export/import of records as CSV/PDF
- Support multiple clinics/doctors per location
- Improve calendar and notifications (email/SMS)
- Add analytics: visits, health trends, doctor load

---

## 📝 Testing Methodology

- Validated edge cases: empty input, duplicate records, incomplete data
- Menu navigation tested for all modules
- Appointment conflicts and data cross-checks manually verified

---

## 📚 Documentation and Code Quality

- Each function and module is well-commented for clarity
- README & statement.md included for project context
- Naming conventions and modularity follow best Python practices

---

## 👤 Author

Anannya Ramesh K.
BTech Computer Science – VIT Bhopal  