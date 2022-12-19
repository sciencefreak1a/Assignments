#1. Write a Python Program to Find LCM?
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

lcm = num1 if (num1>num2) else num2

while(True) :
    if(lcm % num1 == 0 ) and (lcm % num2 == 0) :
        print("The L.C.M of", num1, "and", num2, "is", lcm)
        break
    lcm+=1

#2 Write a Python Program to Find HCF?
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

def compute_hcf(x,y) :
    if x > y :
        smaller = y
    else :
        smaller = x
    for i in range(1,smaller+1):
        if((x % i ==0) and (y % i == 0)):
            hcf = i
    return hcf
print("The H.C.F is", compute_hcf(num1,num2))

#3 Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
decimal = int(input("Enter decimal value "))

print("The decimal value of",decimal,"is : ")
print(bin(decimal),"in binary.")
print(oct(decimal),"in octal.")
print(hex(decimal), "in hexadecimal.")

#4 Write a Python Program To Find ASCII value of a character?

char = (input("Enter a character: "))
print("Thr ASCII value of the given character is : ", ord(char))

#5 Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ("1,2,3,4") :
        num1a = float(input("Enter first number: "))
        num2a = float(input("Enter second number: "))

        if choice == "1" :
            print(num1a, "+", num2a, "=", add(num1a,num2a))

        elif choice == "2" :
            print(num1a, "-", num2a, "=", subtract(num1a,num2a))

        elif choice == "3":
            print(num1a, "*", num2a,"=",multiply(num1a,num2a))

        elif choice == "4":
            print(num1a,"/",num2a,"=",divide(num1a,num2a))

        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else :
        print("Invalid input")