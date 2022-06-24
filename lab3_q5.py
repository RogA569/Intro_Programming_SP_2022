"""
This program asks three questions to the user. 
Based on the user's reply to each of these questions, different print statements showcasing a different snakes are executed.
These snakes and their fun facts are a not-so-subtle analogy to various programming languages.
No conditional operators are used in this problem, simply nested if-else statements.
"""

# Flags; note that they're only true if and only if user types in "yes" 
is_snake_venomous = input("Is the snake venomous? ") == "yes"
is_snake_small = input("Is the snake small? ") == "yes"
is_snake_aggressive = input("Is the snake aggressive? ") == "yes"

if is_snake_venomous:
    if is_snake_small:
        if is_snake_aggressive:
            # Matlab Mamba
            print("That is a Matlab Mamba. Commonly used to introduce mechies to working with snakes. They often hatch plots to catch their prey and enjoys graphical images.")
        else:
            # Verilog Viper
            print("That is a Verilog Viper. Many people first see these snakes around architectures. Reports claim that they like to chew on circuit wires.")
    else:
        if is_snake_aggressive:
            # C++ Cobra
            print("That is a C++ Cobra. Evolved from the C Serpants many years ago. Reports show they have the weird habit of pointing at objects with their tails.")
        else:
            # C Serpent
            print("That is a C Serpent. Can be found in the sea. Has the ability to control their memory, being able to allocate parts of their brain for certain tasks and permanently delete information from their memories.")
else:
    if is_snake_small:
        if is_snake_aggressive:
            # Javascript Treesnake
            print("That is a Javascript Treesnake. Despite its name, they are completely different from the Java Kingsnake. They like to lay on the nodes of a tree to browse through nearby animals for their next meal.")
        else:
            # Java Kingsnake
            print("That is a Java Kingsnake. Very befitting of their name, they are objectively the most sophisticated snake species. One may even say they are very classy.")
    else:
        if is_snake_aggressive:
            # Assembly Anaconda
            print("That is an Assembly Anaconda. Many people hate learning about these snakes, as they look very intimidating. In the Totally Official CS1114 Snake Register, they are said to love being in low level altitudes.")
        else:
            # Python Python
            print("That is a Python Python. One of the largest and most famous snakes. However, they are pretty slow, and are commonly used to introduce people to learning about snakes.")
