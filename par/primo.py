numero = int(input("informe um número"))
w = 1
y = 0
for x in range(1, (numero+1)):
     if (numero % w) == 0:
         y = y+1
     w = w+1
if y == 2:
     print("numero é primo")
else:
    print("numero não é primo")

