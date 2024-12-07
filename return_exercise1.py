s_username="nasreen"
s_password="28"

u_name= input("enter username");
u_password= input("enter password");

def validate():
    if(s_username==u_name and s_password==u_password):
        return "correct"
    else:
        return "wrong"

a=validate();
print(a);
