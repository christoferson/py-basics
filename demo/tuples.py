
def demo_tuples():
    print("*************** Demo Tuples ***************")
    mytuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(mytuple)
    # Access
    print(mytuple[1:3])
    print(mytuple[1:])
    print(mytuple[:3])
    # Unpack
    (e1, e2, *ex) = mytuple
    print(e1)
    print(e2)
    print(ex)
    # For Loop
    for mytuple_element in mytuple:
        print(mytuple_element)