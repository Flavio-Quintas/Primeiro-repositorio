a = int(input("informe um número"))
b = int(input("informe outro número"))
resto_a = a % 2
resto_b = b % 2
if resto_a== 0 and resto_b ==0:
    print("os dois números são pares")
elif resto_a == 0 or resto_b == 0:
    print("foi digitado um número par")
else:
    print("não foi digitado nenhuma número par")