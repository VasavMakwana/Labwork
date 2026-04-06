text = "PYTHON"

for ch in text:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(ch)