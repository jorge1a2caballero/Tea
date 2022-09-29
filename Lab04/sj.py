contador = 0
suma = 0
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            break
        contador = contador + 1
        suma = suma + int(numero)
    except:
        print("Entrada invalida")
print("Contador", contador)
print("suma", suma)
print("promedio", suma/contador)