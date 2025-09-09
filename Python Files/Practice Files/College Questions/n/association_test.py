class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def enroll(self, student):
        print(f"{student.name} enrolled")

s = Student("Alice")
c = Course()
c.enroll(s)  # Association


class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self, engine):
        self.engine = engine

e = Engine()
c = Car(e)
c.engine.start()  # Aggregation
Engine().start()  # Composition