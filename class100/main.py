class Student():
    def __init__(self, name, age, grade, bloodgroup, photo):
        self.name=name
        self.age=age
        self.grade=grade
        self.bloodgroup=bloodgroup
        self.photo=photo
    def setgrade(self):
        print('The student is in 8 grade')
nathan=Student('nathan',9, 8, 'A positive', 'photo')
print(nathan.name)
print(nathan.age)
print(nathan.setgrade())