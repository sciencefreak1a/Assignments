#1. Write a Python Program to Find the Factorial of a Number?
number = int(input("Enter Number : "))
factorial = 1
if number > 0 :
    for i in range(1, number+1) :
        factorial = factorial * i
    print(" The factorial of",number,"is",factorial)
else :
    print("enter a value greater than zero")

#2. Write a Python Program to Display the multiplication Table?
num = int(input("Enter number for multiplication table : "))
i = 1
while i <=10 :
    print(num,'x',i,'=',num*i)
    i += 1

#3. Write a Python Program to Print the Fibonacci sequence?
Number = int(input("\nPlease Enter the Number : "))
First = 0
Second = 1
for Num in range(0, Number):
    if (Num <= 1):
        Next = Num
    else:
        Next = First + Second
        First = Second
        Second = Next
    print(Next)

#4 Write a Python Program to Check Armstrong Number?
arm_num = int(input("Enter a number"))
sum = 0
order = len(str(arm_num))
copy_arm_num = arm_num

while (arm_num >0):

    digit = arm_num % 10
    sum += digit ** order
    arm_num = arm_num // 10

if (sum == copy_arm_num) :
    print("The entered number is an armstrong number")
else :
    print("THe entered number is not an armstrong number")

#5 Write a Python Program to Find Armstrong Number in an Interval?
lower_value = int(input("Enter lower value"))
upper_value = int(input("Enter upper value < 1000"))

for i in range (lower_value, upper_value + 1) :
    sum1 = 0
    arm_num1 = i

    while arm_num1>0:
        digit = arm_num1%10
        sum1 += digit ** 3
        arm_num1 = arm_num1 // 10
        if i == sum1:
             print("Armstrong number in the given range is", i)

#6. Write a Python Program to Find the Sum of Natural Numbers?
numbers = int(input("enter number"))
total = 0
for value in range (1, numbers+1) :
    total = total + value

print("The sum of natural numbers is ", total)
