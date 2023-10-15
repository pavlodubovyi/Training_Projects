class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }

        self.contacts.append(contact)
        Contacts.current_id += 1

        # return self.contacts


all_persons = Contacts()  # зробимо один спільний обʼєкт классу Contacts

all_persons.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)  # додали один контакт
all_persons.add_contacts('Cyrus Jackson', '(501) 472-5218', 'nibh@semsempererat.com', False)  # додали другий

print(all_persons.list_contacts)  # тут будуть вже 2 елемента
