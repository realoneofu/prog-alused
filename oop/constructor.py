"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
    pass


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage
    Empty()
    # 3 x person usage
    person1 = Person()
    person1.firstname = "Eto"
    person1.lastname = "Eta"
    person1.age = 18
    person2 = Person()
    person2.firstname = "Ete"
    person2.lastname = "Etu"
    person2.age = 16
    person3 = Person()
    person3.firstname = "Ety"
    person3.lastname = "Ets"
    person3.age = 20
    # 3 x student usage
    s1 = Student("Tere", "Nimi", 12)
    s2 = Student("Yere", "Niti", 13)
    s3 = Student("Yello", "Nita", 14)
    pass

