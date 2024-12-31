class student:
    def __init__(self):
        self.name="";
        self.register=0;

    def display(self):
        print("name:",self.name);
        print("register:",self.register);

S1=student()
S2=student()

S1.name="nasreen";
S1.register=1;

S2.name="Riyaz";
S2.register=2;

S1.display()
S2.display()
    
