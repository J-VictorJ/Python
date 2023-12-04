"""
Fast way

# split
# var.split("whereToSplit")

# Length len()

# Checking "Word" in var

# Slicing var[start:end]

# Upper case, lower case
# var.upper(), lower()

# Removing Whitespace
# var.strip()

# replace
# var.replace("letterInVar", "newLetter")
"""

# Arrays 'n' strings is the same

a = "Hello, world"
print(a[1])

# Looping through strings
for x in "World":
    print(x)

# Length len()
print(len(a))

# Checking
txt = "But something so strong keeps you holding on"
print("something" in txt)

if "strong" in txt:
    print("It's don't make sense but it makes a good song")

print("someone" not in txt)

# Slicing
print(a[4:8])
print("from the start: ", a[:2])
print("To the end:", a[5:])
print("Negative:", a[-6:-1])

# Upper case, lower case
# var.upper(), lower()
print(a.upper())
print(a.lower())

# Removing Whitespace
# var.strip()
print(a.strip())  # It most to contain whitespaces starting and ending the variable

# replace
# var.replace("letterInVar", "newLetter")
print(a.replace("l", "h"))

# split
# var.split("whereToSplit")
print(a.split("l"))  # will split when sees "l" in more lists

# Concatenate
c = a + " " + txt
print(c)

# Format
age = 36
text = "Someone is {} years old"
print(text.format(age))

# or even much extremely harder better
print(f"Someone is {age}")

# Scape
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\ xhh	Hex value
"""
texto = 'This is called \'single quote\' '
print(texto)

"""
Method	            Description
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()     	Returns the number of times a specified value occurs in a string
encode()    	Returns an encoded version of the string
endswith()  	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()    	Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()   	Returns True if all characters in the string are alphanumeric
isalpha()   	Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()    	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()     	Returns a left justified version of the string
lower()     	Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()   	Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()    	Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()     	Returns a trimmed version of the string
swapcase()  	Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate() 	Returns a translated string
upper()     	Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""
