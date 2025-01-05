# Object Oriented Programming

# Basic Classes and Objects
class Car:

    #class variable counts that how many cars are created as objects
    total_cars = 0
    

    def __init__(self, brand, model, color):

        #we have make it private
        self.__brand = brand

        #we have to make it READ ONLYY
        self.model = model

        self.color = color
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol"

    def full_name(self):
        return f"{self.brand}{self.model}"
    
    #we have make it READ ONLY
    @property
    def model(self):
        return self.model
    

    #static method
    #known as DECORATORRRRRRS
    @staticmethod
    #self is not required
    def General_Description():
        return f"cars are amazing vehicles"

class ElectricCar(Car):
    def __init__(self,brand,model,color,Battery_size):
        #Inheritances from parent class
        super().__init__(brand,model,color)
        #required
        self.Battery_size = Battery_size

    def fuel_type(self):
        return "Electric charge"

tesla = ElectricCar("Tesla","S","White","20kWh")
my_car = Car("Honda", "Civic", "Red")
my_2nd_car = Car("maruti","swift","blue")
safari = Car("Honda","Safari","Black")

#we can write like this
my_car.model = "Civic"
print(my_car.model)


print(my_car.General_Description())
print(Car.General_Description())

print(safari.fuel_type())
print(my_car.brand)
print(my_car.full_name()) #creates and calls the function

print(tesla.Battery_size)
print(tesla.full_name())
print(my_2nd_car.brand)


# Incapsulation Meaning
# to make the classes more secure and onn;y can be accessable by the methods 
# example as {my_car.color} is can be accessable 
# but we have to use the method to access it

print(my_car.get_brand())

# we have make it an privated by putting __ before the variable
# now you cant access it directly out of class
print(my_2nd_car.__brand)

# tou can access it by calling the method
print(Car.total_cars)

# static method
# a method that is not bound to any object
# it is not a part of the object
# a method that to an class rather than an object or instance of the class