# function Syntax
# def func_name():
#    code...
# func_name()

def multiply(x, y):
    return x * y


print(multiply(2, 5))


# Arguments


def saudar(nome):  # parameter
    print(f"Olá, {nome}.")


saudar("Fulano")  # argument
saudar("Ciclano")


# number of arguments


def someone(nome, idade):  # I need to pass 02 arguments too, if false it will give an error
    print(f"{nome}, that is: {idade}, Welcome")


someone("Some People", 14)


# arbitrary arguments ARGS/ Returns a tuple


def puppy(*puppy):
    print(
        F"The puppy's name is {puppy[0]}, and more things like age, {puppy[1]}, forcing, color {puppy[2]}, {puppy[3]} again")
    # explaining: I'll pass 3 arguments when I call the def, so I need to put 'em in order doing in the order I want to


puppy("Bartolomel", 3, "White", "Carroça")


# I can pass the args in the order I want, the print will be the same

# **Kwargs, returns a dict


def child(**kwargs):
    print(
        f"Something {kwargs['cor']}, name:{kwargs['name']}, age:{kwargs['age']}, good lung:{kwargs['lungs']}, predominate Leg:{kwargs['leg']}, hand:{kwargs['hand']}")


child(cor="Verde", name="Genilson", lungs="Both", leg="Left", hand="Right", age=12)


# it's cool to use


# Default parameters and Return values
def calc(x=0):
    return 3 * x


print(calc())
print(calc(5))
print(calc(1))


# pass use pass when create a def but it won't be filled now


# Recursion


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
