with open("./file1.txt") as numbers_file1:
    numbers = numbers_file1.readlines()

with open("./file2.txt") as numbers_file2:
    numbers2 = numbers_file2.readlines()

result = [int(num) for num in numbers if num in numbers2]

print(result)

