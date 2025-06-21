def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
def exp(x,y):
    return x**y

def rem(x,y):
    return x%y

print("Select operation which operation you want to perform : ")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
print("exponential")
print("Remainder")

choice=input("Choose from(1/2/3/4/5/6) :")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))


if choice=='1':
    print('result : ', add(num1,num2))

elif choice=='2':
    print('result : ', sub(num1,num2))
elif choice=='3':
    print('result : ', mul(num1,num2))
elif choice=='4':
    print('result : ', div(num1,num2))
elif choice=='5':
    print('result : ', exp(num1,num2))
elif choice=='6':
    print('result : ', rem(num1,num2))
else:
    print("Invalid choice selection")
