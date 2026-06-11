def count(s):
    letters = 0
    digits = 0
    others = 0
    
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            others += 1
    
    return (letters, digits, others)


s = input()
print(count(s))