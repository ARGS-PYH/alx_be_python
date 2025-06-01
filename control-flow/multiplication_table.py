# choosing the number to perform multiplication table with
number = int(input("Enter a number to see its multiplication table:"))
# rearrangin my variable to look like Z= X*Y
y = number
# iterating to generate a multiplication table
# x is the iterated number while y is inout from user
for x in range(1,11):
    z = y * x
    print(f" {y} * {x} = {z}" )