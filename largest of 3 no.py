n1=int(input("enter number 1 :"))
n2=int(input("enter number 2 :"))
n3=int(input("enter number 3 :"))
if n1>n2 and n1>n3:
    print(f"largest no: is {n1}")
elif n2>n1 and n2>n3:
    print(f"larges no:  is {n2}")
else:
    print(f"largest no: is  {n3}")
