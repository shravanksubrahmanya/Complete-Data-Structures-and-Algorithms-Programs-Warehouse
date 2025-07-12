class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        return f"Official: Person(name={self.name}, age={self.age})"
    
# person = Person("Shravan", 26)
# print(person)
# print(repr(person))

# mathematical operations with custom objects
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1 / 2)
print(v1 == v2)
