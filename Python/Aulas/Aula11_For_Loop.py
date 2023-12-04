# For loops ex
fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]
for x in fruits:
    # Break statement
    if x == "banana":
        break
    for y in adj:
        print(x, y)
    print(x)

# loop through a str
for x in "Core":
    if x == "C":  # C won't be printed it'll jump continue
        continue
    print(x)
print()

# Range Function
# range returns a sequence of numbers
for x in range(6):
    print(x)
print()

for x in range(2, 10):  # here I defined what number to start and finish and put x+1 to add 10
    print(x + 1)

print()

# increment
for x in range(1, 31, 2):  # start from 1 until 31 jumping by 2
    print(x)

# Else I do not put on here but is the same at while-Loop

# Nested Loop. line 8
