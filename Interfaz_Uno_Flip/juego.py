from mazo import crear_mazo
from ascii_art import mostrar_bienvenida, mostrar_carta_mesa

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

    def configurar_juego(self):
        print("\nConfiguración del juego:")
        num_jugadores = int(input("Ingrese el número de jugadores (2-10): "))
        if 2 <= num_jugadores <= 10:
            for i in range(num_jugadores):
                nombre_jugador = input(f"Ingrese el nombre del jugador {i + 1}: ")
                self.jugadores.append(nombre_jugador)
                self.manos_jugadores[nombre_jugador] = []
                self.puntuaciones[nombre_jugador] = 0
            print("\nJugadores configurados:")
            for jugador in self.jugadores:
                print(f"- {jugador}")
            print("\nEl juego está listo para comenzar.")
        else:
            print("Número de jugadores inválido. El juego debe tener entre 2 y 10 jugadores.")

    def repartir_cartas(self):
        """ Reparte 7 cartas a cada jugador """
        for jugador in self.jugadores:
            for _ in range(7):
                carta = self.mazo_claro.pop()
                self.manos_jugadores[jugador].append(carta)
            print(f"{jugador} ha recibido 7 cartas.")

    def preparar_mazo(self):
        """ Prepara la pila de cartas para tomar y tira la primera carta """
        self.pila_para_tomar = self.mazo_claro[:]
        primera_carta = self.pila_para_tomar.pop()
        self.pila_para_tirar.append(primera_carta)
        self.color_actual = primera_carta.color_claro
        self.valor_actual = primera_carta.valor_claro
        mostrar_carta_mesa(self.lado_oscuro_activo, self.pila_para_tirar)

    def iniciar_juego(self):
        """ Inicia el ciclo principal del juego """
        mostrar_bienvenida()
        self.configurar_juego()
        self.repartir_cartas()
        self.preparar_mazo()
