import numpy as np
marks = np.array([
    [80, 70, 90],
    [60, 75, 65],
    [90, 85, 95],
    [50, 60, 55]
])
print("Student Marks:")
print(marks)
print("Average:", np.mean(marks))
print("Highest Score:", np.max(marks))
print("Lowest Score:", np.min(marks))
print("Subject Average:", np.mean(marks, axis=0))
average = np.mean(marks)

if average >= 75:
    print("Overall Performance: Excellent")
elif average >= 50:
    print("Overall Performance: Good")
else:
    print("Overall Performance: Needs Improvement")