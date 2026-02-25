s = input().lower()
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
