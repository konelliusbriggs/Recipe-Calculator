# import libraries...
import pandas


# Functions Go Here..

# Checks that input is either a float or 
# an interger that is more than zero, Takes in custom error message
# Number checking function...
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

# Checks that user has not completed anything with blank errors
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response

# Currency formatting function..
def currency(x):
    return "${:.2f}".format(x)

# Gets expenses, returns a list which has..
# Gets expenses, returns a list which has..
# The data-frame and sub-total...
def get_expenses():

    # Setup dictionaries

    item_list = []
    quantity_list = []
    price_list = []
    package_list = []


    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list,
        "PackageAmount": package_list
    }

    # Loop to get component, quantity and price
    ingredient = ""
    while ingredient.lower() != "xxx":

        print()
        # Get name, quantity and item
        ingredient = not_blank(" Ingredient: ", "please enter an ingredient.")
        print("The ingredient you have chosen is: ", ingredient)
        print()

        if ingredient.lower() == "xxx":
            break

        quantity = num_check("Quantity", "please enter a quantity", int)

        price = num_check("Price ? $", "The price must be a number more than zero", float)

        package_amount = num_check("Package ammount: ", "The price must be a number more than zero", float)

        # Add item, quantity and price to lists
        item_list.append(ingredient)
        quantity_list.append(quantity)
        price_list.append(price)
        package_list.append(package_amount)


    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')


    # Calculate the cost of each component
    # Package Amount / Price x Amount needed
    expense_frame['Cost'] = expense_frame['Price'] / expense_frame['PackageAmount'] * expense_frame['Quantity']
    print(expense_frame)


    # Find sub total..
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Prints expenses frame..

import sys,time
def delprint(text,delay_time): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

def expense_print(heading, frame, subtotal):
    print()
    print("** {} Costs **".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

# Main routine starts here..


# add in delprint when tested!

print("please choose of product name, quantity, weight and your amount servings, ",.05) #printing with a 0.05 delay between each letter
print("")
print("then enter xxx to finalise your request",.05)


# ask user how many servings
people_served = num_check("how many people are you serving?", "please enter a valid input", int)
print("")


# Get product name
product_name = not_blank("Product name: ", "please enter a product")
print("")
print()
print("Please enter your quantity below..")

# Get expenses and sub totals..
expenses_sub = get_expenses()
expense_frame = expenses_sub[0]
total_cost = expenses_sub[1]

cost_per_person = total_cost / people_served


print()
print("**ITEM FINAL COST - {} **".format(product_name))
print()
print(expense_frame)
print()
print(total_cost)
print()
print("The cost per person is {}".format(cost_per_person))
