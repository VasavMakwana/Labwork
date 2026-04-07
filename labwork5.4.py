# Create list of dictionaries
students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

# Print names using loop
print("Student Names:")
for student in students:
    print(student["name"])

#  Print average score
total = sum(student["score"] for student in students)
avg = total / len(students)
print("\nAverage Score:", avg)

#  Add a new student
students.append({"id": 104, "name": "David", "score": 88})

#  Update score of student with ID 102
for student in students:
    if student["id"] == 102:
        student["score"] = 88

# Delete student named "Charlie"
students = [s for s in students if s["name"] != "Charlie"]

#  Print students who scored more than 80
print("\nStudents with score > 80:")
for student in students:
    if student["score"] > 80:
        print(student["name"])

#  Sort students by score (descending)
students.sort(key=lambda x: x["score"], reverse=True)
print("\nSorted Students (Descending by Score):")
for student in students:
    print(student)

#  Find highest score student
top_student = max(students, key=lambda x: x["score"])
print("\nTop Student:", top_student)

#  Create report with grades
print("\nStudent Report:")
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

for student in students:
    grade = get_grade(student["score"])
    print(f"Name: {student['name']} | Score: {student['score']} | Grade: {grade}")

# Count students in each grade
grade_count = {"A": 0, "B": 0, "C": 0}
for student in students:
    grade = get_grade(student["score"])
    grade_count[grade] += 1

print("\nGrade Count:", grade_count)

#  Convert to Pandas DataFrame
import pandas as pd

df = pd.DataFrame(students)
print("\nDataFrame:\n", df)

#  Export to CSV
df.to_csv("students.csv", index=False)
print("\nData exported to students.csv")

#  Re-import and calculate stats
df2 = pd.read_csv("students.csv")
print("\nRe-imported Data:\n", df2)

print("\nStatistics:")
print("Mean:", df2["score"].mean())
print("Min:", df2["score"].min())
print("Max:", df2["score"].max())