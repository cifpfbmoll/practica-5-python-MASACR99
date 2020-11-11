high = int(input("Input the height "))
thicc = int(input("Input the thickness "))
for i in range(high):
    if i == 0 or i == high-1:
        for j in range(thicc):
            print('x', end=" ")
        print(" ")
    else:
        print("x  x")
