# Set
# setName = {"values", 12, False}
# are unordered, all times I reload the items will come at a new position
thisSet = {"apple", "banana", "cherry", "apple", True, 1}  # can't have duplicates / true and 1 is the same
print(thisSet)

# len()
print(len(thisSet))
# Constructor
cars = set(("Ford", "Honda", "Opel"))
print(cars)


# Access items and Loop
for x in cars:
    print(x)

print("Ford" in cars)
print("=-" * 30)


# add items
cars.add("AMG")
print(cars)

# add set
# firstSet.update(secondSet)
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(fruits)

# Add any iterable
frutas = ["Maça", "Morango", "Limão"]
fruits.update(frutas)
print(fruits), print(type(frutas))

print()
# Remove
# setName.remove("nameToRemove")
fruits.remove("cherry")
print(fruits)

# discard
# setName.discard("nameToRemove")
fruits.discard("papaya")
print(fruits)

# pop() removes an random element
# setName.pop()

# clear empties all set
# setName.clear()

# delete the set completely
# del setName


print("=-" * 30)
# Join
# line 35

# only duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)  # method
print(x)

# items in both
z = x.intersection(y)  # it is just to return a new set
print(z)

# Keep All but not duplicates
x.symmetric_difference_update(y)
print(x)


"""
Method	                            Description
add()	                        Adds an element to the set
clear()                     	Removes all the elements from the set
copy()                        	Returns a copy of the set
difference()                	Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()               	Returns a set, that is the intersection of two other sets
intersection_update()       	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()                  	Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()            	        Removes the specified element
symmetric_difference()      	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()                 	    Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""