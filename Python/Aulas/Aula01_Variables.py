# Variables
# Python does not need to declare any variables, just assign a value to it and it's done
x = 5
y = "String"
print(x, y)


# Casting
# casting is when you want to put forced a value, passing it
# dataType(valueInside)
a = str("88")
b = int(88)
c = float(88)
print(a, b, c)


# Get the type
# type(variable)
print(type(a))
print(type(x), type(y))


# single or double
i = "String"
j = 'String too'


# Case
I = "is different than 'i'"
J = "is different too"
# ///////////////////////////////////////////////////////
# Variable names
myvar = ""
my_var = ""
_my_var = ""
myVar = ""
MYVAR = ""
myvar2 = ""
# ///////////////////////////////////////////////////////
# Multi Variables
p, q, r, s, t = "values", "in", "different", "variables", 97
print(p, q, r, s, t)


# one to many
fruit1 = fruit2 = "Banana"
print(fruit1, fruit2)


## Unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)


# If put a str with an int it'll give us an error

# ///////////////////////
# Data types
"TypeError: unsupported operand type(s) for +: 'int' and 'str'"

"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""
