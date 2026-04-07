text = input("Enter a string: ")
reversed_text = text[::-1]

print(f"Reversed string: {reversed_text}")

if text.lower() == reversed_text.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")