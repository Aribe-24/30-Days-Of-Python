#boolean
# A boolean is a data type that can have one of two values: True or False. It is often used in conditional statements and logical operations. In Python, the boolean values are represented by the keywords True and False (with capital T and F).
print(type(True)) # This prints the data type of True, which is <class 'bool'>
print(type(False)) # This prints the data type of False, which is <class 'bool'>
print(True)
print(False)

# Operators in Python:
# Operators are special symbols that perform specific operations on one or more operands. 
#Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left. For example:
x = 5 # This assigns the value of 5 to the variable x
#some of them include:
# 1. = : Assigns a value to a variable.
# 2. += : Adds a value to a variable and assigns the result to that variable
x += 3 # This adds 3 to the value of x and assigns the result to x. Now x is 8
# 3. -= : Subtracts a value from a variable and assigns the result to that variable.
x -= 2 # This subtracts 2 from the value of x and assigns the result to x. Now x is 6
# 4. *= : Multiplies a variable by a value and assigns the result to that variable.
x *= 4 # This multiplies the value of x by 4 and assigns the result to x. Now x is 24
# 5. /= : Divides a variable by a value and assigns the result to that variable.
x /= 3 # This divides the value of x by 3 and assigns the result to x. Now x is 8.0
# 6. %= : Calculates the modulus of a variable and a value and assigns the result to that variable.
x %= 5 # This calculates the modulus of x and 5 and assigns the result to x. Now x is 3.0
# 7. **= : Raises a variable to the power of a value and assigns the result to that variable.
x **= 2 # This raises the value of x to the power of 2 and assigns the result to x. Now x is 9.0
# 8. //= :  Calculates the floor division of a variable and a value and assigns the result to that variable.
x //= 2 # This calculates the floor division of x and 2 and assigns the result to x. Now x is 4.0


#Arithmetic operators are used to perform mathematical operations on numeric values. The most common arithmetic operators are:
#Examples of arithmetic operators in Python include:
#Addition
#Subtraction
#Multiplication
#Division
#Modulus
#Exponentiation

#Comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison. The most common comparison operators are:
#Examples of comparison operators in Python include:
#Equal to (==)
#Not equal to (!=)
#Greater than (>)
#Less than (<)
#Greater than or equal to (>=)
#Less than or equal to (<=)     
print(2 < 3) # This prints True because 2 is less than 3
print(len("Hello") == 5) # This prints True because the length of "Hello" is equal to 5
print(len('milk") != len("bread")) # This prints True because the length of "milk" is not equal to the length of "bread"'))
print(len("apple") > len("banana")) # This prints False because the length of "apple" is not greater than the length of "banana"

#comparing something gives either True or false. True is represented by 1 and False is represented by 0. In Python, you can use the int() function to convert a boolean value to an integer. For example:
print("True == TRue: ", int(True == True)) # This prints 1 because True is equal to True

#Logical operators are used to combine multiple boolean expressions and return a boolean value based on the logical relationship between them. The most common logical operators are:
# AND (&) #Returns True if both expressions are True, otherwise returns False
x < 5 and x > 2 # This returns True because both expressions are True
# OR (|) # Returns True if one of the statements is true, otherwise returns False
x < 5 or x > 2 # This returns True because one of the statements is
# NOT (!) # Returns True if the expression is False, and returns False if the expression is True
not(x < 5) # This returns False because the expression x < 5 is True






