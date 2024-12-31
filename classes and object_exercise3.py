class laptop:
    def __init__(self):
        self.price=0;
        self.ram="";
    def display(self):
        print("price:",self.price);
        print("ram:",self.ram);

hp=laptop()
dell=laptop()

hp.price=5000
hp.ram=8

dell.price=10000
dell.ram=16

hp.display()
dell.display()
