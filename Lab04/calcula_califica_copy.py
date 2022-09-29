def imprimirCalificación(Calificación):
    if(Puntuación >= 0.90 and Puntuación <= 1.00):
        Calificación = "sobresaliente"
    elif(Puntuación >= 0.80 and Puntuación < 0.90):
        Caificación = "notable"
    elif(Puntuación >= 0.70 and Puntuación < 0.80):
        Calificación = "bien"
    elif(Puntuación >= 0.60 and Puntuación < 0.70):
        Calificación = "suficiente"
    elif(Puntuación >= 0 and Puntuación < 0.60):
        Calificación = "Insuficiente"
    else:
        Calificación = "No definido"
    return Calificación



try:
    Puntuación = float(input("Ingrese la puntuación (0 - 1.00): "))
    Calificación = imprimirCalificación(Puntuación)
    print("La calificación de su puntuación es: ", Calificación)
except:
    print("Puntuacion incorrecta")