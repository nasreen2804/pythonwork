salary=int (input("enter your salary"))
age=int (input("enter your age"))
if(salary>=20000 or Age<=25):
    loan=int (input("Loan:"))
    if(loan>=50000):
        print("maximum loan amount is 50000")
    else:
        print("you are eligible")
else:
    print("not eligible")
