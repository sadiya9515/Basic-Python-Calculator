print("===Simple Calculator===")

num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

print("\nChoose Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=input("choose operation(1/2/3/4):")

if choice=="1":
    print("result=",num1+num2)
elif choice=="2":
    print("result=",num1-num2)
elif choice=="3":
    print("result=",num1*num2)
elif choice=="4":
    print("result=",num1/num2)
else:
    print("Error!Division by zero is not allowed.")