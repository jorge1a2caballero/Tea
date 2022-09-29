def calcularSalario(horas,tarifa):
    horas_extras = horas - Max_Horas_Semanales
    if (horas_extras > 0):
        pago = (Max_Horas_Semanales * tarifa) + (horas_extras * (tarifa *1.5))
    else:
        pago = horas * tarifa
    return pago

try:
    Max_Horas_Semanales = 40
    horas = int(input("Horas de trabajo:"))
    tarifa = float(input("tarifa:"))
    salario = calcularSalario(horas, tarifa)
    print(salario)
except:
    print("Debe introducir un valor numerico.")
    
