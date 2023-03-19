#1. Write a Python Program to Add Two Matrices?
def add_matrices(x,y):

    rows = len(x)
    cols = len(x[0])

    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return "Matrices do not have the same shape"

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(x[i][j] + y[i][j])
        result.append(row)

    return result

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
print(add_matrices(x,y))

#2. Write a Python Program to Multiply Two Matrices?
# define matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[14, 43, 32],
     [63, 10, 55],
     [11, 19, 98]]

# initialize the result matrix
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# iterate through rows of A
for i in range(len(A)):
    # iterate through columns of B
    for j in range(len(B[0])):
        # iterate through rows of B
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# print the result
for row in C:
    print(row)

#3. Write a Python Program to Transpose a Matrix?
rows = int(input("Enter the number of rows: "))
cols = int(input("ENter number of columns: "))

#initialize the matrix
matrix = []
for i in range(rows):
    row=[]
    for j in range(cols):
        element =int(input(f"Enter the elememt for row {i+1} column{j+1}: "))
        row.append(element)
    matrix.append(row)

#transpose the matrix
transpose = []
for j in range(cols):
    row =[]
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

# print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

#print the transposed matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)

#4. Write a Python Program to Sort Words in Alphabetic Order?
sentence = input("Enter a string: ")

words = sentence.split()

sorted_words = sorted(words)

print("Sorted words: ")
for word in sorted_words:
    print(word)

#5. Write a Python Program to Remove Punctuation From a String?
import string

input_str = "Hello!!!I am A. How are you feeling today?"

punctuations = string.punctuation

no_punctuations = ''
for char in input_str:
    if char not in punctuations:
        no_punctuations +=char

print("Original Strint: ",input_str)
print("String without Punctuations: ", no_punctuations)