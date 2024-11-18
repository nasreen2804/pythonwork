a=int (input("Mark1:"))
b=int (input("Mark2:"))
c=int (input("Mark3:"))
d=int (input("Mark4:"))
e=int (input("Mark5:"))
f=a+b+c+d+e
print(f)
average=f/5
print(average)
if(average<=35):
    print("additional class is required")
else:
    print("you are good to go")
