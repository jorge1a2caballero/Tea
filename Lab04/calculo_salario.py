Max_Horas_Semanales = 40
Horas = int(input("Horas de trabajo:"))
Tarifa = float(input("tarifa:"))
horas_extras = Horas - Max_Horas_Semanales
if (horas_extras > 0):
    salario = (Max_Horas_Semanales * Tarifa) + (horas_extras * (Tarifa *1.5))
else:
    salario = Horas * Tarifa
print(salario)
