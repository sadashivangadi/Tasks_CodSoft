#calculator 
print("---Simple Calculator----\n")

n1=int(input("Enter the First Number \n"))
n2=int(input("Enter the Second Number\n"))

print("Enter choose operation +,-,/,*,%\n")
op=input("Enter the operation\n")

if op == '+':
    res=n1+n2

elif op=='-':
    res=n1-n2

elif op=='*':
    res=n1*n2

elif op=='/':
    if n1==0:
        res="Error ! can't divided by zero"
    else:
         res=n1*n2

elif op=='%':
    if n2==0:
        res="Error ! can't divided by zero"
    else:
         res=n1%n2

else:
    res="Invalid operation"

print("result of two numbers is=",res)