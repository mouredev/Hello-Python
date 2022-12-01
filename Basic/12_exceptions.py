# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
