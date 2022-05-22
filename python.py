def exp(numero: int, potencia:int):
    pot = numero ** potencia
    return pot

num = int(input("Ingrese número a calcular potencia"))
pote = int(input("Ingrese potencia"))
total = exp(num,pote)
print(str(num) + " Elevado a la " + str(pote) + " es igual a " + str(total))
