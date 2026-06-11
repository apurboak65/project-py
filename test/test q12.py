class MyComplex:
    def __init__(self, self_real, image):
        self.real = self_real
        self.image = image
        
   # write your code here...

    def __add__(self, other):
        return MyComplex(
            self.real + other.real,
            self.image + other.image
        )

    def __sub__(self, other):
        return MyComplex(
            self.real - other.real,
            self.image - other.image
        )

    def __mul__(self, other):
        real = self.real * other.real - self.image * other.image
        image = self.real * other.image + self.image * other.real
        return MyComplex(real, image)

    def __str__(self):
        if self.image >= 0:
            return f"{self.real}+{self.image}j"
        else:
            return f"{self.real}{self.image}j"


def main():
    from random import seed,sample
    seed('mycomplex')    
    a1,b1 = sample(range(-5,5),2)    
    a2,b2 = sample(range(-5,5),2)
    c1 = MyComplex(a1,b1 )
    c2 = MyComplex(a2,b2 )
    for i in range(4):
        op = input()
        if op == '+':
            print(c1+c2)
        elif op == '-':
            print(c1-c2)
        elif op == '*':
            print(c1*c2)
        else:
            print(c1)
if __name__=="__main__":
    main()