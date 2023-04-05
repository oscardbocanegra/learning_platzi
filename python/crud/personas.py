

class Persona:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and i\'m {self.age} years old')

if __name__ == '__main__':
    person = Persona('David', 18)

    print(f'Age {person.age}')
    person.say_hello()