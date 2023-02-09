class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info (self):
        print(f"Name is: {self.name}")

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name is: {self.name}")

    def learn(self):
        print("Learning...")

    def set_class(self, className):
        self.className = className

    def get_class(self):
        return self.className

if __name__ == "__main__":
    p1 = People("John", 25)
    p1.info()

    student1 = Student("Sona", 33)
    student1.info()
    student1.set_class("first")
    print(student1.get_class())