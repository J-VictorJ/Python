# Tuples are unchangeable and ordered
# tupleName = ("thing", 01,)

# allow duplicates
firstTuple = ("Banana", "Strawberry", "Mango", "Banana",)
print(firstTuple)

# len(tupleName)
print(len(firstTuple))

# one tuple item
oneTuple = ("Cherry",)  # it must have a comma to be recognized as a tuple
print(type(oneTuple))

# Constructor
constructor = tuple(("Banana", 48, 15.4886, 'A', True))
print(constructor)

print("=-" * 30)
# Access items
print(firstTuple[-3])  # Accessing the third element from the end

if "Banana" in firstTuple:
    print(True)

# Update
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Grape"
x = tuple(y)
print(x)

# For everything that can change a tuple, first pass it to a list and then pass it to a tuple again

# Adding an item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Removing an item
thistuple01 = ("apple", "banana", "cherry")
y = list(thistuple01)
y.remove("apple")
thistuple01 = tuple(y)

# Deleting the entire tuple
thistuple2 = ("apple", "banana", "cherry")
del thistuple2

# Adding a tuple to a tuple
tuple2 = ("Orange",)
firstTuple += tuple2
print(firstTuple)

print("=-" * 30)

# Unpacking
(green, yellow, red) = x
print(green), print(yellow), print(red)
print()

(green, yellow, *red) = firstTuple  # Using * to capture the rest of the elements into 'red'
print(green), print(yellow), print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits  # Using * to capture some elements into 'tropic'
print()
print(green)
print(tropic)
print(red)
print()

# Loop
for i in range(len(fruits)):
    print(fruits[i])
print()
j = 0
while j < len(firstTuple):
    print(firstTuple[j])
    j = j + 1

# Join tuples

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
print()
# Multiply items
multTuple = fruits * 2
print(multTuple)

# Methods:
"""
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
