a= int(input("enter number 1: "))
b= int(input("enter number 2: "))
c= int(input("enter number 3: "))
if a>=b and a>=c:
    print("greatest: ",a )
elif b>=a and b>=c:
    print("greatest: ",b )
else:
    print("greatest: ",c )
