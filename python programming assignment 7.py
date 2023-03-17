#1. Write a Python Program to find sum of array?
import array as arr
a = arr.array('i',[1,2,3,4,5])

sum = sum(a)

print("The sum of all elements in the array is :",sum)

#2. Write a Python Program to find largest element in an array?
def largest(b,n):
    max=b[0]

    for i in range(1,n):
        if b[i]>max:
            max = b[i]
    return max

b = arr.array('i',[21,22,34,456,32,4565])
n = len(b)
ans = largest(b,n)
print("The largest number in the array is ", ans)

#3. Write a Python Program for array rotation?
def rotateArray(a,d):
   temp = []
   n = len(a)
   for i in range(d,n):
       temp.append(a[i])
   i = 0
   for i in range(0,d):
       temp.append(a[i])
   a = temp.copy()
   return a

arr1 = [1,2,3,4,5,556,665,4433,23]
print("Rotated Array is ")
print(rotateArray(arr1,2))

#4. Write a Python Program to Split the array and add the first part to the end?
def rotateArray1(a,d):
    n = len(a)
    a[:] = a[d:n]+a[0:d]
    return a
arr = [3,4,5,6,6,7,8,45,6,6,345,33]

print("Rotated Array is ")
print(rotateArray1(arr,2))

#5. Write a Python Program to check if given array is Monotonic?
def is_montonic(arr):
    increasing = decreasing = True

    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            increasing = False
        if arr[i] > arr[i-1]:
            decreasing = False

    if increasing :
        print("Array is strictly increasing")
    elif decreasing:
        print("Array is strictly decreasing")
    else :
        print("it is a non monotonic array")

        return increasing or decreasing

arr1 =  [1,2,3,4,5,6]
arr2 = [1,2,3,4]
arr3 = [4,4,3,1,]
arr4 = [5,15,20,10]

is_montonic(arr1)
is_montonic(arr2)
is_montonic(arr3)
is_montonic(arr4)


