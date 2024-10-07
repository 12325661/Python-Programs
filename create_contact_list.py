contact_list = [
    ("Lily", 12345678),
    ("Adam", 23456777),
    ("Danil", 53627364),
    ("Dave", 355574536),
    ("Grace", 69486763),
    ("Helen", 64586845)
]

# Add operation
def Add(name, number):
    contact_list.append((name, number))
    print(f"Contact {name} added successfully!")

# Search operation
def Search(name):
    for contact_name, number in contact_list:
        if contact_name == name:
            return number
    return "Contact not found."

# Delete operation
def Delete(name):
    for contact in contact_list:
        if contact[0] == name:
            contact_list.remove(contact)
            print(f"Contact {name} deleted successfully!")
            return
    print("Contact not found.")

# Display the contact list
def Display():
    return contact_list
