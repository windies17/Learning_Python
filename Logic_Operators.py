# In Python there are logic operators such as

# OR NOT and AND (excuse the pun).   Back in Physics they were rudimentary reffered to as gates

# And gates or logic operators have to take a true and a false for example

#   ____________________
#   |2 input AND gate  |
#   |__________________|
#   | A     | B | AB   |
#   | 0     | 1 | 0    |
#   | 1     | 0 | 0    |
#   | 0     | 0 | 0    |
#   | 1     | 1 | 1    |


# An OR gate takes two inputs if one is false and one is true the outcome is true.
# If two are false the output is false

#   |2 input OR gate   |
#   |__________________|
#   | A     | B | AB   |
#   | 0     | 1 | 1    |
#   | 1     | 0 | 1    |
#   | 0     | 0 | 0    |
#   | 1     | 1 | 1    |


# Example 1


def this_is_my_string(mystr):
    first_letter = mystr[0]  # First letter is the variable of mystr first letter
    if first_letter == "G" or first_letter == "X":
        print("True")  # You do not  need the parenthases after return
    else:
        print("False")


this_is_my_string("Hello there")  # The output will be False as the first letter is "H"
this_is_my_string(
    "The man is away to Spain"
)  # The output will be False as the first letter is "T"
this_is_my_string(
    "Gengis Khan was the man"
)  # The output will be true as the first letter is "G"
