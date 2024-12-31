class calculator:
    def __init__(self,num1,num2):
        self.a=num1;
        self.b=num2;

    def add(self):
        add=self.a+self.b
        print(add)
    def sub(self):
        sub=self.a-self.b
        print(sub)
    def mul(self):
        mul=self.a*self.b
        print(mul)
    def div(self):
        div=self.a/self.b
        print(div)
        

c1=calculator(10,20)
c1.add()
c1.sub()
c1.mul()
c1.div()
