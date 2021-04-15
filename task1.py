# Calculate the side of a triangle

ab = input("Please enter ab: ")
bc = input("Please enter bc: ")

ac = (int(ab)**2 + int(bc)**2)**(1/2)

print("ac is: " + str(ac))

# Calculate the area and convert to binary
height = ab
base = bc
area = (int(height) * int(base)) / 2

print("The area of the triangle is: " + str(area))
print("The area of the triangle is: " + str(bin(int(area))))
