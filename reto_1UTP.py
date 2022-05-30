def cliente(informacion:dict):
    apto = True
    if informacion['edad'] > 18:
        atraccion = "X-Treme"
        if informacion['primer_ingreso'] == True :
            total_boleta = 20000 -  20000 * 0.05 
        else:
            total_boleta = 20000

    elif informacion['edad'] >=15 and informacion['edad'] <= 18:
        atraccion = "Carroschcones"
        if informacion['primer_ingreso'] == True :
            total_boleta = 5000 -  5000 * 0.07 
        else:
            total_boleta = 5000

    elif informacion['edad'] >=7 and informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        
        if informacion['primer_ingreso'] == True :
            total_boleta = 10000 -  10000 * 0.05 
        else:
            total_boleta = 10000        
    else:
        apto = False
        atraccion = 'N/A'
        total_boleta = 'N/A'
    
    return print({'nombre':informacion['nombre'],
                  'edad':informacion['edad'],
                  'atraccion':atraccion,
                  'apto':apto,
                  'primer_ingreso':informacion['primer_ingreso'],
                  'total_boleta':total_boleta})



informacion = {
    "id_cliente":20,
    "nombre":"Tatiana Ruiz",
    "edad":20,
    "primer_ingreso": False
}



informacion3 = {
    "id_cliente":3,
    "nombre":"Tatiana Suarez",
    "edad":17,
    "primer_ingreso": False
}

informacion2 = {
    "id_cliente":2,
    "nombre": "Gloria Suarez",
    "edad": 3,
    "primer_ingreso": True
}

informacion1 = {
    "id_cliente":1,
    "nombre": "Johana Fernandez",
    "edad": 20,
    "primer_ingreso": True
}


cliente(informacion)