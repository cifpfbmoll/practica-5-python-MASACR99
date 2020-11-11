num = int(input("Input the number"))
is_prime = True
for i in range(num):
    if num % (i+1) == 0:
        if i+1 != num and i > 1:
            is_prime = False
            break
if is_prime:
    print("The number "+str(num)+" is prime")
else:
    print("The number "+str(num)+" is not prime")
