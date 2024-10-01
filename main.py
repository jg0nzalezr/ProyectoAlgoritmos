class JuegoUNOFlip:
    def __init__(self):
        self.jugadores = []
        self.jugador_actual = 0
        self.mazo_claro = []  # Lado claro
        self.mazo_oscuro = []  # Lado oscuro
        self.pila_para_tirar = []  # Pila para tirar
        self.pila_para_tomar = []  # Pila para tomar
        self.lado_oscuro_activo = False  # Falso = lado claro, Verdadero = lado oscuro

    def mostrar_bienvenida(self):
        print("¡Bienvenido a UNO Flip!")
        print("Reglas:")
        print("1. El juego comienza en el lado claro de las cartas.")
        print("2. Cada vez que alguien juega una carta Flip, el mazo y las cartas se voltean al lado oscuro.")
        print("3. Las cartas de acción tienen diferentes efectos según el lado del mazo.")
        print("4. Gana el primer jugador que se deshaga de todas sus cartas.")

    def configurar_juego(self):
        print("\nConfiguración del juego:")
        num_jugadores = int(input("Ingrese el número de jugadores (2-10): "))
        if 2 <= num_jugadores <= 10:
            for i in range(num_jugadores):
                nombre_jugador = input(f"Ingrese el nombre del jugador {i + 1}: ")
                self.jugadores.append(nombre_jugador)
            print("\nJugadores configurados:")
            for jugador in self.jugadores:
                print(f"- {jugador}")
            print("\nEl juego está listo para comenzar.")
        else:
            print("Número de jugadores inválido. El juego debe tener entre 2 y 10 jugadores.")

    def voltear_mazo(self):
        # Cambia entre el lado claro y oscuro
        self.lado_oscuro_activo = not self.lado_oscuro_activo
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        print(f"\n¡El mazo ha sido volteado! Ahora estás jugando en el lado {lado}.")

    def mostrar_mano_jugador(self, nombre_jugador):
        #Mostrar cartas del jugador
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        print(f"\nTurno de {nombre_jugador} (jugando con el lado {lado}).")
        print(f"[Mostrando cartas de {nombre_jugador}]")
        print("1. Carta")
        print("2. Carta")
        print("3. Carta")
        print("4. Carta")
        print("5. Carta")

    def turno_jugador(self, nombre_jugador):
        print(f"\nEs el turno de {nombre_jugador}.")
        self.mostrar_mano_jugador(nombre_jugador)
        accion = input("Elige una acción (1. Jugar carta, 2. Robar carta): ")
        if accion == '1':
            carta_elegida = int(input("Elige el número de la carta a jugar: "))
            #Si la carta es flip, se voleta el mazo (crear metodo para eso)
            #Se verifica si la carta es un flip
            if carta_elegida == 4:  # Solo para propósitos de demostración
                self.voltear_mazo()
            print(f"Has jugado la carta {carta_elegida}.")
        elif accion == '2':
            print("Has robado una carta.")
        else:
            print("Error, escoge una opción válida")

    def mostrar_ganador(self, nombre_jugador):
        print(f"\n¡Felicidades {nombre_jugador}! Has ganado!")

    def iniciar_juego(self):
        self.mostrar_bienvenida()
        self.configurar_juego()
        juego_terminado = False
        while not juego_terminado:
            nombre_jugador_actual = self.jugadores[self.jugador_actual]
            self.turno_jugador(nombre_jugador_actual)
            # Aquí se agregará la lógica para verificar si el juego ha terminado
            self.jugador_actual = (self.jugador_actual + 1) % len(self.jugadores)

#main
if __name__ == "__main__":
    juego = JuegoUNOFlip()
    juego.iniciar_juego()
