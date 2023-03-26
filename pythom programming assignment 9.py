#1. Write a Python program to check if the given number is a Disarium Number?
#A Disarium number is a number where the sum of its digits raised to the power of their respective positions is equal to the number itself.
num = int(input("Enter a number: "))
sum2 = 0
temp = num
order = len(str(num))

while temp > 0 :
    digit = temp % 10
    sum2 = sum2 + digit**order
    order = order-1
    temp//=10

if num == sum2:
    print(num, "is a Disarium number")
else:
    print(num,"is not a Disarium number")

#2 Write a Python program to print all disarium numbers between 1 to 100?
num = 1
while num <= 100:
    order = len(str(num))
    temp = num
    sum1 = 0

    while temp>0:
        digit = temp % 10
        sum1 = sum1 + digit**order
        order = order-1
        temp //= 10

    if num == sum1:
        print(num)
    num = num+1

#3 Write a Python program to check if the given number is Happy Number?
def isHappyNumber(num):
    rem = sum = 0;

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10;
        sum = sum + (rem * rem);
        num = num // 10;
    return sum;


num = int(input("Enter a number : "))
result = num;

while (result != 1 and result != 4):
    result = isHappyNumber(result);

# Happy number always ends with 1
if (result == 1):
    print(str(num) + " is a happy number");
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif (result == 4):
    print(str(num) + " is not a happy number");

#4. Write a Python program to print all happy numbers between 1 and 100?
def isHappyNumber(num):
    """
    This function takes a number as input and returns the sum of squares of its digits.
    """
    sum = 0
    while (num > 0):
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


# Print all happy numbers between 1 and 100
print("Happy numbers between 1 and 100:")
for i in range(1, 101):
    result = i
    while (result != 1 and result != 4):
        result = isHappyNumber(result)

    # Happy number always ends with 1
    if (result == 1):
        print(str(i) + " is a happy number")

    # Unhappy number ends in a cycle of repeating numbers which contain 4
    elif (result == 4):
        print(str(i) + " is not a happy number")

#5 Write a Python program to determine whether the given number is a Harshad Number?
def isHarshadNumber(num):
    """
    This function takes a number as input and returns True if it is a Harshad number,
    otherwise returns False.
    """
    # Calculate the sum of digits
    digit_sum = 0
    n = num
    while n > 0:
        digit_sum += n % 10
        n //= 10

    # Check if the number is divisible by the sum of its digits
    if num % digit_sum == 0:
        return True
    else:
        return False



num = int(input("Enter Number: "))
if isHarshadNumber(num):
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")

#6. Write a Python program to print all pronic numbers between 1 and 100?
for i in range(1,101):
    if i == 1 :
        continue
    for j in range(1,i):
        if i == j*(j+1):
            print(i)
            break
