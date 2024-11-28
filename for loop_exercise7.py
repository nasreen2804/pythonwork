a=[]
for i in range(5):
    num=int (input("enter number"+str(i+1)))
    a.append(num)
print(a)
    
sum=0
for i in a:
    sum=sum+i;
    average=sum/2;
print(sum)
print(average)
