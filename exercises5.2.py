num1 = int(input("Input the first number"))
num2 = int(input("Input a second number"))
adder = 0
for i in range(num1, num2+1):
    if i % 2:
        print("The number "+str(i) + " is even")
    else:
        print("The number "+str(i) + " is odd")
