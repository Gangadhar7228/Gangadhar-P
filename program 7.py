def factorial (n):
    if n<0:
        return None
    result=1
    for i in range(2,n+1):
        result*=i
    return result
    
def simple_intrest(principle,time,rate=5.0):
    return(principle*time*rate)/100

square=lambda x:x*x

n=int(input("enter a number for factorial:"))
fact=factorial(n)

if fact is None:
    print("factorial is not defined for negative numbers:")
else:
    print("factorial=",fact)
    
p=float(input("enter a principle amount="))
t=float(input("enter a time in year:"))
print("simple intrest(default rate 5%)=",simple_intrest(p,t))

x=float(input("enter a number to find its square:"))
print("square=",square(x))


        