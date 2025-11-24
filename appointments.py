from data import appointments, patients, doctors

def book_appointment():
    pid = input("Enter patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return
    doctor_id = input("Enter doctor ID: ")
    if doctor_id not in doctors:
        print("Doctor not found.")
        return
    date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment = {'patient_id': pid, 'doctor_id': doctor_id, 'date': date}
    appointments.append(appointment)
    print("Appointment booked successfully.")

def view_appointments():
    if not appointments:
        print("No appointments found.")
    else:
        for appt in appointments:
            print(f"Patient ID: {appt['patient_id']}, Doctor ID: {appt['doctor_id']}, Date: {appt['date']}")

def cancel_appointment():
    pid = input("Enter patient ID to cancel appointment: ")
    date = input("Enter appointment date to cancel (YYYY-MM-DD): ")
    for appt in appointments:
        if appt['patient_id'] == pid and appt['date'] == date:
            appointments.remove(appt)
            print("Appointment cancelled.")
            return
    print("Appointment not found.")
