#Functions with output

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = formatted_f_name + " " + formatted_l_name
    return full_name

formatted_name = format_name(first_name, last_name)
print(formatted_name)
