class Person(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class Teenager(Person):
    def __init__(self, name, phone):
        Person.__init__(self, name, phone)
        self.website="";

mike=Teenager("Mike", "450-564-9891");
jake=Person("Jake", "650-123-3215");

print(mike.name);
print(jake.name);
