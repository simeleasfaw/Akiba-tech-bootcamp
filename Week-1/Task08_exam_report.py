Student_name = input("Enter your name: ")
Python_score = float(input("Enter your Python score: "))
English_score = float(input("Enter your English score: "))
Mathematics_score = float(input("Enter your Mathematics score: "))

Total_average = (Python_score + English_score + Mathematics_score) / 3

print("==========================================")
print("           STUDENT RESULT                 ")
print("==========================================")
print(f"Student Name: {Student_name}")
print()
print(f"Python Score: {Python_score:.2f}")
print(f"English Score: {English_score:.2f}")
print(f"Mathematics Score: {Mathematics_score:.2f}")

print("-"* 40)
print()
print(f"Total Average: {Total_average:.2f}")
print("===========================================")
