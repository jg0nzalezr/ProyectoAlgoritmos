import random
from jugador_sintetico import JugadorIA


# Definir la clase para las cartas
class Carta:
    def __init__(self, color_claro, valor_claro, color_oscuro, valor_oscuro, tipo_accion=None):
        self.color_claro = color_claro
        self.valor_claro = valor_claro
        self.color_oscuro = color_oscuro
        self.valor_oscuro = valor_oscuro
        self.tipo_accion = tipo_accion  # Tipo de carta especial (Toma 1, Reversa, etc.)

    def __str__(self, lado_oscuro_activo=False):
        if lado_oscuro_activo:
            return f"{self.color_oscuro} {self.valor_oscuro} - {self.tipo_accion if self.tipo_accion else 'Número'}"
        else:
            return f"{self.color_claro} {self.valor_claro} - {self.tipo_accion if self.tipo_accion else 'Número'}"

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

# Definir la clase JuegoUNOFlip
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
        # Menú principal con arte ASCII
        print("""
 UUU   N   N   OOO        FFFFF  L      III  PPPP   
U   U  NN  N  O   O       F      L       I   P   P  
U   U  N N N  O   O       FFFF   L       I   PPPP   
U   U  N  NN  O   O       F      L       I   P      
 UUU   N   N   OOO        F      LLLLL  III  P     

**********************************************
*              UNO FLIP TIME!               *
**********************************************
        """)
        print("Reglas:")
        print("1. El juego comienza en el lado claro de las cartas.")
        print("2. Cada vez que alguien juega una carta Flip, el mazo y las cartas se voltean al lado oscuro.")
        print("3. Las cartas de acción tienen diferentes efectos según el lado del mazo.")
        print("4. Gana el primer jugador que se deshaga de todas sus cartas o alcance 500 puntos.")

    def configurar_juego(self):
        print("\nConfiguración del juego:")
        num_jugadores = int(input("Ingrese el número de jugadores (2-10): "))
        if 2 <= num_jugadores <= 10:
            for i in range(num_jugadores - 1):  # Un jugador humano menos
                nombre_jugador = input(f"Ingrese el nombre del jugador {i + 1}: ")
                self.jugadores.append(nombre_jugador)
                self.manos_jugadores[nombre_jugador] = []  # Inicializar la mano del jugador humano
                self.puntuaciones[nombre_jugador] = 0
            # Agregar jugador sintético
            jugador_ia = JugadorIA("Jugador Sintético")
            self.jugadores.append(jugador_ia)
            print("\nJugadores configurados:")
            for jugador in self.jugadores:
                print(f"- {jugador.nombre if isinstance(jugador, JugadorIA) else jugador}")  # Mostrar el nombre correctamente
            print("\nEl juego está listo para comenzar.")
        else:
            print("Número de jugadores inválido. El juego debe tener entre 2 y 10 jugadores.")

    def repartir_cartas(self):
        """Reparte 7 cartas a cada jugador."""
        for jugador in self.jugadores:
            for _ in range(7):  # Repartir 7 cartas
                carta = self.mazo_claro.pop()  # Sacar una carta del mazo
                if isinstance(jugador, JugadorIA):  # Si el jugador es IA
                    jugador.agregar_cartas([carta])  # Agregar la carta a su mano
                else:  # Si es un jugador humano
                    self.manos_jugadores[jugador].append(carta)
            print(f"{jugador.nombre if isinstance(jugador, JugadorIA) else jugador} ha recibido 7 cartas.")

    def puede_jugar(self, carta):
        """Verifica si una carta puede ser jugada según las reglas"""
        if carta.tipo_accion == "Comodín":
            return True  # Los comodines siempre se pueden jugar
        elif self.color_actual is not None:
            if self.lado_oscuro_activo:
                return (carta.color_oscuro == self.color_actual or carta.valor_oscuro == self.valor_actual or carta.tipo_accion == self.valor_actual)
            else:
                return (carta.color_claro == self.color_actual or carta.valor_claro == self.valor_actual or carta.tipo_accion == self.valor_actual)
        else:
            return False

    def obtener_cartas_jugables(self, jugador):
        """Devuelve una lista de cartas que el jugador puede jugar"""
        jugables = []
        for idx, carta in enumerate(self.manos_jugadores[jugador]):
            if self.puede_jugar(carta):
                jugables.append(f"{idx + 1}. {carta.__str__(self.lado_oscuro_activo)}")
        return jugables

    def obtener_siguiente_jugador(self):
        """Obtiene el índice del siguiente jugador según el sentido del juego"""
        if self.sentido_horario:
            return (self.jugador_actual + 1) % len(self.jugadores)
        else:
            return (self.jugador_actual - 1) % len(self.jugadores)

    def saltar_turno(self):
        """Salta el turno del siguiente jugador"""
        self.jugador_actual = self.obtener_siguiente_jugador()

    def aplicar_efecto_accion(self, carta):
        """Aplica el efecto de las cartas de acción"""
        siguiente_jugador_idx = self.obtener_siguiente_jugador()
        jugador_siguiente = self.jugadores[siguiente_jugador_idx]
        
        if carta.tipo_accion == "Toma 1":
            print(f"El siguiente jugador {jugador_siguiente} debe tomar una carta y pierde su turno.")
            self.tomar_cartas(jugador_siguiente, 1)
            self.saltar_turno()
        elif carta.tipo_accion == "Toma 2":
            print(f"El siguiente jugador {jugador_siguiente} debe tomar dos cartas y pierde su turno.")
            self.tomar_cartas(jugador_siguiente, 2)
            self.saltar_turno()
        elif carta.tipo_accion == "Toma 5":
            print(f"El siguiente jugador {jugador_siguiente} debe tomar cinco cartas y pierde su turno.")
            self.tomar_cartas(jugador_siguiente, 5)
            self.saltar_turno()
        elif carta.tipo_accion == "Reversa":
            print("El sentido del juego se ha invertido.")
            self.sentido_horario = not self.sentido_horario
        elif carta.tipo_accion == "Salta":
            print(f"El siguiente jugador {jugador_siguiente} pierde su turno.")
            self.saltar_turno()
        elif carta.tipo_accion == "Salta a todos":
            print(f"Todos los jugadores pierden su turno, el jugador {self.jugadores[self.jugador_actual]} juega de nuevo.")
            pass  # El jugador actual vuelve a jugar
        elif carta.tipo_accion == "Comodín":
            self.cambiar_color()
        elif carta.tipo_accion == "Flip":
            self.voltear_mazo()

    def tomar_cartas(self, jugador, cantidad):
        """Hace que el jugador indicado tome una cantidad de cartas"""
        for _ in range(cantidad):
            if len(self.pila_para_tomar) == 0:
                self.reiniciar_pila_para_tomar()
            carta = self.pila_para_tomar.pop()
            self.manos_jugadores[jugador].append(carta)
        print(f"{jugador} ha tomado {cantidad} cartas.")

    def mostrar_carta_mesa(self):
        """Muestra la carta que está en la pila para tirar"""
        if len(self.pila_para_tirar) > 0:
            carta_mesa = self.pila_para_tirar[-1]
            color = carta_mesa.color_claro if not self.lado_oscuro_activo else carta_mesa.color_oscuro
            valor = carta_mesa.valor_claro if not self.lado_oscuro_activo else carta_mesa.valor_oscuro
            ascii_art = f"""
            ╔════════════════════════╗
            ║    {color.upper():^13} ║
            ║                        ║
            ║       {valor:^7}       ║
            ║                        ║
            ╚════════════════════════╝
            """
            print(ascii_art)
        else:
            print("No hay cartas en la mesa.")

    def cambiar_color(self):
        """Cambia el color actual en juego"""
        nuevo_color = input("Elige un nuevo color (Azul, Verde, Rojo, Amarillo): ").capitalize()
        self.color_actual = nuevo_color
        print(f"El color ha cambiado a {nuevo_color}.")

    def voltear_mazo(self):
        """Voltea el mazo y las manos de los jugadores"""
        self.lado_oscuro_activo = not self.lado_oscuro_activo
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        
        # Arte ASCII para Flip
        ascii_flip = f"""
        ╔═════════════════════╗
        ║      ¡FLIP!         ║
        ║   Cambiando al      ║
        ║    lado {lado.upper():^9}   ║
        ╚═════════════════════╝
        """
        print(ascii_flip)
        print(f"\n¡El mazo ha sido volteado! Ahora estás jugando en el lado {lado}.")

    def reiniciar_pila_para_tomar(self):
        """Rebaraja la pila de cartas tiradas si la pila para tomar se acaba"""
        if len(self.pila_para_tirar) > 1:
            ultima_carta = self.pila_para_tirar.pop()  # Dejar la última carta
            self.pila_para_tomar = self.pila_para_tirar[:]
            random.shuffle(self.pila_para_tomar)
            self.pila_para_tirar = [ultima_carta]
            print("La pila para tomar ha sido rebarajada.")

    def verificar_uno(self, nombre_jugador):
        """Verifica si el jugador debe decir UNO cuando tiene una sola carta"""
        if len(self.manos_jugadores[nombre_jugador]) == 1:
            decir_uno = input(f"{nombre_jugador}, ¿quieres decir UNO? (s/n): ")
            if decir_uno.lower() != 's':
                print(f"{nombre_jugador} no dijo UNO a tiempo. Roba dos cartas.")
                self.tomar_cartas(nombre_jugador, 2)

    def verificar_ganador(self):
        """Verifica si algún jugador ha ganado"""
        for jugador in self.jugadores:
            if isinstance(jugador, JugadorIA):  # Si es el jugador IA
                if len(jugador.mano) == 0:  # Verifica su mano directamente
                    return jugador
            else:  # Si es un jugador humano
                if len(self.manos_jugadores[jugador]) == 0:  # Verifica la mano en el diccionario
                    return jugador
        return None

    def turno_jugador(self, nombre_jugador):
            """Gestiona el turno de un jugador (humano o IA)"""
            if isinstance(nombre_jugador, JugadorIA):
                print(f"\nEs el turno de {nombre_jugador.nombre}. (Jugador IA)")

                # Obtener la carta actual y el estado del juego
                carta_actual = self.pila_para_tirar[-1]
                lado_oscuro_activo = self.lado_oscuro_activo

                # Jugador IA selecciona la mejor jugada
                mejor_carta = nombre_jugador.seleccionar_jugada(carta_actual, self.color_actual, lado_oscuro_activo)

                if mejor_carta == "ROBAR":
                    print(f"{nombre_jugador.nombre} no tiene cartas jugables. Roba una carta.")
                    if len(self.pila_para_tomar) == 0:
                        self.reiniciar_pila_para_tomar()
                    carta_robada = self.pila_para_tomar.pop()
                    nombre_jugador.agregar_cartas([carta_robada])
                    print(f"{nombre_jugador.nombre} ha robado una carta.")
                else:
                    # Actualizar el estado del juego con la carta jugada
                    print(f"{nombre_jugador.nombre} ha jugado: {mejor_carta}")
                    self.pila_para_tirar.append(mejor_carta)  # Agregar la carta a la pila para tirar
                    nombre_jugador.jugar_carta(mejor_carta)  # Eliminar la carta de la mano del jugador IA
                    
                    # Manejar el efecto de la carta jugada
                    if mejor_carta.tipo_accion == "Comodín":
                        # Seleccionar automáticamente el color basado en la mano del jugador IA
                        nuevo_color = nombre_jugador.elegir_color_comodin()
                        self.color_actual = nuevo_color
                        print(f"{nombre_jugador.nombre} ha elegido el color: {nuevo_color}.")
                    elif mejor_carta.tipo_accion:
                        self.aplicar_efecto_accion(mejor_carta)
                    else:
                        # Actualizar color y valor actuales
                        self.color_actual = mejor_carta.color_claro if not self.lado_oscuro_activo else mejor_carta.color_oscuro
                        self.valor_actual = mejor_carta.valor_claro if not self.lado_oscuro_activo else mejor_carta.valor_oscuro
                    
                    # Arte ASCII para la carta jugada
                    color = mejor_carta.color_claro if not self.lado_oscuro_activo else mejor_carta.color_oscuro
                    valor = mejor_carta.valor_claro if not self.lado_oscuro_activo else mejor_carta.valor_oscuro
                    ascii_art = f"""
                    ╔════════════════════════╗
                    ║    {color.upper():^13} ║
                    ║                        ║
                    ║       {valor:^7}       ║
                    ║                        ║
                    ╚════════════════════════╝
                    """
                    print(ascii_art)
            else:
                # Turno del jugador humano
                print(f"\nEs el turno de {nombre_jugador}.")
                self.verificar_uno(nombre_jugador)
                self.mostrar_mano_jugador(nombre_jugador)

                accion_valida = False  # Variable para controlar si la acción fue válida

                while not accion_valida:
                    accion = input("Elige una acción (1. Jugar carta, 2. Robar carta): ")
                    if accion == '1':
                        # Arte ASCII para "Jugar carta"
                        ascii_jugar_carta = """
                        ╔══════════════════════╗
                        ║  ¡HAS ELEGIDO JUGAR! ║
                        ╚══════════════════════╝
                        """
                        print(ascii_jugar_carta)
                        try:
                            carta_elegida = int(input("Elige el número de la carta a jugar: ")) - 1
                            carta = self.manos_jugadores[nombre_jugador][carta_elegida]
                            if self.puede_jugar(carta):
                                self.manos_jugadores[nombre_jugador].pop(carta_elegida)
                                self.pila_para_tirar.append(carta)
                                if carta.tipo_accion:
                                    self.aplicar_efecto_accion(carta)
                                else:
                                    self.color_actual = carta.color_claro if not self.lado_oscuro_activo else carta.color_oscuro
                                    self.valor_actual = carta.valor_claro if not self.lado_oscuro_activo else carta.valor_oscuro
                                print(f"Has jugado la carta {carta.__str__(self.lado_oscuro_activo)}.")

                                # Arte ASCII para la carta jugada
                                color = carta.color_claro if not self.lado_oscuro_activo else carta.color_oscuro
                                valor = carta.valor_claro if not self.lado_oscuro_activo else carta.valor_oscuro
                                ascii_art = f"""
                                ╔════════════════════════╗
                                ║    {color.upper():^13} ║
                                ║                        ║
                                ║       {valor:^7}       ║
                                ║                        ║
                                ╚════════════════════════╝
                                """
                                print(ascii_art)
                                accion_valida = True
                            else:
                                print("No puedes jugar esa carta, intenta con otra carta o roba una carta.")
                        except (ValueError, IndexError):
                            print("Entrada inválida. Por favor selecciona una carta válida.")
                    elif accion == '2':
                        # Arte ASCII para "Robar carta"
                        ascii_robar_carta = """
                        ╔═════════════════════╗
                        ║   ¡HAS ROBADO UNA!  ║
                        ╚═════════════════════╝
                        """
                        print(ascii_robar_carta)
                        if len(self.pila_para_tomar) == 0:
                            self.reiniciar_pila_para_tomar()
                        self.tomar_cartas(nombre_jugador, 1)
                        accion_valida = True
                    else:
                        print("Acción no válida, intenta de nuevo.")



    def mostrar_mano_jugador(self, nombre_jugador):
        """Muestra las cartas de la mano de un jugador"""
        mano = self.manos_jugadores[nombre_jugador]
        lado = "oscuro" if self.lado_oscuro_activo else "claro"
        print(f"\nTurno de {nombre_jugador} (jugando con el lado {lado}).")
        for idx, carta in enumerate(mano):
            print(f"{idx + 1}. {carta.__str__(self.lado_oscuro_activo)}")

        # Mostrar cartas jugables
        cartas_jugables = self.obtener_cartas_jugables(nombre_jugador)
        if cartas_jugables:
            print("\nCartas que puedes jugar:")
            for jugable in cartas_jugables:
                print(jugable)
        else:
            print(f"{nombre_jugador} no tiene cartas jugables.")


    def preparar_mazo(self):
        """Prepara la pila de cartas para tomar y tira la primera carta"""
        # Pasar todas las cartas restantes a la pila para tomar
        self.pila_para_tomar = self.mazo_claro[:]
        random.shuffle(self.pila_para_tomar)
        while True:
            primera_carta = self.pila_para_tomar.pop()
            if primera_carta.tipo_accion != "Comodín" and primera_carta.tipo_accion != "Flip":
                break
            else:
                self.pila_para_tomar.insert(0, primera_carta)
                random.shuffle(self.pila_para_tomar)
        self.pila_para_tirar.append(primera_carta)
        self.color_actual = primera_carta.color_claro if not self.lado_oscuro_activo else primera_carta.color_oscuro
        self.valor_actual = primera_carta.valor_claro if not self.lado_oscuro_activo else primera_carta.valor_oscuro
        print(f"La primera carta en la pila para tirar es {primera_carta.__str__(self.lado_oscuro_activo)}.")


    def iniciar_juego(self):
        """Inicia el ciclo principal del juego"""
        self.mostrar_bienvenida()
        self.configurar_juego()
        self.repartir_cartas()  # Repartir cartas a los jugadores
        self.preparar_mazo()    # Preparar la pila para tomar y la pila para tirar

        juego_terminado = False
        while not juego_terminado:
            nombre_jugador_actual = self.jugadores[self.jugador_actual]
            self.turno_jugador(nombre_jugador_actual)
            ganador = self.verificar_ganador()
            if ganador:
                print(f"\n¡Felicidades {ganador}! Has ganado esta ronda.")
                juego_terminado = True
            else:
                # Avanzar al siguiente jugador
                self.jugador_actual = self.obtener_siguiente_jugador()

# Ejecutar el juego
if __name__ == "__main__":
    juego = JuegoUNOFlip()
    juego.iniciar_juego()