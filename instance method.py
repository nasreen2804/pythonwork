class laptop():
    chargertype="type-c";
    def __init__(self,brand):
        self.brand=brand;
        self.price=0;
    def setprice(self,price):
        self.price=price;
    def getprice(self):
        print("brand:",self.brand);
        print("price:",self.price);
        print("charger:",self.chargertype);

hp=laptop("hp")
hp.setprice(20000)
hp.getprice()
    
