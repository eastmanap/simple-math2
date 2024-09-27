# Apollos Eastman
# Sep 27 2024
# Simple math 2

# Task 1
DISCOUNT = 0.80
# Input
price = float(input('How much does your item cost:'))
# Process
discounted_price = price * DISCOUNT
# Output
print (f'Your item costs {price} before discounts and {discounted_price} after discounts.')

# Task 2
print ()
# Input
length = float(input('What is the length of your rectangle?'))
width = float(input('What is the width of your rectangle?'))
# Processing
area = length * width
# Output
print (f'If the length of a rectangle is {length} and the width is {width} than the area is {area}.')

# Task 3
print()

bacteria_num = 10
hours = 5

total_bacteria = bacteria_num * 2 * hours

print (f'If there are {bacteria_num} bacteria to start, then after {hours} hours there will be {total_bacteria} bacteria.')

# Task 4
print()

distance = 200
speed = 90

time = distance / speed

print (f'If they draive at {speed} kilometers an hour for {distance} kilometers it will take {time} hours to get there.')

# Task 5
print ()

group_num = 23
slices = 8

slices_left = slices - group_num

print (f'If there were {group_num} people that had to split {slices} slices, there would be {slices_left} slices left, which means that not everyone would get a slice.')
