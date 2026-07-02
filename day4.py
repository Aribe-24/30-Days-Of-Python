# Strings
# A string is a sequence of characters enclosed in quotes.
# Text is a string, and it can be represented using either single quotes (' ') or double quotes (" ").
letter = 'a'
print(letter)  # Output: a
print(len(letter))  # Output: 1

multiline_string = """My name is Joan a
Day 4
Strings
Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.nd I am an aspiring AI engineer. I am currently learning Python and I am excited to explore the world of programming."""
print(multiline_string) #Output: My name is Joan and I am an aspiring AI engineer. I am currently learning Python and I am excited to explore the world of programming.

#String Concatenation
# String concatenation is the process of combining two or more strings into a single string. In Python, you can concatenate strings using the + operator. Here's an example:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

#Escape sequences in Strings
# Escape sequences are special characters that are used to represent certain characters in a string. They are preceded by a backslash (\) and are used to represent characters that are difficult to include directly in a string. Here are some common escape sequences in Python:
# \n - Newline
# \t - Tab
# \\ - Backslash
# \' - Single quote
# \" - Double quote
# Here's an example of using escape sequences in a string:
text = "Hello,\n\tThis is a string with escape sequences.\nIt includes a newline, a tab, and a backslash: \\"
print(text)
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t4\t6')

#String formatting
# String formatting is the process of inserting values into a string. In Python, you can use the format() method or f-strings (formatted string literals) to format strings. Here's an example:
# %s = string
# %d = integer
# %f = float

# Using strings only
first_name = "John"
last_name = "Doe"
full_name = "My name is %s %s." % (first_name, last_name)
print(full_name)  # Output: My name is John Doe.

# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
area_string = "The area of a circle with radius %d is %.2f." % (radius, area)
print(area_string)  # Output: The area of a circle with radius 10 is 314.00.

#python libraries
#django, flask, numpy, matplotlib, pandas, seaborn, scikit-learn, tensorflow, keras, pytorch, opencv, nltk, spacy, beautifulsoup4, requests, scrapy, pillow, sqlalchemy, pytest, jupyter, streamlit

#New style string formatting(str)
first_name = "John"
last_name = "Doe"
full_name = "My name is {} {}.".format(first_name, last_name)
print(full_name)  # Output: My name is John Doe.

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))  # Output: 4 + 3 = 7

#Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
area_string = "The area of a circle with radius {} is {:.2f}.".format(radius, area)
print(area_string)  # Output: The area of a circle with radius 10 is 314.00.

#Strin interpolation/f-Strings
# f-strings (formatted string literals) are a way to embed expressions inside string literals,
a = 4
b = 3
print(f'{a} + {b} = {a + b}')  # Output: 4 + 3 = 7

#python strings as sequence of characters
# In Python, strings are sequences of characters. Each character in a string has an index, which represents its position in the string. The index starts at 0 for the first character,
language = 'Python'
a,b,c,d,e,f = language
print(a)  # Output: P
print(b)  # Output: y

#Accessing characters in strings by index
# You can access individual characters in a string using their index. The index starts at 0

language = 'Python'
first_letter = language[0]
print(first_letter)  # Output: P

#Slicing strings
# Slicing is a way to extract a portion of a string. You can use the slice notation to specify the start and end indices of the substring you want to extract. The syntax for slicing
language = 'Python'
first_three_letters = language[0:3]
print(first_three_letters)  # Output: Pyt

#REversing a string
# You can reverse a string by using slicing with a step of -1. Here's an example
language = 'Python'
reversed_language = language[::-1]
print(reversed_language)  # Output: nohtyP


#String methods
# Python provides a variety of built-in string methods that allow you to manipulate and analyze strings.
#capitalize() - Capitalizes the first character of the string.
text = "hello, world!"
capitalized_text = text.capitalize()

#count() - Counts the number of occurrences of a substring in the string.
text = "hello, world!"
count = text.count("o")  # Output: 2

#endswith() - Checks if the string ends with a specified suffix.
text = "hello, world!"
ends_with_exclamation = text.endswith("!")  # Output: True

#find() - Returns the index of the first occurrence of a substring in the string. Returns -1 if the substring is not found.
text = "hello, world!"
index_of_world = text.find("world")  # Output: 7

#rfind() - Returns the index of the last occurrence of a substring in the string. Returns -1 if the substring is not found.
text = "hello, world!"  
index_of_world = text.rfind("world")  # Output: 7

#format() - Formats the string using placeholders and values.
name = "John"       
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is John and I am 30 years old.



#Use the new line escape escape sequence to write the following

#Name: John Doe
#Age: 30
#Country: USA
#City: New York
name = "John Doe"
age = 30
country = "USA"
city = "New York"
info = f"Name: {name}\nAge: {age}\nCountry: {country}\nCity: {city}"
print(info)
print('name: John Doe\nAge: 30\nCountry: USA\nCity: New York')

print('name\tAge\tCountry\tCity')
print('John Doe\t30\tUSA\tNew York')

