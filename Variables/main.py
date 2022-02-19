
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

