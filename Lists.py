#In python you can lists
#lists can be iterated like strings like so

the_new_list = ["John","James","Jack"]

# the_new_list.append["Jim"] # I put square brackets when it should have been parentheses ()

the_new_list.append("Jim")

print(the_new_list)

my_list = ["a", "b", "c"]
my_copy = my_list.copy()
my_copy.append("d")
print(my_list) # my_list is still ["a", "b", "c"]
print(my_copy) # my_copy is now   ["a", "b", "c", "d"]

a = 10
b = 24
print(a + b)

def count_digit_4(string):
    count = 0
    for digit in string:
        if digit == '4':
            count += 1
    return count

string = "283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796"

digit_4_count = count_digit_4(string)
print("The number 4 appears", digit_4_count, "times in the given string.")
