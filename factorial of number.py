def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("entrer a number:"))
if num < 0:
    print("factorial is not defined for negativr numbers.")
elif num==0:
      print(f"{num}!= 1")
else:
    fact = factorial(num)
    print(f"{num}!={fact}")
    
