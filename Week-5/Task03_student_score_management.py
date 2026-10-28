class Student:
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print(f"School: {self.school_name}")
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Department: {self.department}")
        print("--------------------")


# Create three student objects
student1 = Student("Sara", 85, "Software Engineering")
student2 = Student("Abebe", 72, "Computer Science")
student3 = Student("Kebede", 90, "Information Technology")

# Display all students
student1.display()
student2.display()
student3.display()

# Update Sara's score
student1.score = 95

print("After updating Sara's score:")
student1.display()

# Demonstrate independent scores
print("Other students' scores:")
print(f"Abebe: {student2.score}")
print(f"Kebede: {student3.score}")
  