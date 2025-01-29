class animal():
    def sound(self):
        print("animals makes sound");

class dog(animal):
    def sound(self):
        print("dogs barks");

class birds(animal):
    def sound(self):
        print("birds sings");

b1=birds()
b1.sound()
