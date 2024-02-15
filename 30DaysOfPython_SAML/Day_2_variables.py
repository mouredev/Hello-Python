# Exercise 1

first_name = "Simon"
last_name = "Mendez"
country = "Argentina"
city = "Buenos Aires"
age = 40
# Fecha de nacimiento
dia, mes, año = 22, "Julio", 1983
is_married = True
is_true = "True"
light_on = True
print("____________________________________________________")
print("My name is:", first_name, type(first_name))
print("My surname is:", last_name, type(last_name))
print("Country:", country, type(country))
print("City",city,type(city))
print("age:",age,type(age))
print("Fecha de Nacimiento:",dia,mes,año,type(dia),type(mes),type(año))
print("Married:",is_married,type(is_married))
print("is true:",is_true,type(is_true))
print("light on:",light_on,type(light_on))
print("____________________________________________________")
print("Name Length:",len(first_name))
print("Surname Length:",len(last_name))
print("Name Length:",len(first_name),"Surname Length:",len(last_name))
print("____________________________________________________")
# Definicion de variables
num_one=5
num_two=4
variable_total_suma=num_one+num_two
variable_total_resta=num_one-num_two
variable_total_multiplicacion=num_two*num_one
variable_total_division=num_one/num_two
variable_total_modulo=num_two%num_one
variable_total_exponentiation=num_one**num_two
variable_total_floor_division=num_one//num_two
# Prints de respuestas
print("A:",num_one)
print("B:",num_two)
print("La sumatoria es:",variable_total_suma)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("La resta es:",variable_total_resta)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("El producto es:",variable_total_multiplicacion)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("El cociente es:",variable_total_division)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("El modulo es:",variable_total_modulo)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("La potencia es:",variable_total_exponentiation)
print("____________________________________________________")
print("A:",num_one)
print("B:",num_two)
print("La division entera es:",variable_total_floor_division)
print("____________________________________________________")
# Datos de un circulo
radius=30
pi=3.1416
diameter=2*radius
circle_perimeter=diameter*pi
circle_area=pi*radius**2

print("Radio:",radius)
print("Diametro:",diameter)
print("pi:",pi)
print("Perimetro de la circunferencia:",circle_perimeter)
print("Area de la circunferencia:",circle_area)
print("____________________________________________________")

# Pedir datos del usuario y el radio para calcular todo lo referente al circulo

name=input("Nombre:")
surname=input("Apellido:")
country_=input("Pais:")
city_=input("Ciudad:")
age_=input("Edad:")
print("Fecha de Nacimiento")
day_of_birth=input("Dia:")
month=input("Mes(en letras):")  
year_=input("Año:")
married_=input("Estado civil:")
print("____________________________________________________")
print("Nombre:",name)
print("Apellido:",surname)
print("Pais:",country_)
print("Ciudad:",city_)
print("Edad:",age_)
print("Fecha de Nacimiento")
print(day_of_birth,"de ",month,"de ",year_)
print("Estado civil:",married_)
print("____________________________________________________")