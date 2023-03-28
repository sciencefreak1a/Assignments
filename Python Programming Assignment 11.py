#1. Write a Python program to find words which are greater than given length k?
sentence = input("Enter a sentence: ")
k = int(input("Enter a value for k: "))

words = sentence.split()
for i in words:
    if len(i)>k:
        print(i)

#2.Write a Python program for removing i-th character from a string?
string = input("Enter a string: ")
i = int(input("Enter an index i to remove: "))

new_string = string[:i] + string[i+1:]

print("New string after removing i-th character:", new_string)

#3. Write a Python program to split and join a string?
string = input("Enter a string: ")

# Split the string into words using whitespace as the separator
words = string.split()

# Join the words back together using a hyphen as the separator
new_string = "-".join(words)

print("New string after splitting and joining:", new_string)

#4. Write a Python to check if a given string is binary string or not?
string = input("Enter a string: ")

# Set of valid binary digits
valid = {'0', '1'}

# Check if all characters in the string are valid binary digits
if set(string) == valid or set(string) == {'0'} or set(string) == {'1'}:
    print("The input string is a binary string.")
else:
    print("The input string is not a binary string.")

#5. Write a Python program to find uncommon words from two Strings?
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

words1 = string1.split()
words2 = string2.split()

unique_words = set(words1+words2)

uncommon = []

for i in unique_words:
    if (i in words1) != (i in words2):
        uncommon.append(i)
print("The uncommon words are : ",uncommon)

#6. Write a Python to find all duplicate characters in string?
string = input("ENter a string : ")

char_counts = {}

for i in string :
    char_counts[i] = char_counts.get(i,0)+1

duplicate_char = []

for i, count in char_counts.items():
    if count>1:
        duplicate_char.append(i)
print("The duplicate characters are : ",duplicate_char)

#5. Write a Python Program to check if a string contains any special character?
import string

def contains_spl_char(s):
    spl_char = set(string.punctuation)
    for i in s :
        if i in spl_char:
            return True
    return False

s = "Hello Everyone! I'm doing good!"
if contains_spl_char(s):
    print("String contains special characters")
else :
    print("String doesn't contain special characters")