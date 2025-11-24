from data import doctors

def add_doctor():
    did = input("Enter doctor ID: ")
    if did in doctors:
        print("Doctor already exists.")
        return
    name = input("Enter doctor name: ")
    speciality = input("Enter doctor speciality: ")
    doctors[did] = {"name": name, "speciality": speciality}
    print("Doctor added successfully.")

def view_doctors():
    if not doctors:
        print("No doctors found.")
    else:
        for did, info in doctors.items():
            print(f"ID: {did}, Name: {info['name']}, Speciality: {info['speciality']}")
