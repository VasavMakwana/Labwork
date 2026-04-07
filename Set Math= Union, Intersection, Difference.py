set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# All unique elements from both
print(f"Union: {set_a | set_b}") 

# Common elements
print(f"Intersection: {set_a & set_b}")

# In set_a but not in set_b
print(f"Difference (a-b): {set_a - set_b}")