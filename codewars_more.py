from copy import deepcopy, copy


class Expenses:
    def __init__(self):
        self.data = {}
        self.places = []

    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self):
        copy_obj = Expenses()
        copy_obj.data = copy(self.data)
        copy_obj.places = copy(self.places)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Expenses()
        memo[id(copy_obj)] = copy_obj
        copy_obj.data = deepcopy(self.data)
        copy_obj.places = deepcopy(self.places)
        return copy_obj


e = Expenses()
e.spent("hotel", 100)
e.spent("taxi", 10)
print(e.places)  # ['hotel', 'taxi']

e_copy = copy(e)
print(e_copy is e)  # False
e_copy.spent("bar", 30)
print(e.places)  # ['hotel', 'taxi', 'bar']

e_deep_copy = deepcopy(e)
print(e_deep_copy is e)  # False
e_deep_copy.spent("airport", 300)
print(e.places)  # ['hotel', 'taxi', 'bar']
print(e_deep_copy.places)  # ['hotel', 'taxi', 'bar', 'airport']
