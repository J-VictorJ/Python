"""
Fast way:

# Lists = []
# Changing items        list[1] = "Molanguinho"

# Change in a range     list[start:end] = ["Molanguinhuu", "Manguinhaa"]

# Insert items          listName.insert(position, "name")

# append method add a new item at the end of the list       listName.append("name")

# insert, inserts in a specified index      listName.insert(index, "name")

# extend, works as in Java :)       originalList.extend(listToBeInherited)

# remove items      listName.remove()

# remove specific      listName.pop(index)

# del can delete the list or an index       del listName or del listName[index]

# clear the list        listName.clear()

# list Comprehension
# newlist = [expression for item in iterable if condition == True]

# sort()
#descending = listName.sort(reverse = True)
# putting in order = listName.sort(key=str.lower)


# Copy
# listName.copy()

# List()
newList = list(firstList)
"""
# Lists = []
myList = ["mela", "orange", "uva"]  # Lists have an order, if I add a new one it'll get the last position
print(myList)

# I can duplicate elements in a list
myDuplicateList = ["Apple", "Strawberry1", "orange", "Grape", "Strawberry", "Grape", "Grape"]
print(myDuplicateList)

if len(myList) > len(myDuplicateList):
    print(len(myList), " Is bigger")
else:
    print(len(myDuplicateList), " Is bigger")

# Lists can have any data types
list2 = [1, 5, 7, 9, 3, "str"]
list3 = [True, False, False, "788", 12.54]  # Both with different data types
print(list3), print(list2)

# Constructor
lastExList = list(("value1", "value2", "value3", 87))
print(lastExList), print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////


# Access list item

print(myDuplicateList[1]), print(myDuplicateList[1:2]), print(myDuplicateList[-3:-2]), print(myDuplicateList[:2])
#     second item        ,      from 2nd to 3rd       ,         negative from the end,      all  until the 3rd position

# check existence of an item
if "Grape" in myDuplicateList:
    print("Grape is", True)
print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////


# Changing items
myDuplicateList[1] = "Molanguinho", print(myDuplicateList)

# Change in a range
myDuplicateList[0:2] = ["Molanguinhuu", "Manguinhaa"], print(myDuplicateList)

# Change the second value by replacing it with two new values:
myDuplicateList[2:3] = ["Laranjinha", "Uvinha"]  # I've been added two 'in a row'
# The length will change if there isn't a second value
print(myDuplicateList)

# Insert items /  listName.insert(position, "name")
myDuplicateList.insert(8, "Abacaxi"), print(myDuplicateList), print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////


# List items

# append method add a new item at the end of the list
# listName.append("name")
myDuplicateList.append("Tangerina"), print(myDuplicateList)

# insert, inserts in a specified index
# listName.insert(index, "name")
myDuplicateList.insert(1, "banana"), print(myDuplicateList)

# extend, works as in Java :)
# originalList.extend(listToBeInherited)

cobaia = ["Things", 12, 8.235]
cobaia.extend(myDuplicateList), print(cobaia)  # can add from others like dict. tuples....
print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////


# remove items
# listName.remove()
myDuplicateList.remove("Laranjinha")
print(myDuplicateList)

# remove specific
# listName.pop(index)
myDuplicateList.pop(0), print(myDuplicateList)  # if don't specify the item it'll remove the last one

# del can delete the list or an index
# del listName or del listName[index]
del myDuplicateList[1]
print(myDuplicateList)

# clear the list
# listName.clear()
myList.clear(), print(myList), print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////

# Loop in list
for x in myDuplicateList:
    print(x)
print()
# using range() and len()
for i in range(len(myDuplicateList)):
    print(myDuplicateList[i])
print()
# using while loop
i = 0
while len(myDuplicateList) > i:
    print(myDuplicateList[i])
    i = i + 1
print()
# list comprehension
[print(j)for j in myDuplicateList]
print(), print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////


# list comprehension
# adding to a new list only fruits that contains 'a'
novaLista = [l for l in myDuplicateList if 'a' in l]
print(novaLista)

# with iterable
otherList = [m for m in range(10)]
print(otherList)

# to upper again
upperList = [u.upper() for u in myDuplicateList]
print(upperList)

# set all to salut
salut = ["salut" for s in otherList]
print(salut)

# return "orange" instead of "banana":

newlist2 = [x if x != "banana" else "orange" for x in myDuplicateList]
print(newlist2)
# translation: "Return the item if it is not banana, if it is banana return orange".
print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////

# sort()
myDuplicateList.sort()  # case-sensitive, it ordered by Capitalizes ones and then by lower
print(myDuplicateList)

# Descending
myDuplicateList.sort(reverse=True)
print(myDuplicateList)

# solving the first problem
myDuplicateList.sort(key=str.lower)
print(myDuplicateList)

# reverse
myDuplicateList.reverse()
print(myDuplicateList)
print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////

# Copy
# listName.copy()
copyList = myDuplicateList.copy()
print(copyList)

# List()
secondCopyList = list(copyList)
print(secondCopyList)
print("/*" * 30)
# ////////////////////////////////////////////////////////////////////////////

# Join list
# concatenate two or more lists
list3 = copyList + cobaia
print(list3)

# Others ways
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
#
# for x in list2:
#   list1.append(x)
#
# print(list1)

# extend
# list1.extend(list2)
# print(list1)
"""
Method	            Description
append()    	Adds an element at the end of the list
clear()     	Removes all the elements from the list
copy()      	Returns a copy of the list
count()     	Returns the number of elements with the specified value
extend()    	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()    	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()    	Removes the item with the specified value
reverse()   	Reverses the order of the list
sort()	        Sorts the list
"""