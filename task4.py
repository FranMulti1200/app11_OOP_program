class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


user = User(name="john", birthyear=1999)

print(user.age(current_year=2024))



