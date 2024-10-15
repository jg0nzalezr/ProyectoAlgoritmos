from mazo import crear_mazo
from acciones import aplicar_efecto_accion
from ascii_art import mostrar_bienvenida, mostrar_carta_jugada, mostrar_accion_jugar, mostrar_accion_robar, mostrar_flip

class JuegoUNOFlip:
    def __init__(self):
        self.jugadores = []
        self.jugador_actual = 0
        self.mazo_claro = crear_mazo()  # Crear el mazo con los lados claros y oscuros
        self.pila_para_tirar = []  # Pila para tirar
        self.pila_para_tomar = []  # Pila para tomar
        self.lado_oscuro_activo = False  # Comienza con el lado claro
        self.manos_jugadores = {}  # Cartas de cada jugador
        self.puntuaciones = {}  # Puntuaciones de cada jugador
        self.color_actual = None  # Color que está actualmente en juego
        self.valor_actual = None  # Valor que está actualmente en juego
        self.sentido_horario = True  # Controla la dirección del juego

    def mostrar_bienvenida(self):
        """Muestra la bienvenida con arte ASCII"""
        mostrar_bienvenida()

    def mostrar_carta_mesa(self):
        """ Muestra la carta que está en la pila para tirar """
        if len(self.pila_para_tirar) > 0:
            carta_mesa = self.pila_para_tirar[-1]
            color = carta_mesa.color_claro if not self.lado_oscuro_activo else carta_mesa.color_oscuro
            valor = carta_mesa.valor_claro if not self.lado_oscuro_activo else carta_mesa.valor_oscuro
            mostrar_carta_jugada(color, valor)  # Muestra la carta en la mesa
        else:
            print("No hay cartas en la mesa.")

    def turno_jugador(self, nombre_jugador):
        """ Gestiona el turno de un jugador """
        print(f"\nEs el turno de {nombre_jugador}.")
        self.verificar_uno(nombre_jugador)
        self.mostrar_mano_jugador(nombre_jugador)

        accion_valida = False  # Variable para controlar si la acción fue válida

        while not accion_valida:
            accion = input("Elige una acción (1. Jugar carta, 2. Robar carta): ")
            if accion == '1':
                # Arte ASCII para "Jugar carta"
                mostrar_accion_jugar()
                carta_elegida = int(input("Elige el número de la carta a jugar: ")) - 1
                carta = self.manos_jugadores[nombre_jugador][carta_elegida]
                if self.puede_jugar(carta):
                    self.manos_jugadores[nombre_jugador].pop(carta_elegida)
                    if carta.tipo_accion:
                        aplicar_efecto_accion(self, carta)
                    self.color_actual = carta.color_claro if not self.lado_oscuro_activo else carta.color_oscuro
                    self.valor_actual = carta.valor_claro if not self.lado_oscuro_activo else carta.valor_oscuro

                    # Mostrar carta jugada en ASCII
                    mostrar_carta_jugada(self.color_actual, self.valor_actual)
                    accion_valida = True
                else:
                    print("No puedes jugar esa carta, intenta con otra carta o roba una carta.")
            elif accion == '2':
                # Arte ASCII para "Robar carta"
                mostrar_accion_robar()
                self.tomar_cartas(1)
                self.mostrar_carta_mesa()  # Muestra la carta en la mesa después de tomar
                accion_valida = True
            else:
                print("Acción no válida, intenta de nuevo.")

    def tomar_cartas(self, cantidad):
        """ Hace que el siguiente jugador tome una cantidad de cartas """
        siguiente_jugador = self.obtener_siguiente_jugador()
        for _ in range(cantidad):
            if len(self.pila_para_tomar) == 0:
                self.reiniciar_pila_para_tomar()
            carta = self.pila_para_tomar.pop()
            self.manos_jugadores[siguiente_jugador].append(carta)
        print(f"{siguiente_jugador} ha tomado {cantidad} cartas.")
        self.mostrar_carta_mesa()  # Muestra la carta en la mesa después de tomar

    def obtener_siguiente_jugador(self):
        """ Devuelve el nombre del siguiente jugador según la dirección del juego """
        if self.sentido_horario:
            return self.jugadores[(self.jugador_actual + 1) % len(self.jugadores)]
        else:
            return self.jugadores[(self.jugador_actual - 1) % len(self.jugadores)]

    def reiniciar_pila_para_tomar(self):
        """ Rebaraja la pila de cartas tiradas si la pila para tomar se acaba """
        if len(self.pila_para_tirar) > 1:
            ultima_carta = self.pila_para_tirar.pop()  # Dejar la última carta
            self.pila_para_tomar = self.pila_para_tirar[:]
            random.shuffle(self.pila_para_tomar)
            self.pila_para_tirar = [ultima_carta]
            print("La pila para tomar ha sido rebarajada.")

    def voltear_mazo(self):
        """Voltea el mazo con arte ASCII"""
        self.lado_oscuro_activo = not self.lado_oscuro_activo
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        mostrar_flip(lado)  # Mostrar arte ASCII del flip
        print(f"\n¡El mazo ha sido volteado! Ahora estás jugando en el lado {lado}.")

    def mostrar_mano_jugador(self, nombre_jugador):
        """ Muestra las cartas de la mano de un jugador """
        mano = self.manos_jugadores[nombre_jugador]
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        print(f"\nTurno de {nombre_jugador} (jugando con el lado {lado}).")
        for idx, carta in enumerate(mano):
            print(f"{idx + 1}. {carta.__str__(self.lado_oscuro_activo)}")

    def verificar_uno(self, nombre_jugador):
        """ Verifica si el jugador debe decir UNO cuando tiene una sola carta """
        if len(self.manos_jugadores[nombre_jugador]) == 2:
            decir_uno = input(f"{nombre_jugador}, ¿quieres decir UNO? (s/n): ")
            if decir_uno.lower() != 's':
                print(f"{nombre_jugador} no dijo UNO a tiempo. Roba dos cartas.")
                self.tomar_cartas(2)

    def verificar_ganador(self):
        """ Verifica si algún jugador ha ganado """
        for jugador in self.jugadores:
            if len(self.manos_jugadores[jugador]) == 0:
                return jugador
        return None

    def preparar_mazo(self):
        """ Prepara la pila de cartas para tomar y tira la primera carta """
        # Pasar todas las cartas restantes a la pila para tomar
        self.pila_para_tomar = self.mazo_claro[:]
        random.shuffle(self.pila_para_tomar)
        primera_carta = self.pila_para_tomar.pop()
        self.pila_para_tirar.append(primera_carta)
        self.color_actual = primera_carta.color_claro if not self.lado_oscuro_activo else primera_carta.color_oscuro
        self.valor_actual = primera_carta.valor_claro if not self.lado_oscuro_activo else primera_carta.valor_oscuro
        print(f"La primera carta en la pila para tirar es {primera_carta.__str__(self.lado_oscuro_activo)}.")

    def iniciar_juego(self):
        """ Inicia el ciclo principal del juego """
        self.mostrar_bienvenida()
        self.configurar_juego()
        self.repartir_cartas()  # Repartir cartas a los jugadores
        self.preparar_mazo()  # Preparar la pila para tomar y la pila para tirar

        juego_terminado = False
        while not juego_terminado:
            nombre_jugador_actual = self.jugadores[self.jugador_actual]
            self.turno_jugador(nombre_jugador_actual)
            ganador = self.verificar_ganador()
            if ganador:
                print(f"\n¡Felicidades {ganador}! Has ganado esta ronda.")
                juego_terminado = True
            self.jugador_actual = (self.jugador_actual + 1) % len(self.jugadores)
