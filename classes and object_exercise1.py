class goa:
    name=""
    drink=""
    def party(self):
        print("Let party");
    def beach(self):
        print("enjoying the beach")

ramesh=goa()
suresh = goa()

ramesh.name="Ramesh";
ramesh.drink="yes";
suresh.name="Suresh";
suresh.drink="No";


print("name:",ramesh.name)
print("drink:",ramesh.drink)
print("name:",suresh.name)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()
