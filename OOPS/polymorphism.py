class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    # method overriding
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

# Example usage
if __name__ == "__main__":
    my_dog = Dog()
    my_cat = Cat()

    make_animal_speak(my_dog)  # Output: Dog barks
    make_animal_speak(my_cat)  # Output: Cat meows

# polymorphism with functions and methods
class Shape:
    def area(self):
        return "the area of the figure"
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)

# function that demonstrates polymorphism
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Example usage of polymorphism with shapes
if __name__ == "__main__":
    my_rectangle = Rectangle(5, 10)
    my_circle = Circle(7)

    print_area(my_rectangle)  # Output: The area is: 50
    print_area(my_circle)      # Output: The area is: 153.86
    
# polymorphism with abstract base class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

# create objects of car and motorcycle
car = Car()
motorcycle = Motorcycle()
# demonstrate polymorphism
print(car.start_engine())        # Output: Car engine started
print(motorcycle.start_engine())  # Output: Motorcycle engine started
    