n1= int(input("enter the number1: "));
n2= int(input("enter the number2: "));
oper= input("enter the operator to be perform: ");
if(oper=='+'):
    a=n1+n2
    print(a)
elif(oper=='-'):
    b=n1-n2
    print(b)
elif(oper=='*'):
    c=n1*n2
    print(c)
elif(oper=='/'):
    d=n1/n2
    print(d)
elif(oper=='%'):
    e=n1%n2
    print(e)
elif(oper=='**'):
    f=n1**n2
    print(f)
else:
    print("INVALID OPERATOR")