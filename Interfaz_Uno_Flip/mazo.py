# mazo.py
from carta import Carta
import random

def crear_mazo():
    colores_claros = ['Azul', 'Verde', 'Rojo', 'Amarillo']
    colores_oscuros = ['Rosa', 'Verde Azulado', 'Anaranjado', 'Morado']
    
    mazo = []

    # 18 cartas numéricas de cada color del lado claro (1 a 9)
    for i in range(1, 10):
        for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
            mazo.append(Carta(color_claro, i, color_oscuro, i))
            mazo.append(Carta(color_claro, i, color_oscuro, i))  # Agregar dos de cada número

    # Cartas de acción
    for color_claro, color_oscuro in zip(colores_claros, colores_oscuros):
        mazo.append(Carta(color_claro, "Toma 1", color_oscuro, "Toma 5", tipo_accion="Toma 1"))
        mazo.append(Carta(color_claro, "Reversa", color_oscuro, "Reversa", tipo_accion="Reversa"))
        mazo.append(Carta(color_claro, "Salta", color_oscuro, "Salta a todos", tipo_accion="Salta"))
        mazo.append(Carta(color_claro, "Flip", color_oscuro, "Flip", tipo_accion="Flip"))

    # Comodines
    for _ in range(4):
        mazo.append(Carta("Multicolor", "Comodín", "Multicolor", "Comodín", tipo_accion="Comodín"))
        mazo.append(Carta("Multicolor", "Toma 2", "Multicolor", "Toma un color", tipo_accion="Comodín"))

    random.shuffle(mazo)  # Mezclar el mazo
    return mazo
