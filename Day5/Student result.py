import numpy as np

# Student Marks Dataset
# Rows = Students, Columns = Subjects
marks = np.array([
    [85, 78, 92],
    [76, 88, 81],
    [90, 67, 85],
    [60, 72, 70],
    [95, 89, 98]
])

subjects = ["Math", "Science", "English"]

# Average of all marks
print("Overall Average:", np.mean(marks))

# Highest Score
print("Highest Score:", np.max(marks))

# Lowest Score
print("Lowest Score:", np.min(marks))

# Subject-wise Statistics
print("\nSubject-wise Statistics:")
for i in range(len(subjects)):
    print(subjects[i])
    print(" Average:", np.mean(marks[:, i]))
    print(" Highest:", np.max(marks[:, i]))
    print(" Lowest :", np.min(marks[:, i]))
    print()

# Overall Performance of each student
print("Overall Performance:")
student_avg = np.mean(marks, axis=1)

for i in range(len(student_avg)):
    if student_avg[i] >= 85:
        grade = "Excellent"
    elif student_avg[i] >= 70:
        grade = "Good"
    elif student_avg[i] >= 50:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print(f"Student {i+1}: Average = {student_avg[i]:.2f}, Performance = {grade}")