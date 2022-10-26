# Clase en vídeo (25/10/22): https://www.twitch.tv/videos/1634818287

### File Handling ###

import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "w+") # Leer, escribir y sobrescribir si ya existe

txt_file.write("Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt")

