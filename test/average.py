def avg_input():
    numbers = []
    
    while True:
        try:
            line = input()
            if line == '':
                break
            numbers.append(float(line))
        except:
            break
    
    if len(numbers) == 0:
        return 'N/A'
    else:
        average = sum(numbers) / len(numbers)
        return f"{average:.1f}"


print(avg_input())
