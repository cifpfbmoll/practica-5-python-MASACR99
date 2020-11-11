for i in range(10):
    print(i+1)
print("Fase 1 done")
for i in range(10):
    print((i+1)*2)
print("Fase 2 done")
for i in range(39):
    if(i > 19 and i % 2 == 0):
        print(i)
print("Fase 3 done")
last = 0
for i in range(31):
    if i > 9 and i >= last+4:
        last = i
        print (i)
print("Fase 4 done")
for i in range(9):
    print(40-i*5)
print("Fase 5 done")
