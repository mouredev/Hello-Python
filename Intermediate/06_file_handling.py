# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# Posiciona el cursor al inicio del fichero
txt_file.seek(0)

# Lee e imprime todo el contenido del fichero
print(txt_file.read())

# Lee e imprime 10 caracteres desde el inicio del fichero
txt_file.seek(0)
print(txt_file.read(10))

# Lee e imprime el resto de la línea actual desde la posición 11
print(txt_file.readline())

# Lee e imprime la siguiente línea
print(txt_file.readline())

# Lee e imprime las líneas restantes del fichero
for line in txt_file.readlines():
    print(line)

# Escribe una nueva línea en el fichero
txt_file.write("\nAunque también me gusta Kotlin")

# Posiciona el cursor al inicio del fichero, lee e imprime todo su contenido
txt_file.seek(0)
print(txt_file.read())

# Cierra el fichero
txt_file.close()

# Agrega una nueva línea en el fichero
with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?
