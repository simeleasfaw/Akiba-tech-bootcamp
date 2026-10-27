class  Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def  display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
student1 = Student("Kebede", 20, "Computer Science")
student2 = Student("Abebe", 22, "Software Engineering")
student3 = Student("Marta", 21, "Information Technology")     

student1.display_info()
student2.display_info()
student3.display_info()   