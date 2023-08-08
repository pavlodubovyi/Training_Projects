class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for el in self.contacts:
            if el["id"] == id:
                self.contacts.remove(el)


    
first_person = Contacts()
second_person = Contacts()
first_person.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
second_person.add_contacts('Cyrus Jackson', '(501) 472-5218', 'nibh@semsempererat.com', False)
contacts = Contacts.list_contacts
print(contacts)
