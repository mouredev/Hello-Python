# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=21442

### Conditionals ###

# if

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")
