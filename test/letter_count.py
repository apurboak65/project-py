s = input().lower()

letter_count = {}

for char in s:
    if 'a' <= char <= 'z':
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

print(letter_count)
