
def demo_tuples():
    print("*************** Demo Tuples ***************")
    mytuple = ("apple", "banana", "cherry", "apple", "orange")
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
    # Join
    mtuple1 = (1, 2, 3)
    mtuple2 = (4, 5, 6)
    print(mtuple1 + mtuple2)
    print(mtuple1 * 2)   
    # Tuple.count
    print("Count 'apple' in {} : {} instances".format(mytuple, mytuple.count("apple")))
    # Tuple.index
    print("Index of 'orange' in {} : {}".format(mytuple, mytuple.index("orange")) )