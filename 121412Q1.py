# Initialize an empty list to store patients
patients = []


# Function to add a new patient
def add_patient():
    print("\nEnter patient details:")
    name = input("Name: ")
    age = input("Age: ")
    illness = input("Illness: ")
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    patients.append(patient)
    print(f"\nPatient '{name}' added successfully.")


# search for patients in the system
def display_patients():
    if not patients:
        print("\n no patients found")
    else:
        print("\n list all patients found")
    for idx, patient in enumerate(patients, start=1):
        print(f"{idx}. Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")


# search for patient by name

def search_patient():
    if not patients:
        print("\n no patients found")
    return

    search_name = input("\nEnter the name of the patient to search: ")
    found = False
    for patient in patients:
        if patient['name'].lower() == search_name.lower():
            print("\nPatient found:")
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            found = True
            break

    if not found:
        print(f"\nPatient '{search_name}' not found.")

    def remove_patient():
        if not patients:
            print("\nNo patients found.")
            return
    remove_name = input("patients name")
    removed = False
    for patient in patients:
        if patient['name'].lower() == remove_name.lower():
            patients.remove(patient)
            print(f"\nPatient '{remove_name}' removed successfully.")
            removed = True
            break

    if not removed:
        print(f"\nPatient '{remove_name}' not found.")


while True:
    print("\nHospital Patient Management System")
    print("1. Add a new patient")
    print("2. Display all patients")
    print("3. Search for a patient by name")
    print("4. Remove a patient by name")
    print("5. Exit the program")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        display_patients()
    elif choice == '3':
        search_patient()
    elif choice == '4':
        remove_patient()
    elif choice == '5':
        print("\n PROGRAM EXIT")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
