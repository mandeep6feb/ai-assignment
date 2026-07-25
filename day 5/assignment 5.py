import numpy as np

# Student marks
marks = np.array([
    [80, 70, 90],
    [60, 75, 65],
    [90, 85, 95],
    [50, 60, 55]
])

print("Student Marks:")
print(marks)

# Average
print("Average:", np.mean(marks))

# Highest Score
print("Highest Score:", np.max(marks))

# Lowest Score
print("Lowest Score:", np.min(marks))

# Subject-wise Average
print("Subject-wise Average:", np.mean(marks, axis=0))

# Overall Performance
average = np.mean(marks)

if average >= 75:
    print("Overall Performance: Excellent")
elif average >= 50:
    print("Overall Performance: Good")
else:
    print("Overall Performance: Needs Improvement")