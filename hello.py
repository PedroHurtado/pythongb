def primer_divisible_por_siete(numeros):
    for numero in numeros:
        if numero >= 0 and numero % 7 == 0:            
            return numero