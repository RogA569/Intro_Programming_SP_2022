class Pet:
    """
    Objects of the Pet class are any kind of pet, real or fictional!
    """
    def __init__(self, name, type, age):
        """
        Define attributes of Pet objects.
        :param name: str
        :param type: str
        :param age: str
        :return: None
        """
        self.name = name
        self.type = type
        self.age = int(age) # cast to int for birthday method
        self.fav_treats = [] # initialize as empty list

    def __str__(self):
        """
        Returns a specifically formatted string that gives the name, type, and age of a Pet object
        :return: str
        """
        string_1 = "{} is a {} that is {} years old.\n".format(self.name, self.type, self.age) # format brackets with pet attributes
        string_2 = "Favorite treats:\n"
        string_3 = "" # initialize as empty string
        for treat in self.fav_treats:
            string_3 += "\t{}\n".format(treat) # concatenate each treat to string_3, with a preceding tab and a succeeding newline
        return_string = string_1 + string_2 + string_3 # concatenate all strings into one
        return return_string
    def rename(self, new_name):
        """
        Store a newly given name to the Pet object's name attribute
        :param new_name: str
        :return: None
        """
        self.name = new_name
    def birthday(self):
        """
        Increments the Pet object's age attribute by one
        :return: None
        """
        self.age += 1
    def add_treat(self, treat):
        """
        Appends a given treat to the Pet object's fav_treats attribute
        :param treat: str
        :return: None
        """
        self.fav_treats.append(treat)
        
def main():
    """
    The user is prompted for a command.
    These commands can: 
    - add a Pet object to a list of pets;
    - rename a pet
    - increment a pet's age
    - add a favorite treat of the pet
    - print out a list of adopted pets
    User can stop program by entering the exit code. 
    """
    pets = [] # initialize as empty list; will contain any number of Pet objects
    COMMANDS = ['adopt', 'rename', 'birthday', 'treat', 'pets'] # list of specific, case-sensitive commands user can input
    EXIT_CODE = 'q' # exit code to end while loop execution
    command = input("Enter a command: ") # user prompt for a command
    while command.lower() != EXIT_CODE: # either 'q' or 'Q'
        if command in COMMANDS: # will run if user inputted command is in list of valid commands
            if command == 'adopt':
                name = input('What is the name of the pet? ') # user prompt for pet's name
                pet_type = input('What type of pet is it? ') # user prompt for pet type
                age = input('How old is the pet? ') # user prompt for pet's age
                pet = Pet(name, pet_type, age) # instantiate Pet object with given arguments
                pets.append(pet) # append newly instantiated pet to list of pets
            if command == 'rename':
                current_name = input('What is the current name of the pet? ') # user prompt for pet's name; pet should be in list of pets
                new_name = input('What is the new name of the pet? ') # user prompt for new name for specified pet
                for i in range(len(pets)): # look through list of pets
                    if pets[i].name == current_name: # if pet's name matches user-given name
                        pets[i].rename(new_name) # use Pet object's rename method to rename the pet
            if command == 'birthday':
                birthday_pet = input("Whose birthday is it? ")
                for i in range(len(pets)):
                    if pets[i].name == birthday_pet:
                        pets[i].birthday() # use Pet object's birthday method to increment their age by 1
            if command == 'treat':
                good_pet = input('Who is this treat for? ')
                treat = input('What is the name of the treat? ') # user prompt for the name of treat
                for i in range(len(pets)):
                    if pets[i].name == good_pet:
                        # use Pet object's add_treat method to add treat to the Pet object's fav_treat attribute
                        pets[i].add_treat(treat)
            if command == 'pets':
                for pet in pets:
                    print(pet) # print out the __str__ return value of each pet

        command = input("\nEnter a command: ") # ask the user for a command once again
    
main()
