num = int(input("Input the number"))
print("The divisors of "+str(num) + " are: ", end=" ")
for i in range(num):
    if num % (i+1) == 0:
        print(str(i+1) + ",", end=" ")
