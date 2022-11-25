# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=24010

### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy
import numpy 

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas
import pandas 

 # pip list
 # pip uninstall pandas
 # pip show numpy

# pip install requests
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))