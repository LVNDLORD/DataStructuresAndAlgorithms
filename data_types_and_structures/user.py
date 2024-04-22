class User:
    def __init__(self, first_name, last_name, username, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}\n"
              f"Username: {self.username}\n"
              f"Email: {self.email}\n"
              f"Location: {self.city}")

    def greet_user(self):
        print(f"Welcome back {self.username}!")


if __name__ == '__main__':
    Matti = User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
    Matti.describe_user()

    Maila = User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
    Maila.greet_user()

    Pekka = User('Pekka', 'Seppänen', 'pseppanen', 'p.Seppanen@yle.fi', 'Espoo')
    Pekka.describe_user()
    Pekka.greet_user()
