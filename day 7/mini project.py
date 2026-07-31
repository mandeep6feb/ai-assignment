import pandas as pd
import numpy as np
import json

# Read CSV File
df = pd.read_csv("student.csv")

print("real Data")
print(df)

print("\nMissing Values")
print(df.isnull())

print("\nTotal Missing Values")
print(df.isnull().sum())


df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

print("\nData After Cleaning")
print(df)


print("\nStatistics")

print("Average Marks")
print(df[["Math", "Science", "English"]].mean())

print("\nHighest Marks")
print(df[["Math", "Science", "English"]].max())

print("\nLowest Marks")
print(df[["Math", "Science", "English"]].min())


df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Percentage"] = (df["Total"] / 300) * 100
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)


df = df.sort_values(by="Percentage", ascending=False)

df["Rank"] = range(1, len(df) + 1)

print("\nStudent Ranking")
print(df)


name = input("\nEnter Student Name: ")

result = df[df["Name"].str.lower() == name.lower()]

if len(result) > 0:
    print("\nStudent Found")
    print(result)
else:
    print("Student Not Found")


df.to_csv("result.csv", index=False)

print("\nResult exported successfully.")
# Summary JSON
summary = {
    "Total Students": int(len(df)),
    "Average Percentage": float(df["Percentage"].mean()),
    "Highest Percentage": float(df["Percentage"].max()),
    "Lowest Percentage": float(df["Percentage"].min()),
    "Topper": df.iloc[0]["Name"]
}
with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)
print("\nSummary JSON Created Successfully.")