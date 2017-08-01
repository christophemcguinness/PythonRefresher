# age = 42
# name = "Julie"
# isTodayCold = True

#Example of a print statment
# print("Hello my name is {}, my age is {}".format(name, age))

"""This
is
an
examples
of
a
multi
line
comment"""

# #examples of if elses
# if  age>18:
#     print("You're older than 18")
#     print( "This is another line.")
# else:
#     print("You're younger than 18")

# if  isTodayCold:
#     print("It is cold today.")
# else:
#     print("It is warm today.")


# year = 1830 # When you check your solution, don't change this number

# if year >2000 and year <2100:
#     print("Welcome to the 21st century!")
# else:
#     print("You are before or after the 21st century")


# def Hello(name="DefaultName", age=100):
#     # print("Hello, World")
#     # print("Hello, Dog")
#     # print("Hello, Chris")
#     print("Hello my name is {}, my age is {}".format(name, age))

# Hello("Mr. Stringy",34)

# Hello()

# #Create a list of dog names (Aka Array)
# dognames = ["Daisy","Lucky","Fluffy","Sally"]

# #instert new dog named Jane
# dognames.insert(0,"Jane")

# #delete a dog from a list
# del(dognames[3])

# #update dog at pos 2 of the list
# dognames[2] = "Billy"

# #print dog 3
# print(dognames[3])


# shoes = ["Spizikes"]

# shoes.insert(1,"Air Force 1")
# shoes.insert(2,"Curry 2")
# shoes.insert(5,"Melo 5")

# print(shoes)

# # #Create a list of dog names (Aka Array), for loops example
# dognames = ["Daisy","Lucky","Fluffy","Sally"]

# for dog in dognames:
#     print(dog)


# #print all number from 1 to 100000
# for x in xrange(1,100001):
#    print(x)

# #while loop example
# while age < 101:
#     print(age)
#     age +=1

#print every number greater than 90
# numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

# for x in numbers:
#     if x > 90:
#         print(x)



# #dictonary
# dogs = {"Chris":12,"Fluffy":6,"Daisy":3}

# del(dogs["Fluffy"])

# dogs["Santa's Little Helper"] = 8

# dogs["Chris"] = 2

# print(dogs)



# """I have provided you with two lists. words and definitions

# Create a dictionary called cooldictionary where you use words for keys and definitions for values"""

# words = ["PoGo","Spange","Lie-Fi"]
# definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

# cooldictionary = {}

# for x in range(0,3):
#     cooldictionary[words[x]] = definitions[x]


# class Dog():

#     dogInfo = "Dogs are cool"

#     def bark(self,str):
#         print("Bark!!! " + str)


# myDog = Dog()

# myDog.bark("Test")

# myDog.name = "Fluffy"
# myDog.age = 34

# print(myDog.name)
# print(myDog.age)

# myDog.dogInfo = "This is a doggy test"

# print(myDog.dogInfo)


# Dog.dogInfo = "This is a doggy test updating the class"

# print(Dog.dogInfo)

# print("As we can see myDog the class object is unaffected '" +myDog.dogInfo + "'")


# class Dog:

#     def __init__(self, name="", age=0, furcolour=""):
#         self.age = age
#         self.name = name
#         self.furcolour = furcolour

#     def bark(self,str):
#         print("Bark!!! " + str)


# myDog = Dog("Daisy",34,"Blue")
# myDog2 = Dog()

# print(myDog.name)
# print(myDog2.age)


"""Add a method to the Car class called age that returns how old the car is (2017 - year)

*Be sure to return the age, not print it*"""

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self,):
        currentYear = 2017
        return currentYear - self.year

myCar = Car(2001,"Ford","Mustang")

print(myCar.age())

