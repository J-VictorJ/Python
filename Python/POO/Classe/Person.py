# create a classe
# class ClassName

class Person:  # Definição de uma classe chamada "Person"

    def __init__(self, name, age):  # Construtor da classe "Person" com dois parâmetros
        self.name = name  # Atributo "name" da instância
        self.age = age  # Atributo "age" da instância
        self.birthdate = 2023  # I pass only 2023 instead all calc because it only takes the first age, if I don't
        # change, it's good, if not, it's bad

    def __str__(self):  # Método especial para representação em string da instância
        return f"{self.age}, {self.name}, {self.birthdate  - self.age}"  # Retorna uma string com informações

    def meumetodo(self):  # Método personalizado da classe "Person"
        print(f"My name is {self.name}, I was born in {self.birthdate - self.age}, so I'm {self.age} years old")


p1 = Person("Zé", 65)  # Cria uma instância da classe "Person" com nome "Zé" e idade 65

print(p1)  # Imprime a representação em string da instância
p1.meumetodo()  # Chama o método personalizado da instância

# modify obj properties
p1.age = 33
print(p1)
p1.meumetodo()

# delete obj properties
del p1
p1.meumetodo()

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass
 statement to avoid getting an error.
 
"""