class laptop:
    price="";
    processor="";
    ram="";
    def HP(self):
        print("HP LAPTOP");
    def DELL(self):
        print("DELL LAPTOP");
    def LENOVO(self):
        print("LENOVO LAPTOP");

HP=laptop();
DELL=laptop();
LENOVO=laptop();

HP.price="10000"
HP.processor="all function";
HP.ram="5";

DELL.price="10000"
DELL.processor="all function";
DELL.ram="5";

LENOVO.price="10000"
LENOVO.processor="all function";
LENOVO.ram="5";

print(HP.price);
print(HP.processor);
print(HP.ram);

print(DELL.price);
print(DELL.processor);
print(DELL.ram);

print(LENOVO.price);
print(LENOVO.processor);
print(LENOVO.ram);

HP.HP()
DELL.DELL()
LENOVO.LENOVO()
