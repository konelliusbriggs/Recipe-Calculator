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

quantity = num_check("Quantity: ", "The component name cannot be blank", int)
price = num_check("Price: ", "The component name cannot be blank", float)

print(quantity)
print(price)
