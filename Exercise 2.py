def factorial(n):
    
    factorial = 1
    for i in range(n):
        factorial*=i+1


    return factorial


print(factorial(5))

def RecursionChallenge(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * RecursionChallenge(num - 1)
    
print (RecursionChallenge(6))