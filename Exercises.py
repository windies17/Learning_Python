# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

name = input("What is your name?")
age = input("What is your age?")
age = int(age)

print(f"Hello {name} on your next birthday your going to {age}")

# Write a function that takes a string gets rid of hyphens and determines if the lenth is over 15 character.


def report_long_words(words):
    long_words = []
    for word in words:
        if len(word) > 10 and "-" not in word:
            if len(word) > 15:
                word = word[:15] + "..."
                long_words.append(word)

    if long_words:
        report = "This is a really long word" + ",".join(long_words)
    else:
        report = "This is a really long word"

    return report


print(report_long_words(["Hello", ]))


def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False
    pass


print(large_power(45, 4))
print(large_power(3, 4))

#Strip a sting

word  = "Hello there "
