# Enclosed by brackets and delimited by colon
mydictionary = {"key1" : "value1", "key2" : "value2"}
print(mydictionary)

# Access 
print(mydictionary["key2"])

# Mix
mydictionary = {"key1" : 2.98, "key2" : [1,2,3], "key3": {"foo": "bar"}}
print(mydictionary)
print(mydictionary["key3"]["foo"])

# Add New Value
mydictionary["key4"] = 5
print(mydictionary)

# Set New Value
mydictionary["key4"] = 7
print(mydictionary)

# Get all Keys
print(mydictionary.keys())

# Get all Values
print(mydictionary.values())

# Get all Entries
print(mydictionary.items())