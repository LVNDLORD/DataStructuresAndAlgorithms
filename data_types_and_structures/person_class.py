class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, my name is " + self.name)


if __name__ == '__main__':
    p = Person('Matti')
    p.hello()