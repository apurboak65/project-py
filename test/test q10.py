def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    
    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    elif step < 0:
        while start > stop:
            result.append(start)
            start += step
    
    return result


vals = eval(input())
print(my_range(*vals))