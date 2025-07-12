

def main_welcome(func):
    
    def wrapper():
        func()
        print("Welcome to the course!")
        
    return wrapper

@main_welcome
def course_introduction():
    print("This is an advanced python course")
    
# main_welcome(course_introcuction)

course_introduction()

'''************************decorators with arguments************************'''

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")