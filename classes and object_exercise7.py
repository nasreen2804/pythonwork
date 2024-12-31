class teacher:
    def __init__(self,name,register):
        self.name=name;
        self.register=register;

    def display(self):
        print("name:",self.name);
        print("register:",self.register);

t1=teacher("nasreen","1")
t2=teacher("riyaz","2")



t1.display()
t2.display()
