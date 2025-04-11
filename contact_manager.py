import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)

    print(f"✅ Contact '{name}' added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📂 No contacts found.")
    else:
        print("\n📖 Contact List:")
        for name, info in contacts.items():
            print(f"{name}: {info['Phone']} | {info['Email']}")

# Edit contact
def edit_contact():
    contacts = load_contacts()
    name = input("Enter the contact name to edit: ").strip()

    if name in contacts:
        phone = input("Enter new Phone Number: ").strip()
        email = input("Enter new Email: ").strip()
        contacts[name] = {"Phone": phone, "Email": email}
        save_contacts(contacts)
        print(f"✅ Contact '{name}' updated successfully!")
    else:
        print("❌ Contact not found!")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter the contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"✅ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found!")

# Main menu
def main():
    while True:
        print("\n📞 Contact Management System")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Edit Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Management System.")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
