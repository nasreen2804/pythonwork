class shape():
    def area(self):
        return 0;
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b);

s1=shape()
print(s1.area())

r1=rectangle()
r1.area()
