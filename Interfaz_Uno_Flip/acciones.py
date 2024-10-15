def aplicar_efecto_accion(carta, juego):
    """ Aplica el efecto de las cartas de acción """
    siguiente_jugador = juego.obtener_siguiente_jugador()
    
    if carta.tipo_accion == "Toma 1":
        print(f"El siguiente jugador {siguiente_jugador} debe tomar una carta y pierde su turno.")
        juego.tomar_cartas(1)
        juego.saltar_turno()
    elif carta.tipo_accion == "Toma 2":
        print(f"El siguiente jugador {siguiente_jugador} debe tomar dos cartas y pierde su turno.")
        juego.tomar_cartas(2)
        juego.saltar_turno()
    elif carta.tipo_accion == "Toma 5":
        print(f"El siguiente jugador {siguiente_jugador} debe tomar cinco cartas y pierde su turno.")
        juego.tomar_cartas(5)
        juego.saltar_turno()
    elif carta.tipo_accion == "Reversa":
        print("El sentido del juego se ha invertido.")
        juego.sentido_horario = not juego.sentido_horario
    elif carta.tipo_accion == "Salta":
        print(f"El siguiente jugador {siguiente_jugador} pierde su turno.")
        juego.saltar_turno()
    elif carta.tipo_accion == "Salta a todos":
        print(f"Todos los jugadores pierden su turno, el jugador que tiró la carta juega de nuevo.")
        juego.saltar_turno_para_todos()
    elif carta.tipo_accion == "Comodín":
        juego.cambiar_color()
    elif carta.tipo_accion == "Flip":
        juego.voltear_mazo()
