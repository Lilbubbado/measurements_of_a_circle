import math
print("Welcome to the area of a circle calculator!")
option = int(input("What do you have? (Choose number) \n1. Radius \n2. Diameter \n3. Circumference\n"))

if option == 1:
  radius = float(input("What is the radius of the circle? "))
  area = math.pi * radius ** 2
  print("Area of the circle = %.2f" %area)

elif option == 2:
  diameter = float(input("What is the diameter of the circle? "))
  diameter_area = math.pi * (diameter / 2) ** 2
  print("Area of the circle = %.2f" %diameter_area)

elif option == 3:
  circumference = float(input("What is the circumference of the circle? "))
  c_area = circumference ** 2 / (4 * math.pi)
  print("Area of the circle = %.2f" %c_area)

else:
  print("Restart and input a valid option.")