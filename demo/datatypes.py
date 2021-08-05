
def demo_datatypes():
    print("*************** Demo Datatypes ***************")
    x = "String Value"
    x = 51 # Int
    x = 82.5 # Float
    x = 3j # Complex 
    x = ["diamond", "spade", "flower"] # List
    x = ("diamond", "spade", "flower", "diamond") # Tuple - A tuple is a collection which is ordered and unchangeable.
    x = range(7) # Range
    x = {"name" : "Conan", "age" : 24} # Dictionary
    x = {"diamond", "spade", "flower"} # Set
    x = frozenset({"diamond", "spade", "flower"}) # Frozen Set
    x = True # Boolean
    x = b"Hello" # Bytes
    x = bytearray(5) # Byte Array
    x = memoryview(bytes(5)) # Memory View
    x = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' # Multiline String
