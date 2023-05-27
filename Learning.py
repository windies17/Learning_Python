# In order to understand how to do something you need to practice

# To practice I am going to write a small program

# This block of code below starts with def
# The function is called mynumber
# It is followed by a pararentheses and inside the pararenthisis is a paramter
# The code is followed by a colon
# Once you press return it indents it
# return is a keyword

def mynumber(num):
    return num


print("Hell World the number in my number is:")
print(mynumber(17))

# To run another code you can do many things

# The output willm return the number and add 1


def runnum(num):
    return num + 1


print('The return number is:')
# Youd o not need exclamation marks as you are printing the functions
print(runnum(5))


#I am going to return a number and add 2
def my_num(num):
    return num + 2

print('The new number is:')
print (my_num(9))

def multiply_numbers(num_a,num_b):
    return num_a * num_b

print ("The result of Num A * Num B is :")
print (multiply_numbers(6,9))

def add_one(num):
  return num + 1

# You may need to widen the panel or zoom out to see the table:

# | Code           | What is it?                                        |
# | -------------- | -------------------------------------------------- |
# | def            | `def` is a keyword that defines a new function     |
# | add_one        | `add_one` is the function name                     |
# | (num)          | `(num)` is the parameter list                      |
# | num            | `num` is a parameter                               |
# | :              | The `:` symbol indicates the body should start now |
# | return num + 1 | `return num + 1` is a statement                    |
# | num + 1        | `num + 1` is an expression                         |
# | num            | `num` here is a variable                           |
# | +              | `+` is an operator                                 |
# | 1              | `1` is a literal number                            |

# Don't worry about remembering all of that table, but pay
# attention now to three items: operators, statements, and
# expressions. We're going to look at all three next.

# Strings

# after the print char needs to go in brackets ()

my_word = ["This is a brilliant Learning opportunity"]

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# If you go into the REPL >>> by typing python3 you can interactively go into a file by typing -i for example in the terminal......... python3 -i Learning.py


my_number = 17

print(f"Today my favourite number is {my_number}")

# here we are going to input the word

name = input ("What is your name ")

print (f"Hello and welcome to the party {name}")


