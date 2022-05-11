print("VELOCITY CALCULATOR")
print("(All values must be whole numbers.)")
print("Enter first position below (in meters)")
x = int(input())
print("Enter second position below (in meters)")
y = int(input())
print("Enter elapsed time below (in seconds)")
t = int(input())
if x == int(1):
    print("First position is", x, "meter")
else:
    print("First position is", x, "meters")
if y == int(1):
    print("Second position is", y, "meter")
else:
    print("Second position is", y, "meters")

if t == int(1):
    print("Elapsed time is", t, "second")
else:
    print("Elapsed time is", t, "seconds")

v = (y - x) / t
print("Velocity in meters per second is", v, "m/s")



