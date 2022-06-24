STOP_ID_IDX = 0 # in the .csv file, this is the index where the stop id for each train is at
STOP_NAME_IDX = 2 # this is the index where the stop name is at

def clean_train_data(raw_data_file):
    """
    Returns a dictionary with every MTA train line and their respective stops
    :param raw_data_file: str
    :return: {}
    """
    mta_dict = {} # initialize as an empty dictionary
    try:
        file_obj = open(raw_data_file, 'r') # if file exists, open it in read mode
    except FileNotFoundError:
        print("File Not Found") # print out human-readable error
        return mta_dict # return an empty dictionary
    
    file_obj.readline() # disregard file's first line

    for line in file_obj:
        data = line.strip().split(',') # for each line, remove whitespace and split the line based on commas into a list
        line_name = data[STOP_ID_IDX][0] # the first character of the stop id represents the train line name
        stop_name = data[STOP_NAME_IDX]
        
        if line_name in mta_dict:
            if stop_name not in mta_dict[line_name]: # if the stop isn't already in the appropriate train line key
                mta_dict[line_name].append(stop_name) # append stop to list of the train line's stops
        else:
            # if the train line is not in the dictionary at all, add it as a new key with the stop as its initial value
            mta_dict[line_name] = [stop_name]
    
    return mta_dict

def pretty_print(train_line, stop_list):
    """
    Pretty prints out a specified train line and its respective stops.
    :param train_line: str
    :param stop_list: []
    :return: None
    """
    print("{} line: {}".format(train_line, ", ".join(stop_list))) # using join method concatenates list elements in a specific manner

def main():
    """
    Program prompts user for a valid train line, unless the user would like to exit the program.
    The program then pretty prints out the stops of the given train line.
    """
    mta_dict = clean_train_data("mta_data.csv") # clean_train_data used to parse data in .csv file into a dictionary
    if mta_dict: # if the dictionary is not empty
        choice = input("Enter a train line, or 'done' to stop: ") # user prompt for a train line or to stop
        while choice.lower() != 'done': # any upper/lowercase combination of the word "done" is the exit code
            pretty_print(choice, mta_dict[choice])
            choice = input("Enter a train line, or 'done' to stop: ") # reprompt

main()
            
        
