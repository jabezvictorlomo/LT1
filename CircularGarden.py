import math

radius = float(input("Enter radius of the garden: "))
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
sqrt_area = math.sqrt(area)
area_rounded_down = math.floor(area)
area_rounded_up = math.ceil(area)

print(f"Area of the circular garden {area:.2f} square meters")
print(f"Circumference of the circular garden: {circumference:.2f} meters")
print(f"Square root of the area: {sqrt_area:.2f}")
print("Area rounded down:", area_rounded_down, "square meters")
print(f"Area rounded up:", area_rounded_up, "square meters")