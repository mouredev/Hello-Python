# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Hola Mundo ###

# Nuestro hola mundo en Python
print("Hola Python")
print('Hola Python')

# Esto es un comentario

"""
Este es un
comentario
en varias líneas
"""

'''
Este también es un
comentario
en varias líneas
'''

# Cómo consultar el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type([1, 2, 3])) # Tipo 'list'
print(type((1, 2, 3))) # Tipo 'tuple'
print(type(range(10)))
print(type(print("Mi cadena de texto")))  # Mi cadena de texto -> Tipo 'NoneType'

"""
Concatenación con f string
"""

variable = "Hola, soy una variable :)"
print(f"La variable te saluda: {variable}")
print(f"El tipo de dato de la variable es: {type(variable)}")
