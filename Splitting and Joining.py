
fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")
print(f"List: {fruit_list}")


words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Joined sentence: {sentence}")


multiline = "Line 1\nLine 2\nLine 3"
for line in multiline.splitlines():
    print(line)