def calcularCalificaciones(Calificacion):
    if (Calificacion > 0.9):
        print("sobresaliente")
    elif (Calificacion > 0.8):
        print("Notable")
    elif (Calificacion > 0.7):
        print("Bien")
    elif (Calificacion > 0.6):
        print("suficiente")
    elif (Calificacion <= 0.6):
        print("Insuficiente")
    return Calificacion

try:
    Calificacion = float(input("Introduzca su calificacion:"))
except:
    print("Debe introducir un valor numerico.")
    
