PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    print(names_list)

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in names_list:
        stripped_name = name.strip()
        name_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(name_letter)
