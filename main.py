import pandas


# Checks that user has entered either 'yes' or 'no'...
# If user has said 'no' code breaks
# If user has said 'yes' code continues
# Error message shows when an unexpected
# Value has been entered...

# Functions Go Here..

# Checks that input is either a float or
# an interger that is more than zero, Takes in custom error message
# Number checking function...

# Checks that user has entered either 'yes' or 'no'...


# Checks that user has entered either 'yes' or 'no'...
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return var_item
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


def check_quantity():
    while True:
        response = input("whats the quantity of the item you would like: ")

        rounds_error = "Please press either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 0:
                    print(rounds_error)
                    continue

            except ValueError:
                print(rounds_error)
                continue

        return response


# Checks that user has not completed anything with blank errors
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

        question = ("Would you like to see the instructions: ")

    print("delicous")

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

# This will decorate some of the words that will be shown on the screen
# So the game does not appear boring

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#main routine

# .lower() makes things lowercase (not UPPERCASE)
print("Welcome")
print()

# checks if user wants to see instructions
# if user says "y", show_instructions
# if the user says "yes", show_instructions
# if user says "n", program countinues..
# if user says no, countinue...

question = yes_no("would you like to see the instructions ")

if question == "yes":
    show_instructions()
    print()
     
check_quantity()


play_again = ""
while play_again == "":
  play_again = input("Press <Enter> to Play, Good luck!").lower()

  # Increase # of rounds played 
  rounds_played += 1
 
  # Print round number 
  print()
  print("*** Round #{} ***".format(rounds_played))

  chosen_num = random.randint(1 , 100)
  
  if 1 <= chosen_num = ham:
    chosen = "5"
    chose_dec = "*"
    weight += 4 g

  # If the random # is is between 6 and 36
  # user gets a donkey (subtract $1 from weight)
  elif 6 <= chosen_num <= 36:
    chosen = "Donkey"
    chose_dec = "D"
    weight -= 1

  # The token is either a horse or a zebra 
  # In both cases, subtract $0.50 from weight 
  else:
    # If the chosen number is even
    # Item to a horse
    if chosen_num % 2 == 0:
      chosen = "Horse"
      chose_dec = "H"

    # Otherwise set it to a zebra 
    else:
      chosen = "Zebra"
      chose_dec = "Z"

    balance -= 0.5
  
  print()
  feedback = "You got a {}, your new balance is ${:.2f}".format(chosen, balance)
  statement_generator(feedback, chose_dec)