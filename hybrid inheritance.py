class dad():
    def money(self):
        print("money");
class land():
    def important(self):
        print("imp land");

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1=son1()
s1.money()
s2=son2()
s2.money()
s1.important()
