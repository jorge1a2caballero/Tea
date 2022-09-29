contador = 0
suma = 0
minimo = 0
maximo = 0
primerNumero = True
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            break
        contador = contador + 1
        suma = suma + int(numero)
        if (primerNumero):
            minimo = int(numero)
            maximo = minimo
            primerNumero = False
        else:
            if (int(numero) > maximo):
                maximo = int(numero)
            if (int(numero) < minimo):
                minimo = int(numero)
    except:
        print("entrada invalida")
print("Contador", contador)
print("suma", suma)
print("promedio", suma/contador)
print("Maximo", maximo)
print("Minimo", minimo)