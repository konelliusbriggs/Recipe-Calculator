# Checks that user has entered either 'yes' or 'no'...
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return response

        print("Please enter either yes or no...\n")

def show_instructions():
    print("recipe instructions", ".")
    print("")
    print("choose what item that you would like from the list of recipes")
    print("")
    print("choose the quantity of the item")
    print("")
    print("then choose the cost per gram")
    print("")
    return ""