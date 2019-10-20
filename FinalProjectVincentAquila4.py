"""
Vincent Aquila
Introduction to Python - University of Washington
Final Project
using python 3.6.2

This program creates an errand list showing stores and time at each store

Objectives:
- Contain at least one if/else statement (see the main function).
- Create a class to contain the related functions (class is called Errands, see line 26).
- Run the script from the command line.
- Perform a calculation on a list - started but needs work - (see 'def total_errand_time(locations):' option 5 - 
here hours from each errand are added to provide a total errand time (addition across multiple lists); the 
calculation part works if using static values, but feeding the subfunction from the main function isn't working).
- Use a dictionary - started but needs work - (see 'def total_errand_time(locations):' option 5 - here a dictionary 
is created - it works if using static values, but feeding the subfunction fromthe main function isn't working).
- Each function must be documented with comments telling the purpose of each function, its inputs and outputs.
- Include docstrings telling how to run the script.

* How to run this script *: Run the program.  The program will ask for your name - type your name and press enter.  The
 program bot will introduce himself. Make a selection between 1-6 and press enter.  Press enter after each selection
 to move to the next prompt.  Option 4 gives the bot a chance to say something.
"""

class Errands(object):  # the Errand class defines an errand in terms of a store and time at each store
    # Constrictors
    def __init__(self, theLocation, theTime):
        """
        - when the locations_time function is called, the store name and the amount of time are populated above
        - this init method will be called automatically when locations_time is constructed
        - the location and time are instances of the Errands class, and are used to store variables
        """
        self.store_name = theLocation
        self.amount_of_time = theTime

    # Accessor Methods (the "getters") - allow for retrieval of locations and time
    def getLocation(self):
        return self.store_name

    def getDistance(self):
        return self.amount_of_time

    def __str__(self):  # part of opt 3: uses python's string method when selecting option 3 to show all
        return "Errands[store = " + self.store_name + ", time = " + self.amount_of_time + "]"

def locations_time():   # opt 1: captures a location/store for an errand, and the amount of time required for each
    store_name = input("Enter a store for this errand: ")
    amount_of_time = input("Enter the estimated amount of time each store will require: ")
    return Errands(store_name, amount_of_time)

def total_errand_time(locations):    # opt 5: the below loop calculates total time for all errands
    print("Showing complete errand list of stores and time at each: ")
    for location in locations:
        print(location)
        """
        the program fails where the main function feeds this subfunction - the intention is for the variable inputs 
        of hours from different stores be sent to this function, and their list data type executed by the below 
        calculation - the below calculation works but improperly if the x and y variables below are hard coded, 
        like x = [2,4,5] and y = [6,2,9] - I will continue to work on this
        """
        x = store
        y = time
        xy = {}     # map the two lists together into a dictionary with xy = {}
        b = 0   # starts a counter
        for a in x:  # loop through each item in x, and "grab" each item x with each iteration
            xy[a] = y[b]  # this maps the first item in x to the first item in y    cp[x] = p[y]
            b = b + 1  # iterates the counter
            # print(xy)
        ErrandTime = sum(xy.values())  # totals the values, which is grand total amount of time in hours
        print("Total errand time is: ", ErrandTime)

def location_lookup(locations):    # opt 2: looks up a location in the errand list, and displays store and time
    found = False
    store_name = input("Enter store to lookup: ")
    for location in locations:
        if store_name in location.getLocation():
            print(location)
            found = True
    if not found:
        print("There is no such store on the errand list, see option 1 below.")

def show_all_locations(locations):  # opt 3: this shows all stores and the amount of time at each
    print("Showing complete errand list of stores and time at each: ")
    for location in locations:
        print(location)

def wisdom_for_today(wisdom_for_today):     # opt 4: it outputs a saying - part of the bot feature in the program
    import random
    sayings = ["The more something changes, the more it stays the same.",
               "Calculus is the mathematics of the world.",
               "Don't go to Structure Cellars - you only end up washing the wine glasses, and others steal your wine."]
    print(">" + random.choice(sayings))

def main():     # this is the central engine of the program - it calls up the functions listed above
    UserName = input("Hello, what is your name?: ")
    print("Nice to meet you", UserName)
    print("My name is Alan, and I will be your assistant today.")  # would like to create a chatbot, named after
    # Alan Watts, but he would not be concerned with such trival errand running
    locations = []
    running = True
    while running:
        print("\nMake a selection below, then press Enter.")
        print("1) Where do you need to go today",UserName,"?: ")
        print("2) Enter a store in your list to look up: ")
        print("3) Show all stores and time at each in the errand list: ")
        print("4) Today's wisdom from your chat bot Alan Watts.")
        print("5) Show total time for all errands.")
        print("6) End")
        option = input(">")
        if option == "1":
            locations.append(locations_time())
        elif option == "2":
            location_lookup(locations)
        elif option == "3":
            show_all_locations(locations)
        elif option == "4":
            wisdom_for_today(wisdom_for_today)
        elif option == "5":
            total_errand_time(locations)
        elif option == "6":
            running = False
        else:
            print(UserName, "Thank you for letting me help design your errand list.")


if __name__ == "__main__":  # when the program opens, this is the driving element that calls the main function
    main()
