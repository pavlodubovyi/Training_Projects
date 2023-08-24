import csv

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Pavlo Dubovyi",
        "email": "pavlodubovyi@yahoo.com",
        "phone": "1234567890",
        "favorite": True,
    },
    {
        "name": "John Doe",
        "email": "john.doe@nowhere.to.go",
        "phone": None,
        "favorite": False,
    },
]

filename = "my_contacts.csv"


def write_contacts_to_file(filename, contacts):
    field_names = []
    for el in contacts:
        for key in el.keys():
            field_names.append(key)
        break

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(contacts)


def read_contacts_from_file(filename):
    contact_list = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contact = {
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "favorite": row["favorite"] == "True",
            }
            contact_list.append(contact)
    return contact_list


write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))
