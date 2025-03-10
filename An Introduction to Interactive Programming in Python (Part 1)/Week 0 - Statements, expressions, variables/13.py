"""
Given a template that pre-defines the variables width and height that are the lengths
of the sides of a rectangle, write an assignment statement that defines a variable
perimeter whose value is the perimeter of the rectangle in inches.
"""


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
width = 4
height = 7


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 7
# height = 4


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 10
# height = 10


###################################################
# Rectangle perimeter formula
# Student should enter formula on the next line.

perimeter = 2 * width + 2 * height

###################################################
# Test output
# Student should not change this code.

print "A rectangle " + str(width) + " inches wide and " + str(height),
print "inches high has a perimeter of " + str(perimeter) + " inches."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.
