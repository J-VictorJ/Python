# Dictionaries
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020,
    "Carburetor": True,
    "colors": ["Red", "Black", "White"]  # dict accept others "arrays" values
}

# len(dictName)

# constructor
person = dict(name="Perneta", age=31, country="Brazil")
print(person)

# Access Items
print(car["model"])
print(car.get("model"))  # both will return the same

# Get Keys
# dictName.keys()
print(car.keys())

# Values
# dictName.values()
print(person.values())

# Get item will return as tuple in a list
# dictName.items()
print(car.items())

# check Loop
if "name" in person:
    print(True)

# change items
# dictName["value"] = newValue
car["year"] = 2018
print(car)

# Update
# dictName.update("value":newValue)
person.update({"age": 28})

# adding items
# dictName["newValue"] = "newValue"
car["color"] = "White"
print(car)

# Update
# dictName.update({"Element":"newValue"})
car.update({"color": "Black"})
print(car)

print("=_=" * 30)
print()

# Removing
cobaia = dict(nome="Zé", sobreNome="Carroça", idade=68, veiculo="Égua", corVeiculo="Preta", pais="Brasil")
cobaia["AKA"] = "Zé da Carroça"

# dictName.pop("item")
cobaia.pop("corVeiculo"), print(cobaia)
# popitem() removes the last item / dictName.popitem()

# delete
# del dictName (delete the entire dictionary) / dictName["item"]
del cobaia["sobreNome"]
print(cobaia)

# clear
# dictName.clear()
# cobaia.clear()
# print(cobaia)


print("=_=" * 30)
print()

# Loop
for x in car:
    print(car[x])  # print all values
    # print(x)  # print names One by one
print()

# return values
for i in car.values():  # the same as in line 83
    print(i)
print()

for j in cobaia.keys():
    print(j)
print()

for a, b in car.items():
    print(a, b)
print()

print("=_=" * 30)
print()

# Copy
# newDict = oldDict.copy()
newDict = car.copy()
print(newDict)

# copy with dict
# newDict = dict(oldDict)
otherDict = dict(cobaia)
print(otherDict)

print()
print("=_=" * 30)

# Nested Dicts

footballPlayers = {
    "player1": {
        "Name": "Fábrec",
        "Position": "ZC"
    },
    "player2": {
        "Name": "Klian",
        "Position": "MC"
                    "player"},
    "player3": {
        "Name": "Marcelo",
        "Position": "LE"
    }
}

# or create 3 dicts and add to a new one
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# Access item
print(footballPlayers["player1"]["Position"])
print(footballPlayers["player2"]["Name"])
for k, l in footballPlayers.items():
    print(k, l)
for xx in footballPlayers:
    print(footballPlayers[xx])

"""
Method	            Description
clear()     	Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()         	Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()      	Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()      	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""