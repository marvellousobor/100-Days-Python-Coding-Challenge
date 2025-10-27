programming_dictionary = {
    "Bug": "An error is a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


#Adding new item to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again",
# print(programming_dictionary["Bug"])

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A bug in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])