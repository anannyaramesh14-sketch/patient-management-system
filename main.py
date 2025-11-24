import patients
import appointments
import doctors
import history

def main():
    while True:
        print("\nPatient Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Add Doctor")
        print("6. View Doctors")
        print("7. Book Appointment")
        print("8. View Appointments")
        print("9. Cancel Appointment")
        print("10. Add Medical History")
        print("11. View Medical History")
        print("12. Exit")
        choice = input("Enter your choice (1-12): ")
        
        if choice == "1":
            patients.add_patient()
        elif choice == "2":
            patients.view_patients()
        elif choice == "3":
            patients.update_patient()
        elif choice == "4":
            patients.delete_patient()
        elif choice == "5":
            doctors.add_doctor()
        elif choice == "6":
            doctors.view_doctors()
        elif choice == "7":
            appointments.book_appointment()
        elif choice == "8":
            appointments.view_appointments()
        elif choice == "9":
            appointments.cancel_appointment()
        elif choice == "10":
            history.add_medical_history()
        elif choice == "11":
            history.view_medical_history()
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
