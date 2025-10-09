# DATA TYPES

# STRING
print("Hello"[0]) #Subscripting is pulling out a particular element from a string

# INTEGER
print(123 + 345)

#float
print(3141.59)

#Boolean
True
False


print(len(12345)) #gives error. strings can be counted
num_char = len(input("What is your pets name: "))
print("Your name has " + str(num_char) + " characters.")  #Type casting or conversion

B = "12345"
print(type(B))
print(str(B))

print(70 + float("150.5"))
print(str(20) + str(25))

# print(int(first_digit) + int(second_digit))

#MATHEMATICAL OPERATIONS IN PYTHON
3 + 5
7 - 4
3 * 2
print(6 / 3) #you will always get a floating point as an answer in python 
2 ** 3

#Order of arrangement in python
#PEMDAS
#Parentheses(Brackets)- ()
#Exponents- **
#Multiplication- *
#Division- /
#Addition- +
#Subtraction- -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)