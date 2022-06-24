def read_menu(filepath):
    """
    Returns menu information as a dictionary.
    :param filepath: str
    :return: {}
    """
    menu = {} # initialize as an empty dictionary
    try:
        file_obj = open(filepath, 'r') # if file exists, open it in read mode
    except FileNotFoundError:
        print("File Not Found") # print out human-readable error
        return menu # return an empty dictionary
    
    file_obj.readline() # skip first line of file
    
    for line in file_obj:
        data = line.strip().split(",") # remove whitespace and, with "," as separator, split each line into a list
        menu[data[0]] = float(data[1]) # add key-value pair to menu dictionary; value is casted to a float
    
    file_obj.close()
    return menu

def order_food(menu):
    """
    Returns the total cost of items the user orders from the menu.
    :param menu: {}
    :return: int or float
    """
    total_cost = 0 # initialize
    food = input("Enter what you want off the menu: ") # user prompt for item to order

    while food.lower() != 'q': # 'q' or 'Q' exits the constant program prompt
        total_cost += menu[food] # add cost of menu item to total_cost
        food = input("Enter what you want off the menu: ") # re-prompt
    return total_cost

def main():
    """
    Run two functions that will allow the user to read the menu and order food from that menu
    """
    menu = read_menu("menu.csv") # menu information from menu.csv is stored in variable
    cost = order_food(menu) # By ordering food, the program stores the cost in variable
    print("Your food costs {} dollars".format(cost)) # print out the total cost for ordered items

main()
