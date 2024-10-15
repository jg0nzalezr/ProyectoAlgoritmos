import random
from cartas import Carta  # Importamos la clase Carta desde cartas.py

# Crear el mazo completo con 112 cartas siguiendo las especificaciones
def crear_mazo():
    colores_claros = ['Azul', 'Verde', 'Rojo', 'Amarillo']
    colores_oscuros = ['Rosa', 'Verde Azulado', 'Anaranjado', 'Morado']
    
    mazo = []

    # 18 cartas numéricas de cada color del lado claro (1 a 9)
    for i in range(1, 10):
        for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
            mazo.append(Carta(color_claro, i, color_oscuro, i))
            mazo.append(Carta(color_claro, i, color_oscuro, i))  # Agregar dos de cada número

    # 8 cartas de acción Toma 1 del lado claro
    for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
        mazo.append(Carta(color_claro, "Toma 1", color_oscuro, "Toma 5", tipo_accion="Toma 1"))

    # 8 cartas Reversa del lado claro
    for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
        mazo.append(Carta(color_claro, "Reversa", color_oscuro, "Reversa", tipo_accion="Reversa"))

    # 8 cartas Salta del lado claro
    for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
        mazo.append(Carta(color_claro, "Salta", color_oscuro, "Salta a todos", tipo_accion="Salta"))

    # 8 cartas Flip del lado claro
    for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
        mazo.append(Carta(color_claro, "Flip", color_oscuro, "Flip", tipo_accion="Flip"))

    # 4 cartas de comodín multicolor
    for _ in range(4):
        mazo.append(Carta("Multicolor", "Comodín", "Multicolor", "Comodín", tipo_accion="Comodín"))

    # 4 cartas de comodín Toma 2 del lado claro y Toma un color del lado oscuro
    for _ in range(4):
        mazo.append(Carta("Multicolor", "Toma 2", "Multicolor", "Toma un color", tipo_accion="Comodín"))

    random.shuffle(mazo)  # Mezclar el mazo
    return mazo
