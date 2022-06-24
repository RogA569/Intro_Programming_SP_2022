import random

def print_lst(lst, name):
    """
    Prints out applicable list's header and contents in a specific format
    :param lst: [] or [str]
    :param name: str
    """
    print()
    print(name, "list: ") # print header

    for item in lst: # for each item
        print("\t-", item) # print each item in specific format
    
    print()

def add_to_lst(lst, items):
    """
    Extends list with items.
    :param lst: [] or [str]
    :param items: [str]
    :return: None
    """
    lst.extend(items)

def remove_from_lst(lst, items):
    for item in items:
        if not len(lst): # if the list is empty
            return # return none and end function execution
        if item == "random": # if user types in "random" after typing in "remove"
            rand_item = get_rand_item(lst)
            lst.remove(rand_item) # remove randomly selected item from lst
        elif item in lst: # if and only if item is in lst
            lst.remove(item) # remove that item from the list

def get_rand_item(lst):
    """
    Returns a randomly selected element from a given list.
    :param lst: []
    :return: []
    """
    return random.choice(lst) # choose random element from lst

def run_dynamic_list(my_list):
    """
    Returns a dynamic list.
    The contents can be added or removed based on specific user input commands.
    :param my_list: []
    :return: [] or [str]
    """
    name = input("Enter a name for your list: ") # user prompt for the name of the dynamic list
    inp = "" # initialize list elements

    while inp.lower() != 'q': # as long as user doesn't input 'q' or 'Q', loops continues execution
        print_lst(my_list, name) # function print_lst runs with my_list and name as arguments

        inp = input("Enter a command: ") # user prompt for an input command; commands can be upper/lower case
        inp_lst = inp.split(" ") # separate the command from any extra words, if needed
        command = inp_lst[0].lower() # command, which should be the first element, is normalized to lowercase

        if command == "add":
            items = inp_lst[1:] # select elements from index 1 to end of list
            add_to_lst(my_list, items) # function used to add items to dynamic list
        elif command == "random":
            print("Random Item:", get_rand_item(my_list)) # print a random item from the list, using get_rand_item function
        elif command == "remove":
            items = inp_lst[1:]
            remove_from_lst(my_list, items) # function used to remove items from dynamic list

    return my_list

def main():
    """
    A list using the run_dynamic_list function is saved and printed.
    """
    my_list = run_dynamic_list([]) # initialize the run_dynamic_list function with an empty list
    print(my_list) # print out the list, which may or may not be different from its initial state
main()
