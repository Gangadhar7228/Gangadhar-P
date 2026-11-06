while True:
  print("\n---MENU---")
  print("1.check even or odd")
  print("2.largest of three numbers")
  print("3.multiplication table")
  print("4.prime numbers in range")
  print("5.exit")
  
  choice=input("enter your choice=")

  if choice=="1":
    n=int(input("enter a number="))
    print(n,"is even"if n%2==0 else"is odd")
  
  elif choice=="2":
    a=float(input("enter a first number="))
    b=float(input("enter a second number="))
    c=float(input("enter a third number="))
    print("largest number=",max(a,b,c))
   
  elif choice=="3":
    n=int(input("enter a number="))
    for i in range (1,11):
        print(f"{n}x{i}={n*i}")
      
  elif choice=="4":
     start=int(input("enter a start of range="))
     end=(input("enter end of range="))
     print("prime numbers:",end=" ")
     for n in range(max(2,start),end+1):
      is_prime=True
     for i in range(2,int(n**0.5)+1):
      if n%i-0:
        is_prime=False
        break
      if is_prime:
        print(n,end=" ")
      print()
      
  elif choice=="5":
   print("exiting program....")
   break
  
else:
  print("invalid choice try again:") 