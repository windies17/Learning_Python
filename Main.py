#Dictionary is a collection of {key:value} pairs which in curly braces, Dictionaries are ordered and chaneable have no duplicates.

#Things to remember with a list is always seperate the key pairs with a comma



 #This is really useful as it shows methods are available.

capitals = {
   "Germany": "Berlin",
   "Scotland": "Edinburgh",
   "England": "London",
    "Wales": "Cardiff",
    "Northern Ireland": "Belfast",
    "ROI": "Dublin"} #Remember the comma and quotations and the colon is outside the quotations

print(help(capitals))

#length = capitals.__len__()
#print(length)

#To get the key of the dictionary you would use method .get but you need to print and after the print comes a bracket.

#print(capitals.get("Scotland"))

'''
This code is checking whether the key "ROI" is present in the capitals dictionary and printing a message accordingly. Let's break it down step by step:

if capitals.get("ROI") is None:
    print("This is not in the list")
else:
    print("This is in the list")
Dictionary Lookup:
capitals.get("ROI")
This part retrieves the value associated with the key "ROI" from the capitals dictionary. If the key is present, it returns the associated value; otherwise, it returns None.
Check for Presence:
python
Copy code
if capitals.get("ROI") is None:
The is None part checks if the result of capitals.get("ROI") is None. If it is, that means the key "ROI" is not in the dictionary.
Print the Result:
    print("This is not in the list")
else:
    print("This is in the list")
If the key "ROI" is not in the dictionary (i.e., capitals.get("ROI") returns None), it prints "This is not in the list". Otherwise, if the key is present, it prints "This is in the list".
'''

#if capitals.get("Hungary") is None:
    #print("This is not in the list")
#else:
    #print("This is in the list")


#capitals.update({"China":"Beijing"})
#This updates a new key value pair eg China and Beijing

#To remove a can use pop
#print(capitals.pop("China"))
#To remove the last include key pair you can use pop item
#print(capitals.popitem())

#TO ITERATE OVER THE KEYS YOU CAN USE A FOR LOOP OR A KEYS METHODS

#keys = capitals.keys()
#print(keys)

#for keys in capitals.keys():
    #print(keys)

#values = capitals.values()
#print(values)

#for values in capitals.values():
  #print(values)

#items = capitals.items()
#print(items)

#for key, value in capitals.items():
    #print(f'{key}: {value}')

#capitals.copy()

#print(capitals)

names = {
    "Jon":30,
    "Dianne":42,
    "Craig": 44,
    "Caris": 26,
        }

#print(help(names))

if names.get("Jack") is not None:
    print("This is in the list")
else:
    print("This is not in the list")

print(names.get("Dianne"))

for name in names.values():
    print(names)