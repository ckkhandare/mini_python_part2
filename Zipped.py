cities = []
locations=[]
n = int(input("Enter number of cities you want to enter : "))
for i in range(0, n):
    C = input('enter city name: ')
    cities.append(C)
    L = input('enter location: ')
    locations.append(L)

zipped = zip(cities, locations)
print(list(zipped))