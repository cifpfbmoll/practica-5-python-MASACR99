high = int(input("Input the height"))
adder = 0
for i in range(high):
    for j in range(high-i):
        print('x', end=" ")
    print(" ")
