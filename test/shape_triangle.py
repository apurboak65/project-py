def judgeTri(a, b, c):
    a, b, c = sorted([a, b, c])
    
    if a + b <= c:
        return "ERROR"
    
    sum_of_squares = a*a + b*b
    c_squared = c*c
    
    if abs(sum_of_squares - c_squared) < 1e-9:
        return "Z"
    elif sum_of_squares > c_squared:
        return "R"
    else:
        return "D"


a, b, c = eval(input())
print(judgeTri(a, b, c))
