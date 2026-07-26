import pandas as pd
import numpy as np
import json

data = pd.read_csv("students.csv")
data = data.fillna(0)
data["Total"] = data["Math"] + data["Science"] + data["English"]
data["Average"] = np.mean(
    data[["Math", "Science", "English"]], axis=1
)
data["Rank"] = data["Total"].rank(
    ascending=False,
    method="min"
).astype(int)
print("\nStudent Data:")
print(data)
name = input("\nEnter student name to search: ")

result = data[data["Name"].str.lower() == name.lower()]

if len(result) > 0:
    print("\nStudent Found:")
    print(result)
else:
    print("Student not found!")
data.to_csv("student_results.csv", index=False)
summary = {
    "Total Students": len(data),
    "Highest Marks": int(data["Total"].max()),
    "Lowest Marks": int(data["Total"].min()),
    "Average Marks": float(data["Average"].mean())
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("\nResults saved in student_results.csv")
print("Summary saved in summary.json")