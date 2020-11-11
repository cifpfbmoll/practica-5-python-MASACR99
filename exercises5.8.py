high = int(input("Input the thickness"))
for i in range(high-1):
    for j in range(i+1):
        print('x', end=" ")
    print(" ")
for i in range(high):
    for j in range(high-i):
        print('x', end=" ")
    print(" ")
