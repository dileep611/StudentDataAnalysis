def calculate_highest_maths(student_list):
    highest_marks_in_maths = 0
    highest_marks_in_maths_name = ''
    for student in student_list:
        if (student.get("Maths") > highest_marks_in_maths):
            highest_marks_in_maths = student.get("Maths")
            highest_marks_in_maths_name = student.get("Name")
    print(f"Highest score in maths is {highest_marks_in_maths} by {highest_marks_in_maths_name}")

def calculate_highest_Science(student_list):
    highest_marks_in_Science = 0
    highest_marks_in_Science_name = ''
    for student in student_list:
        if (student.get("Science") > highest_marks_in_Science):
            highest_marks_in_Science = student.get("Science")
            highest_marks_in_Science_name = student.get("Name")
    print(f"Highest score in Science is {highest_marks_in_Science} by {highest_marks_in_Science_name}")

def calculate_highest_Social(student_list):
    highest_marks_in_Social = 0
    highest_marks_in_Social_name = ''
    for student in student_list:
        if (student.get("Social") > highest_marks_in_Social):
            highest_marks_in_Social= student.get("Social")
            highest_marks_in_Social_name = student.get("Name")
    print(f"Highest score in Social is {highest_marks_in_Social} by {highest_marks_in_Social_name}")

student_1 = {
    "Maths" : 45,
    "Science" : 75,
    "Social" : 65,
    "Name" : "Thanmay"
}

student_2 = {
    "Maths" : 75,
    "Science" : 85,
    "Social" : 96,
    "Name" : "Dheeraj"
}

student_3 = {
    "Maths" : 55,
    "Science" : 95,
    "Social" : 89,
    "Name" : "Suraj"
}

student_list = [student_1,student_2,student_3]

calculate_highest_maths(student_list)
calculate_highest_Science(student_list)
calculate_highest_Social(student_list)



