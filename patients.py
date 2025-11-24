from data import patients

def add_patient():
    pid = input("Enter patient ID: ")
    if pid in patients:
        print("Patient already exists.")
        return
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    patients[pid] = {"name": name, "age": age}
    print("Patient added successfully.")

def view_patients():
    if not patients:
        print("No patients found.")
    else:
        for pid, info in patients.items():
            print(f"ID: {pid}, Name: {info['name']}, Age: {info['age']}")

def update_patient():
    pid = input("Enter patient ID to update: ")
    if pid not in patients:
        print("Patient not found.")
        return
    patients[pid]['name'] = input("Enter new name: ")
    patients[pid]['age'] = input("Enter new age: ")
    print("Patient updated successfully.")

def delete_patient():
    pid = input("Enter patient ID to delete: ")
    if pid in patients:
        del patients[pid]
        print("Patient deleted.")
    else:
        print("Patient not found.")
