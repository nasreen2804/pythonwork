class a():
    def __init__(self):
        print("A")

class b():
    def __init__(self):
        super().__init__()
        print("b")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")

obj3=c()
