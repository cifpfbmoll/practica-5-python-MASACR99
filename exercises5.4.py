num1 = int(input("Input the number"))
adder = 1
for i in range(num1):
    adder *= i+1
print("The factorial from " + str(num1) + " is: " + str(adder))
