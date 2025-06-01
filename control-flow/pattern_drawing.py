length = int(input("Enter the size of the pattern:"))

width = 0
while width < length :
    for size in range(length):
        print("*", end="")

    print()
    width +=1
