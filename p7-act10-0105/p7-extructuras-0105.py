# ==========================================
# EJEMPLOS DE IF, ELIF Y ELSE
#Iker Montoya
# ==========================================

# EJEMPLO 1
calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")


# EJEMPLO 2
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 15:
    print("Eres adolescente")
else:
    print("Eres menor de edad")


# ==========================================
# EJEMPLOS DE FOR
# ==========================================

# EJEMPLO 1
for numero in range(1, 6):
    print("Número:", numero)


# EJEMPLO 2
for calificacion in range(70, 101, 10):
    print("Calificación:", calificacion)


# EJEMPLO 3
for actividad in range(1, 6):
    print("Actividad", actividad, "completada")


# ==========================================
# EJEMPLOS DE WHILE
# ==========================================

# EJEMPLO 1
numero = 1

while numero <= 5:
    print("Número:", numero)
    numero = numero + 1


# EJEMPLO 2
calificacion = 50

while calificacion <= 100:
    print("Calificación:", calificacion)
    calificacion = calificacion + 10


# EJEMPLO 3
actividad = 1

while actividad <= 5:
    print("Actividad", actividad, "realizada")
    actividad = actividad + 1

    print("Iker Mnotoya 0105")