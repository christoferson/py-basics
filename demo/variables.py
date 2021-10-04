# Demo Variables


def demo_variables():
    print("*************** Demo Variables ***************")

    demo_declaration()

def demo_declaration():
    
    # 1.Python has no command for declaring a variable.

    x = 5
    y = "stringvar"

    print(x, y)

    # 2. Variables do not need to be declared with any particular type, and can even change type after they have been set.

    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)