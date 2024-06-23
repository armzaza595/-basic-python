"""
#
# Part: Python Conditions
#
"""

a = 200
b = 500

if a > b:
    print("a > b is true.")
elif a < b:
    print("a < b is true.1")
elif a < b:
    print("a <= b is true.2")
elif a < b:
    print("a == b is true.3")
else:
    print("Nothing")

if a < b: print("a < b is True.")

print("B") if a < b else print("A")

a = 200
b = 30
c = 500
if (a > b) and (c > a):
    print("Both is True.")
if a > b or c > a :
    print("some cond is True.")
if not a > b:
    print("Not")
if b > a:
    print("pass")
    pass
x = 19
if x > 10:
    print("Let's go!")
    if x > 20:
        print("x > 20 is True.1")
        if x > 20:
             print("x > 20 is True.2")
        if x > 20:
                print("x > 20 is True.3")
else:
        print("x > 20 is False.")