#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fibonacci(n):
    if(n<=1):
        return n

    else :
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the number of terms : "))

print("Fibonacci sequence: ")
for i in range(n) :
    print(fibonacci(i))

#2. Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(n1):
    if (n1<=1):
        return n1

    else:
        return(n1 * factorial(n1-1))

n1 = int(input("Enter number"))

print("Factorial is : ")
print(factorial(n1))

#3. Write a Python Program to calculate your Body Mass Index?

def bodymassindex(height, weight):
    return round((weight/height**2))

h = float(input("Enter your height in meters : "))
w = float(input("Enter your weight in kgs"))

print("Welcome to the BMI calculator")
bmi = bodymassindex(h,w)
print("Your BMI is : ", bmi)

if bmi <= 18.5 :
    print("You are underweight")
elif bmi >18.5 and bmi <= 24.9 :
    print("YOur weight is normal")
elif bmi >25 and bmi <=29.9 :
    print("You are overweight")
else :
    print("You are obese")

#4  Write a Python Program to calculate the natural logarithm of any number?
import math
num = int(input("Enter number to find the log value: "))

ans = math.log(num)

print("The log of",num,"is",ans)

#5 Write a Python Program for cube sum of first n natural numbers?3


num1 = int(input("Enter number : "))
s = 0

for i in range(1,(num1+1)):
    s = s+pow(i,3)
print(s)
