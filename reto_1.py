def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo >= 3:
        valorIntereses = capital * 0.03 * tiempo / 12
        valorTotal = valorIntereses + capital    
    elif tiempo <= 2:
        valorPeder = capital * 0.02
        valorTotal = capital - valorPeder
              
    return "Para el usuario {0} La cantidad de dinero a recibir, según el monto inicial {1} para un tiempo de {2} meses  es: {3} ".format(usuario,capital,tiempo,valorTotal)

print(CDT("AB1012", 1000000, 3))
print(CDT("ER3366", 650000, 2))


