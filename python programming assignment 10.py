#1. Write a Python program to find sum of elements in list?
l1 =[1,2,3,4,5,6]
sum = 0

for i in l1:
    sum = sum+i
print(sum)

#2. Write a Python program to Multiply all numbers in the list?
l2 = [1,2,3,4,5]
mul = 1
for j in l2 :
    mul = mul*j
print(mul)

#3. Write a Python program to find smallest number in a list?
l3 = [8, 7, 1, 9, 4]
smallest = l3[0]
for i in l3:
    if i < smallest:
        smallest = i
print(smallest)

#4. Write a Python program to find largest number in a list?
largest = l3[0]
for i in l3:
    if i > largest:
        largest = i
print(largest)

#5. Write a Python program to find second largest number in a list?
max1= max(l3)
l3.remove(max1)
sec_max = max(l3)
print(sec_max)

#6. Write a Python program to find N largest elements from a list?
import heapq

def n_largest_element(l4,n):
    return heapq.nlargest(n,l4
                          )
l4 = [123,32,444,543,6546,4564,233,24422,653,23432]
n = 3

print(n_largest_element(l4,n))

#7. Write a Python program to print even numbers in a list?
l5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

for i in l5:
    if i % 2 == 0:
        print(i)

#8. Write a Python program to print odd numbers in a List?
for i in l5:
    if i % 2 != 0:
        print(i)

#9. Write a Python program to Remove empty List from List?
l6 = [1, [], 3, [], 5, [], 7]
new_list = [x for x in l6 if x != []]
print(new_list)

#10. Write a Python program to Cloning or Copying a list?
new_list = l6[:]
print(new_list)

#11. Write a Python program to Count occurrences of an element in a list?
l7 = [1,1,1,2,2,2,3,3,3,4,5,6,7,1,1,1]
count = l7.count(1)
print(count)