students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

# Validate a student's score.
def validate_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False

# Calculate a grade.
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Calculate the average score.
def calculate_average(students_list):
    total = 0

    for student in students_list:
        total += student["score"]

    if len(students_list) == 0:
        return 0

    return total / len(students_list)

# Find the highest and lowest scores.
def find_highest_lowest(students_list):
    if not students_list:
        return None, None

    highest = students_list[0]["score"]
    lowest = students_list[0]["score"]

    for student in students_list:
        score = student["score"]

        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

    return highest, lowest

# Count passed and failed students.
def count_passed_failed(students_list):
    passed = 0
    failed = 0
    for student in students_list:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1
    return passed, failed

# Generate a report for the class.
def generate_report(students_list):
    for student in students_list:
        score = student["score"]

        if not validate_score(score):
            print(f"Invalid score for {student['name']}: {score}")
            continue

        grade = calculate_grade(score)
        print(f"{student['name']}: Score = {score}, Grade = {grade}")

    average = calculate_average(students_list)
    highest, lowest = find_highest_lowest(students_list)
    passed, failed = count_passed_failed(students_list)

    print("\nClass Report")
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")
    
def students_above_average(students_list):
    average = calculate_average(students_list)
    result = []

    for student in students_list:
        if student["score"] > average:
           result.append(student)

    return result    
generate_report(students)
print("\nStudents Above Average:")
print(students_above_average(students))   