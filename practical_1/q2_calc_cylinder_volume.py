# Computing the volume of a cylinder
# C reads in the radius and length of a cylinder and computes its volume using the following formulae:
# area = radius * radius * pi
# volume = area * length

import math
radius = float(input("Input the radius of the cylinder here boiii: ")) 
length = float(input("Input the length of the cylinder here boiii: ")) 
area = radius * radius * math.pi 
volume = area * length

print("The volume of the cylinder is: " + str(volume))
