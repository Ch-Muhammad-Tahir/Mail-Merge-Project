PLACEHOLDER = "[name]"

# Read Names From File
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letters_file:
    letters_contents = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


