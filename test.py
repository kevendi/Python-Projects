import os
import sys
import pytest

from decimal import Decimal, localcontext

print ("test")

x = 14
y = 13
z = 14

if x < y < z:
    print(x)
    print(y)
    print(z)
elif x == y:
    print ("Not valid")
else:
    print ("Test")

while (x == 14):
    print ("x is 14")
    x = x + 1
else:
    print ("x is 15")

for i in range(10):
    print(i)
    i = 5  # does not affect the loop

print (i)

try:
    raise TypeError
except:
    print(repr(sys.exception()))
    try:
        raise ValueError
    except:
        print(repr(sys.exception()))
    print(repr(sys.exception()))        # exception is returned to its previous value

print(repr(sys.exception()))

# if this try block creates exception groups - the following function can't be called?
try:
    raise BlockingIOError
except* BlockingIOError as e:
    print(repr(e))

def test():
    try:
       return 'try'
    finally:
        return 'finally'
    
test()

with open("example.txt", "w") as file:
    file.write("Hello World!")

# or

# Safely open the file
file = open("example.txt", "w")

try:
    file.write("Hello, World again!")
finally:
    # Make sure to close the file after using it
    file.close()

# scan current directory
with os.scandir(".") as entries:
    for entry in entries: 
        print(entry.name, "->", entry.stat().st_size, "bytes")

with localcontext() as loc:
    loc.prec = 3
    a = Decimal("45")
    b = Decimal("67")
    print (a/b)

print (45.0/67.0)

with pytest.raises(ZeroDivisionError) as exeption:
    8/0

assert str(exeption.value) == "division by zero"

cars = {"honda":"integra", "toyota":"celica"}
with pytest.raises(KeyError) as exc:
    cars["porsche"]

# flag serves as a guard
flag = False
match (100, 200):
   case (100, 300):  # Mismatch: 200 != 300
       print('Case 1')
   case (100, 200) if flag:  # Successful match, but guard fails as flag is False
       print('Case 2')
   case (100, y):  # Matches and binds y to 200
       print(f'Case 3, y: {y}')
   case _:  # Pattern not attempted
       print('Case 4, I match anything!')