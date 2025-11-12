# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=24010

### Python Package Manager ###

##PIP (Python Install Packages)
#this command can be install new packages and utilities for different purposes from PyPi repository

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install pandas (pandas is a data analysis library)
# pip install requests (requests is a library to make HTTP requests)
# pip install numpy (numpy is a library for numerical computing)

import pandas
from mypackage import arithmetics
import requests
import numpy

# some packages can be used from a alias to simplify their use
# import numpy as np
# this is a common practice for numpy package
# import pandas as pd

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package


print(arithmetics.sum_two_values(1, 4))
