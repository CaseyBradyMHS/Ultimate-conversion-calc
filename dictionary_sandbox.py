

def num_check(question, low, high):
    valid = False
    while not valid:

        error = "please enter an integer that is more than {} and less than {}.".format(low, high)

        try:
            # ask for a number
            response = float(input(question))

            # check number is more than 0
            if response > low:
                if response < high:
                    return response
                else:
                    print(error)
                    print()
            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# main routine

# set up dictionaries and 'domain lists'
my_dict = {
    "mm": 1,
    "cm": 10,
    "m": 1000,
    "km": 1000000
}

distance_list = ["mm", "cm", "m", "km"]
weigh_list = ["g", "kg"]


while True:

    given_unit = input("Please enter what unit you are converting from.")

    # limit of 1000 to keep things simple
    number = num_check("Please enter the number you are converting.", 0, 1000)

    # Ask user what they want to convert to
    produced_unit = input("Please enter what unit you wish to convert to.")

    # check that given and produced unit are in the same domain (ie: distance, weight or time)
    if produced_unit in distance_list and given_unit in distance_list:
        # times to get to mm
        # check if it's a key
        if given_unit in my_dict:
            # converts to meters
            multiplied_by = my_dict[given_unit]
            answer = number * multiplied_by

            # convert to required unit
            divided_by = my_dict[produced_unit]
            final_answer = answer / divided_by

            print(final_answer)
    else:
        print(f"Oops - you can't convert between {produced_unit} and {given_unit}. Please try again")
        continue
