# Number 1

def smallest(numbers):
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min

lst1 = [232,4356,123,6]

print(smallest(lst1))


# Number 2

def largest(numbers2):
    max = numbers2[0]
    for x in numbers2:
        if x > max:
            max = x
    return max

lst2 = [12312, 234234, 1231, 1234]

print(largest(lst2))


# Number 3


def shortest(strings):
    short = strings[0]
    for a in strings:
        if len(a) < len(short):
            short = a
    return short

lst3 = ['ase', 'asdff', 'sadfsad', 's']

print(shortest(lst3))




# Number 4

def longest(strings2):
    long = strings2[0]
    for b in strings2:
        if len(b) > len(long):
            long = b
    return long

lst4 = ['sadfsadf', 'sadfs', 'sad', 'sdfghjkld']

print(longest(lst4))


 # Extra from slack


# Number 1


def power(base, exponent):
    if (exponent == 0):
        return 1
    else:
        return base * power(base, exponent -1)

print (power(2,2))


# Number 2

def factorial(factor):
    if factor == 0:
        return 1
    else:
        return factor * factorial(factor-1)
num = 5
print(factorial(num))

# Number 3

def recursiveRange(number):
    if number == 0:
        return 1
    else:
        return number + recursiveRange(number-1)
num2 = 2
print(recursiveRange(num2))

# Number 4

def reverse(string):
    index = len(string)
    reversedString = ''
    while index > 0:
        index -=1
        reversedString += string[index]
    return reversedString
string1 = 'dog'
print(reverse(string1))

# Number 5

def isPalindrome(string2):
    if reverse(string2) == string2:
        print('True')
        return True
    else:
        print('False')
        return False
string3 = 'racecar'

isPalindrome(string3)

# Number 6

def productOfArray(array):
    result = array[0]
    for z in array:
        result = result * z
    return result
arr = [1,2,3,3]
print(productOfArray(arr))

# Number 7

def fib(rng):
    if rng in {0,1}:
        return rng
    return fib(rng - 1) + fib(rng -2)

print(fib(14))