class grandpa():
    def phone(self):
        print("grandpa phone");

class dad(grandpa):
    def money(self):
        print("dads money");

class son(dad):
    pass

s1=son()
s1.phone();
