# Variable

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable,my_int_to_str_variable,my_bool_variable)
print(type(print(my_string_variable,my_int_to_str_variable,my_bool_variable)))
print("Este es el valor de:", my_bool_variable)

# Funciones Integradas del Sistema
print(len(my_string_variable))
bus=[115,118,556,721]
print(len(bus))

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, edad, alias = "Simon", "Mendez", 40, "Joker"
print("Mi nombre es:", name, surname,". Alias The ", alias,"y mi edad es:",edad)

# Inputs
"""first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(age)"""

"""name = input('Cual es tu nombre: ')
age = input('Cuantos años tienes? ')
print(name)
print(age)"""

# Cambiamos su tipo
name = 40
age = "Simon"
print(name)
print(age)

# ¿Forzamos el tipo?
address = str = "Mi direccioón"
address = True
address = 5
address = 1.2
print(type(address))