# Demo Variables


def demo_variables():
    print("*************** Demo Variables ***************")

    demo_declaration()

    demo_casting()

    demo_type()

def demo_declaration():
    
    # 1.Python has no command for declaring a variable.

    x = 5
    y = "stringvar"

    print(x, y)

    # 2. Variables do not need to be declared with any particular type, and can even change type after they have been set.

    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)

def demo_casting():

    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0 

    print(x, y, z, sep="|")


def demo_type():

    x = 5
    y = "John"
    print(type(x))
    print(type(y)) 