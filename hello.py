# első py script

print(5) #példa
print(5.5)
print("Hello World")
print('Hello World')

print(type(5))
print(type(5.5))
print(type("Hello World"))
print(type('Hello World'))
print(type(True))
print(type(False))

print("apró" 
      "kalap")
print("""apró
    kalap""")

favorite_pet = "kutya"
print(favorite_pet)
favorite_pet = "macs"
print(favorite_pet)

print(type(favorite_pet))

wheel_of_cars = 4
pi = 3.14
print(type(wheel_of_cars))
print(type(pi))

houses = 12
print(houses)
print(type(houses))
houses = "sok"
print(houses)
print(type(houses))

#del(houses)

#type hint : milyen típusú értéket javasolt belerakni a változóba
number_of_cars: int = 16
print(number_of_cars)

number_of_cars_in_parking = number_of_cars
print(number_of_cars_in_parking)

#number_of_cars_in_parking = 12
#print(number_of_cars)
#print(number_of_cars_in_parking)

cars_in_parking = 12
print(number_of_cars)
print(number_of_cars_in_parking)

print(len("alma"))
length_of_apple = len("alma")
print(length_of_apple)

# float float
szorzas = 2.2*2.2
print(szorzas)
# egész egész
osztas = 10/6
print(osztas)
# float egész
kivon = 10.6-10
print(kivon)
kivon_k = 10.7-10
print(kivon_k)

name = "John Doe"
age = 40
print(name, age, "éves")
print(name, age, "éves", sep="")
print(name, age, "éves", sep="**")
print(name, age, "éves", sep=" ")

print("alma" + "körte")
fr1 = "meggy"
fr2 = "cser"
print(fr1 + fr2)

print(name + " " + str(age) + " éves")

#string interpolation
print(f"A {name} emberke {age} éves")

print(f"A 3 + 5 kifejezés értéke: {3 + 5}")

#int-et srting-el nem tudunk összeconcatenalni
#ddd

