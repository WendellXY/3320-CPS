class Person:
    def __init__(self):
        pass

    def __init__(self, name: str = 'Unnamed', age: int = 0, weight: float = 0, height: float = 0):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_person_data(self):
        print('Name: {0}\nAge: {1}\nWeight: {2}\n'.format(self.name, self.age, self.weight))

    def input_person_data(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


def main():
    person_1 = Person()
    person_2 = Person()

    person_1.input_person_data('Jack', 11, 50.2, 1.4)
    person_2.input_person_data('Johnny', 18, 70.2, 1.80)

    person_1.get_person_data()
    person_2.get_person_data()

if __name__ == "__main__":
    main()