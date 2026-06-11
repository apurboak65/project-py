import random

def gen_points():
    q1 = q2 = q3 = q4 = 0
    
    for i in range(100):
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        
        if x > 0 and y > 0:
            q1 += 1
        elif x < 0 and y > 0:
            q2 += 1
        elif x < 0 and y < 0:
            q3 += 1
        elif x > 0 and y < 0:
            q4 += 1
    
    return (q1, q2, q3, q4)

random.seed(input())
print(gen_points())
