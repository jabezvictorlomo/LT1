# PROJECT TITLE: CIRCULAR GARDEN CALCULATOR
## Description:
- **The circular garden calculator** is a program that uses the **math library** and **basic formulas** to calculate the **area, circumference, square root of the area, rounded down value of the area, and rounded up value of the area**.

## Problem Identification:
-  Calculate the area and circumference of the circular garden. square root of the calculated area, the area rounded down to the nearest whole number, and the area rounded up to the nearest whole number.

## Problem Decomposition:
- Determine the square root of the calculated area, the area rounded down to the nearest whole number, and the area rounded up to the nearest whole number.

## Pattern Recoognition:
- Use the formula for the area and circumference of the circle, and use the math library functions math.sqrt() to calculate the square root, math.floor() to calculate the area rounded down to the nearest whole number, and math.ceil() to calculate the area rounded up to the nearest whole number.

## Data Representation:
- The data consists of numerical values and thus can be represented in real and float data types.

## Algorithm Development:
```
Import library
Declare radius, area, circumference, sqrt_area, area_rounded_up, area_rounded_down
Output "Enter radius of the garden: "
Input radius
Assign area = math.sqrt(area)
Assign circumference = 2 * math.pi * radius
Assign sqrt_area = math.sqrt(area)
Assign area_rounded_down = math.floor(area)
Assign area_rounded_up = math.ceil(area)
Output (f"Area of the circular garden: {area:.2f} square meters")
Output (f"Circumference of the circular garden: {circumference:.2f} meters")
Output (f"Square root of the area: {sqrt_area:.2f}")
Output "Area rounded down:", area_rounded_down ,"square meters"
Output "Area rounded up:", area_rounded_up ,"square meters"
```

## How to Run:
- First, open the ***"LT1"*** repository. Then, press  ***"CircularGarden.py"***.

## Input Needed:
- The **radius** of the garden in **meters** and **float value**.

## Sample Output 1:
- Enter the radius of the garden: 5
- Area of the garden: 78.54 square meters
- Circumference of the garden: 31.42 meters
- Square root of the area: 8.86
- Area rounded down: 78 square meters
- Area  rounded up: 79 square meters

## Sample Output 2:
- Enter the radius of the garden: 7
- Area of the garden: 153.94 square meters
- Circumference of the garden: 43.98 meters
- Square root of the area: 12.41
- Area rounded down: 153 square meters
- Area rounded up: 154 square meters

## AUTHOR: Jabez Victor A. Lomo
## GRADE & SECTION: 8-Camia
