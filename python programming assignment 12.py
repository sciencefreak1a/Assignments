#1. Write a Python program to Extract Unique values dictionary values?

sample_dict = {'a':1, 'b':2,'c':3, 'd':1,'e':2}

unique_values = {value for value in sample_dict.values()}

print(unique_values)

#2. Write a Python program to find the sum of all items in a dictionary?
sample_dict = {'a':20,'b':30, 'c':40, 'd':50}

sum = sum(sample_dict.values())

print(sum)

#3. Write a Python program to Merging two Dictionaries?

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged dictionary:", merged_dict)

#4. Write a Python program to convert key-values list to flat dictionary?
l = [('a',2),('b',3),('c',4)]

dict = {key:value for key, value in l}

print(dict)

#5. Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict
od = OrderedDict([('a',10), ('b',20),('c',30)])

od.update({'d':40})

od.move_to_end('d', last = False)

print("Modified OrderedDict: ", od)

#6. Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict

def check_order(input_str, pattern):
    char_dict = OrderedDict.fromkeys(input_str)

    index = 0

    for key in char_dict :
        if key == pattern[index]:
            index += 1
        if index -- len(pattern):
            return True
    return False

input_str = 'hello world'
pattern = 'llo'
if check_order(input_str, pattern):
    print("The pattern {} appears in the string {} in the same order.".format(pattern, input_str))
else:
    print("The pattern {} does not appear in the string {} in the same order.".format(pattern, input_str))

#7. Write a Python program to sort Python Dictionaries by Key or Value?
my_dict = {'apple': 4, 'banana': 2, 'orange': 1, 'pear': 3}

sorted_dict_by_key = {k: v for k, v in sorted(my_dict.items())}
print("Sorted by Key:", sorted_dict_by_key)

sorted_dict_by_value = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print("Sorted by Value:", sorted_dict_by_value)


