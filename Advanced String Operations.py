
text = "Hello World"
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with 'World': {text.endswith('World')}")


mixed_str = "Data123#Science!"

clean_str = "".join(char for char in mixed_str if char.isalpha())
print(f"Cleaned string: {clean_str}")


print(f"Reversed 'Python': {'Python'[::-1]}")