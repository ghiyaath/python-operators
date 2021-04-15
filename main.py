# Task 1 sample solutions
# Given two sides of a right triangle
# Calculate the third side. Get two sides from
# The user

ab = float(input("Please enter the first side: "))
bc = float(input("Please enter the second side: "))

ac = (ab**2 + bc**2)**(1/2)
print("The third side of the triangle equals: "+ str(ac))

# Part 2 of Task 1

ab = float(4)
bc = float(3)
height = ab
base = bc
area = (height * base) / 2
print(area)

# Task 2

my_list = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
print("Minimum number of my list " + str(min(my_list)))
print("Maximum number of my list " + str(max(my_list)))

