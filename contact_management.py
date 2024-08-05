import json
import re

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Validate phone number (simple check)
def is_valid_phone(phone):
    return re.match(r"^[+]?\d{10,15}$", phone) is not None

# Validate email address
def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not is_valid_phone(phone) or not is_valid_email(email):
        print("Invalid input. Please enter valid details.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact with this name already exists.")
            return

    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")

# Search for a contact by name
def search_contact(contacts):
    search_name = input("Enter the name to search: ").strip()
    results = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

# Update an existing contact
def update_contact(contacts):
    search_name = input("Enter the name to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()
            
            if not is_valid_phone(new_phone) or not is_valid_email(new_email):
                print("Invalid input. Please enter valid details.")
                return

            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Display menu and handle user input
def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
