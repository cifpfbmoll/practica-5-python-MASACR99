high = int(input("Input the height "))
for i in range(high):
    for j in range(high*2):
        if j <= high+i and j >= high-i:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print(" ")
