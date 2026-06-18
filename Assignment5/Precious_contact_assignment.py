contacts = []

# Validation Functions

def validate_phone(phone):
    """
    Phone number should contain only digits, '+' and '-'
    Example: +256-701234567
    """
    for char in phone:
        if not (char.isdigit() or char in ['+', '-']):
            return False
    return True


def validate_email(email):
    """
    Email must contain @ and .
    """
    if email == "":
        return True

    return "@" in email and "." in email


# CRUD Functions

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")

    if not validate_phone(phone):
        print("Error: Invalid phone number.")
        return

    if not validate_email(email):
        print("Error: Invalid email address.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully.")


def view_contact():
    name = input("Enter contact name to view: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\n--- Contact Details ---")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")

            if not validate_phone(new_phone):
                print("Error: Invalid phone number.")
                return

            if not validate_email(new_email):
                print("Error: Invalid email.")
                return

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

# Search Functions

def search_contacts():
    keyword = input("Enter name, phone, or email to search: ").lower()

    results = []

    for contact in contacts:
        if (keyword in contact["name"].lower() or
                keyword in contact["phone"].lower() or
                keyword in contact["email"].lower()):
            results.append(contact)

    if not results:
        print("No matching contacts found.")
        return

    print("\n=== Search Results ===")

    for i, contact in enumerate(results, start=1):
        print(f"\nContact {i}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


# List Contacts

def list_all_contacts():

    if not contacts:
        print("No contacts available.")
        return

    print("\n=== All Contacts ===")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")

# Main Menu

def main():

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            search_contacts()

        elif choice == "6":
            list_all_contacts()

        elif choice == "7":
            print("Exiting Contact Manager...")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()