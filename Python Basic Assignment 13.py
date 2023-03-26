#1. What advantages do Excel spreadsheets have over CSV spreadsheets?
# Excel spreadsheets have several advantages over CSV (Comma Separated Values) spreadsheets:
#
# Formatting: Excel allows you to format your data using a variety of formatting options, such as font size, color, and style, alignment, and cell borders. This makes it easier to read and understand your data, and can also help you highlight important information.
#
# Calculations: Excel allows you to perform calculations on your data using formulas and functions. You can use built-in functions like SUM, AVERAGE, and COUNT to calculate totals, averages, and counts, or create your own custom formulas to perform more complex calculations.
#
# Graphs and charts: Excel allows you to create graphs and charts to visualize your data. You can create bar charts, line charts, pie charts, and more, and customize them to display your data in the most meaningful way.
#
# Multiple sheets: Excel allows you to create multiple sheets within a single workbook, so you can organize your data by topic or category.
#
# Macros: Excel allows you to create macros to automate repetitive tasks or perform complex operations on your data. This can save you time and improve the accuracy of your work.
#
# While CSV spreadsheets are simple and easy to use, they lack many of the advanced features of Excel, and are best suited for simple, straightforward data sets that do not require formatting or complex calculations.

#2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
#To create a reader object using the csv module in Python, you pass a file object or a list of lines to csv.reader().
import csv

# Open a CSV file and create a reader object
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # Read each row in the CSV file
    for row in reader:
        print(row)
#In this example, we open a file called data.csv in read mode, and create a reader object using csv.reader(). We then loop through each row in the CSV file and print it to the console.

# To create a writer object using the csv module, you pass a file object and a list of fieldnames to csv.writer().
import csv

# Create a CSV file and write some data to it
with open('output.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write a header row to the CSV file
    writer.writeheader()

    # Write some data to the CSV file
    writer.writerow({'Name': 'Amal', 'Age': 25, 'Gender': 'F'})
    writer.writerow({'Name': 'Kumari', 'Age': 30, 'Gender': 'M'})

# In this example, we create a new file called output.csv in write mode, and create a writer object using csv.DictWriter().
# We pass the file object and a list of fieldnames (['Name', 'Age', 'Gender']) to the DictWriter constructor.
# We then write a header row to the CSV file using writer.writeheader(), and write some data to the CSV file using writer.writerow().

#3. What modes do File objects for reader and writer objects need to be opened in?

# For CSV reader objects, the associated file object needs to be opened in 'r' mode (read mode). This is because the CSV reader reads data from the file.
#
# For CSV writer objects, the associated file object needs to be opened in 'w' mode (write mode) or 'a' mode (append mode).
# This is because the CSV writer writes data to the file.
#
# When opening a file for CSV reading or writing, it's recommended to use the 'newline' argument with a blank value, '\'like so: newline=''.
# This is to ensure that the file is properly formatted with respect to line endings.

#4. What method takes a list argument and writes it to a CSV file?

# The writerow() method of a CSV writer object is used to write a single row of data to a CSV file.
# To write a list of rows to a CSV file, the writerows() method can be used.
# The writerows() method takes an iterable argument, such as a list of lists or a generator,
# where each element in the iterable represents a row of data to be written to the CSV file.

#5. What do the keyword arguments delimiter and line terminator do?

# The keyword argument delimiter is used in csv.writer() method to specify the character to be used as a field delimiter. By default, a comma (',') is used as the delimiter.
#
# The keyword argument lineterminator is used to specify the character to be used as a line terminator.
# By default, a new line (\n) is used as the line terminator. It is also used to specify the line terminator in the csv.reader() method.

#6. What function takes a string of JSON data and returns a Python data structure?

# The json.loads() function can be used to parse a JSON string and convert it into a Python data structure.
# The json module needs to be imported before using this function.

#7. What function takes a Python data structure and returns a string of JSON data?'
# The json.dumps() function takes a Python data structure and returns a string of JSON data.
# The dumps() function is used to encode Python objects into a JSON formatted string.
# It takes an object and returns a string.


