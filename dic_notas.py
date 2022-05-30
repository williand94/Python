def promedioNotas2(dicNotas: dict):

    sumatoria = 0
    sumatoria += dicNotas['nota1']    
    sumatoria += dicNotas['nota2']    
    sumatoria += dicNotas['nota3']    
    sumatoria += dicNotas['nota4']
    promedio = round(sumatoria / 4,2 )
    if promedio < 3:
        calificacion = "bajo"
    elif promedio > 3 and promedio< 4:
        calificacion = "medio"
    else: calificacion = "alto"   

    return {"promedio":promedio,"calificacion":calificacion}

dicNotas = {}

dicNotas["nota1"] = float(input("Ingrese nota 1 :"))
dicNotas["nota2"] = float(input("Ingrese nota 2 :"))
dicNotas["nota3"] = float(input("Ingrese nota 3 :"))
dicNotas["nota4"] = float(input("Ingrese nota 4 :"))

info = promedioNotas2(dicNotas)

print("El promedio del estudiante es : " + str(info['promedio']) )