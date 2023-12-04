# IF Elif Else
# Syntax
# if a>b:
x = 5
y = 10
z = 45
# Syntax
if x > y:
    print("x>y")
elif x < y:
    print("x<y")
else:
    print("x most to be equals y")

# Short Hand IF
if y > x: print("y>x")

# short Hand If Else
print("Y") if y > x else print("x")

print("A") if y > x else print("=") if y == x else print("B")  # multiple else

# and, or & not
if x < y and x < z or z > y:
    print("Nó")

# Nested If
if z > 10:
    print("Above ten")
    if z > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# pass
if z > 32:
    pass  # just to avoid some error
