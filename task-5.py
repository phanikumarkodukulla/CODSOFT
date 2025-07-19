contacts = {}

def show_menu():
    print("\n" + "="*30)
    print("       My Contact Book")
    print("="*30)
    print("1. Add new contact")
    print("2. View all contacts") 
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    print("-"*30)

def add_contact():
    print("\nAdd New Contact")
    print("-"*15)
    
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    if name.lower() in contacts:
        print(f"{name} already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name.lower()] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    print(f"\n{name} has been added successfully!")

def view_all_contacts():
    if not contacts:
        print("\nNo contacts found!")
        return
    
    print(f"\nAll Contacts ({len(contacts)} total)")
    print("-"*40)
    
    for key, contact in contacts.items():
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-"*40)

def search_contact():
    if not contacts:
        print("\nNo contacts to search!")
        return
    
    search_term = input("\nEnter name or phone to search: ").strip().lower()
    found_contacts = []
    
    for key, contact in contacts.items():
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)
    
    if found_contacts:
        print(f"\nFound {len(found_contacts)} contact(s):")
        print("-"*30)
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-"*30)
    else:
        print("No contacts found!")

def update_contact():
    if not contacts:
        print("\nNo contacts to update!")
        return
    
    name = input("\nEnter name of contact to update: ").strip().lower()
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    contact = contacts[name]
    print(f"\nUpdating contact: {contact['name']}")
    print("(Press Enter to keep current value)")
    
    new_name = input(f"Name ({contact['name']}): ").strip()
    new_phone = input(f"Phone ({contact['phone']}): ").strip()
    new_email = input(f"Email ({contact['email']}): ").strip()
    new_address = input(f"Address ({contact['address']}): ").strip()
    
    if new_name:
        del contacts[name]
        name = new_name.lower()
        contact['name'] = new_name
    
    if new_phone:
        contact['phone'] = new_phone
    if new_email:
        contact['email'] = new_email
    if new_address:
        contact['address'] = new_address
    
    contacts[name] = contact
    print("Contact updated successfully!")

def delete_contact():
    if not contacts:
        print("\nNo contacts to delete!")
        return
    
    name = input("\nEnter name of contact to delete: ").strip().lower()
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    contact_name = contacts[name]['name']
    confirm = input(f"Are you sure you want to delete {contact_name}? (y/n): ").lower()
    
    if confirm == 'y':
        del contacts[name]
        print(f"{contact_name} has been deleted!")
    else:
        print("Delete cancelled.")

def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("Please enter a number between 1 and 6")
        except ValueError:
            print("Please enter a valid number")

def run_contact_book():
    print("Welcome to your Contact Book!")
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_all_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("\nThanks for using Contact Book!")
            break

if __name__ == "__main__":
    run_contact_book()