# ----- functions go here -----

# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # make string with 5 characters
    ends = decoration * 5
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# sorts what the user has chosen into file types
def user_choice():
    # list of valid responses3
    distance_ok = ["distance"]
    weight_ok = ["weight"]
    time_ok = ["time"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("Unit type (distance / weight / time)").lower()

        # check for valid response and return text image or integer

        if response in distance_ok:
            return "distance"

        elif response in weight_ok:
            return "weight"

        elif response in time_ok:
            return "time"

        # error message
        else:
            print("Please choose a valid unit!")
            print()


# instructions display
def instructions():
    statement_generator("Instructions / information", "=")
    print('''
This program will convert any from of distance, time and weight to a 
different unit (meter to centimeter, second to hour, kilogram to gram etc)
first enter the type of thing you want, then the unit you are translating from, 
then the number. 
Complete as many calculations as necessary, pressing <enter>
at the end of each calculation or any key to quit. 
    ''')
    return ""


# integer checker
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


def distance_conversion():
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


# ----- main routine goes here -----
# dictionary
my_dict = {
    "mm": 1,
    "cm": 10,
    "m": 1000,
    "km": 1000000,
}
# lists
distance_list = ["mm", "cm", "m", "km"]
weigh_list = ["g", "kg"]

# heading
statement_generator("Conversion Calculator for distance, time & weight", "-")

# display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue. ")

if first_time == "":
    instructions()

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # ask the user for the unit type
    data_type = user_choice()
    print("you chose", data_type)
    # convert distance
    if data_type == "distance":
        distance_conversion()
    # convert weight
    elif data_type == "weight":
        weight_conversion()
    # convert time
    else:
        time_conversion()

    print()
    keep_going = input("Press <enter> to continue or any other key to quit. ")
    print()
