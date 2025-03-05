import  pandas as pd

cities = ["Maringá", "Itabira", "Uberlandia", "Salvador", "Fortaleza"]
population = [403.063, 120.904, 699.097, 2.886698, 2.686612]

#Convert list to Dictionary
population_cities = dict(zip(cities,population))
#Printing Dictionary
print(population_cities)
#Cheking data type
print(type(population_cities))

#Showing information
print(population_cities["Uberlandia"])

#Looking if a city exist
print("Maringá" in population_cities)
print("Sao Carlos" in population_cities)

#Adding new values
population_cities["Victória"] = 365.855

#Checking Addition
print(population_cities)

#Deleting Values
del population_cities["Fortaleza"]

#Checking Deleting
print(population_cities)


