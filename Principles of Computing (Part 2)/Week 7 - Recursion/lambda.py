"""
Learn lambda function
"""

double = lambda x: x * 2

print(double(5))


# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = filter(lambda x: x%2==0, my_list)
print(list(new_list))

# Program to double each item in a list using map()
new_list = map(lambda x: x*2, my_list)
print(list(new_list))