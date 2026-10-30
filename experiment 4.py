num1=float(input("enter the first number"))
num2=float(input("enter the second number"))

print("addition=",num1+num2)
print("floor division=",num1*num2)

if num2!=0:
   print("division=",num1/num2)
   print("floor division=",num1//num2)
   print("modulus=",num1%num2)
else:
    print("division,floor division and modulus are undefined for zero divisior.")
    print("exponentiation=",num1**num2)