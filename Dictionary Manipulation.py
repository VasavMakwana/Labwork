student = {"name": "Vasav", "age": 20, "grade": "A"}

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")


student["city"] = "Gujrat"


student["age"] = 21


del student["grade"]

print(f"Updated Dictionary: {student}")