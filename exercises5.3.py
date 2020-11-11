num1 = int(input("Input the first number"))
num2 = int(input("Input a second number"))
adder = 0
for i in range(num1, num2+1):
    adder += i
print("The sum from " + str(num1) + " to "+str(num2) + " is: " + str(adder))
