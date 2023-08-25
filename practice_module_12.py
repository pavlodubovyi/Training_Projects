# import pickle


# class Human:
#     def __init__(self, name):
#         self.name = name


# bob = Human("Bob")
# encoded_bob = pickle.dumps(bob)

# decoded_bob = pickle.loads(encoded_bob)

# bob.name == decoded_bob.name  # True
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        
  

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        elif contacts:
            
        

    def save_to_file(self):
        
            

    def read_from_file(self):
        
            
        