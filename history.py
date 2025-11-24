from data import medical_history, patients

def add_medical_history():
    pid = input("Enter patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return
    record = input("Enter medical history record: ")
    if pid not in medical_history:
        medical_history[pid] = []
    medical_history[pid].append(record)
    print("Medical history record added.")

def view_medical_history():
    pid = input("Enter patient ID to view history: ")
    if pid not in medical_history or not medical_history[pid]:
        print("No medical history found for this patient.")
    else:
        print(f"Medical History for {pid}:")
        for rec in medical_history[pid]:
            print(f"- {rec}")
