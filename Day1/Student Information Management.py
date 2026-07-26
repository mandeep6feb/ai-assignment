print("===== Student Information =====")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
course = input("Enter Course: ")

math = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

total = math + science + english
average = total / 3

print("\n----- Student Report -----")
print("Name :", name)
print("Roll No :", roll)
print("Course :", course)
print("Maths :", math)
print("Science :", science)
print("English :", english)
print("Total :", total)
print("Average :", round(average, 2))

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade :", grade)