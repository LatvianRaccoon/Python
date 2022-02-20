
# Variables
a = 5
b = "John"
print("Variable a is " + str(a))
print("Variable b is " + b)

# Casting
c = str(3)
d = int(4)
e = float(3)

# Get the Type
print("Type of variable c, d and e")
print(type(c))
print(type(d))
print(type(e))

# Many Values to Multiple Variables
a, b, c = "orange", "banana", "cherry"
print(a)
print(b)
print(c)

# One Value to Multiple Variables
a = b = c = "orange"
print(a)
print(b)
print(c)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)

# Output Variables
a = "awesome"
b = "w3school is "
c = "cool"
print("Python is " + a)
print(b + c)

# Global variables
x = "awesome"

def my_func():
    print("Python is " + x)

my_func()


# Create a variable inside a function, with the same name as global variable
z = "cool"
def my_func1():
    z = "fantastic"
    print("w3school is " + z)

my_func1()

print("Python is " + z)


