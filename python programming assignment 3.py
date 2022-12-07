#1 find out if a number is positive negative or zero
number = int(input("Enter number : "))
if number < 0 :
    print("The number is negative.")

elif number > 0 :
    print("The number is positive")

elif number == 0 :
    print("The number is zero")

else :
    print("Wrong Input")

#2 Check if a number is odd or even
number1 = int(input("Enter number1 : "))
if number1 % 2 == 0 :
    print("It is an even number")

else :
    print("This number is an odd number ")


#3 Write a python programme to check leap year
year = int(input("Enter Year : "))

if(year % 400 == 0) and (year % 100 == 0) :
    print("It's a leap year")
elif (year % 4 == 0) and (year % 100 != 0) :
    print("It's a leap year")
else :
    print(" not a leap year")

#4 Write a python programme to check prime number
number2 = int(input("Enter number2"))
if number2 > 1 :
    for i in range(2,number2):
        if(number2%i) == 0 :
            print( number2, "is not prime number")
            break
        else :
            print(number2, "is prime number")

#5 Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = int(input("Enter lower value "))
upper = int(input("Enter the upper value "))
for number in range(lower, upper +1) :
    if number>1 :
        for i in range(2,number):
            if (number%i) == 0 :
                break

        else :
            print(number)