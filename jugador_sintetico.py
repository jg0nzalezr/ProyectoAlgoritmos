import random

class JugadorIA:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def agregar_cartas(self, cartas):
        """Agrega cartas a la mano del jugador."""
        self.mano.extend(cartas)
        print(f"[DEBUG] {self.nombre} ha recibido cartas: {[str(c) for c in cartas]}")

    def jugar_carta(self, carta):
        """Juega una carta específica de la mano."""
        if carta in self.mano:
            self.mano.remove(carta)
            print(f"[DEBUG] {self.nombre} ha jugado la carta: {carta}")
        else:
            raise ValueError(f"[ERROR] La carta {carta} no está en la mano de {self.nombre}.")

    def seleccionar_jugada(self, carta_actual, color_actual, lado_oscuro_activo):
        """
        Selecciona la mejor carta para jugar acorde a las reglas del juego y la situación actual.
        """
        print(f"\n[DEBUG] Turno de {self.nombre} (Jugador IA)")
        print(f"[DEBUG] Carta en mesa: {carta_actual}")
        print(f"[DEBUG] Color actual: {color_actual}")
        print(f"[DEBUG] Lado oscuro activo: {lado_oscuro_activo}")
        print(f"[DEBUG] Cartas en la mano del jugador IA: {[str(c) for c in self.mano]}")

        cartas_no_comodines = []
        cartas_comodines = []

        # Buscar cartas jugables en la mano
        for carta in self.mano:
            if lado_oscuro_activo:
                if carta.color_oscuro == color_actual or carta.valor_oscuro == carta_actual.valor_oscuro:
                    cartas_no_comodines.append(carta)
                elif carta.tipo_accion == "Comodín":
                    cartas_comodines.append(carta)
            else:
                if carta.color_claro == color_actual or carta.valor_claro == carta_actual.valor_claro:
                    cartas_no_comodines.append(carta)
                elif carta.tipo_accion == "Comodín":
                    cartas_comodines.append(carta)

        # Depuración: Mostrar cartas jugables separadas
        print(f"[DEBUG] Cartas no comodines jugables: {[str(c) for c in cartas_no_comodines]}")
        print(f"[DEBUG] Cartas comodines jugables: {[str(c) for c in cartas_comodines]}")

        # Priorizar cartas no comodines
        if cartas_no_comodines:
            mejor_carta = cartas_no_comodines[0]  # Jugar la primera carta válida
            print(f"[DEBUG] Jugando carta no comodín: {mejor_carta}")
            return mejor_carta

        # Si solo hay comodines disponibles, jugarlos como última opción
        if cartas_comodines:
            mejor_carta = cartas_comodines[0]  # Jugar el primer comodín disponible
            print(f"[DEBUG] Jugando carta comodín como última opción: {mejor_carta}")
            return mejor_carta

        # Si no hay cartas jugables, devolver "ROBAR"
        print("[DEBUG] No hay cartas válidas. Decisión: Robar.")
        return "ROBAR"

    def elegir_color_comodin(self):
        """
        Decide qué color elegir al jugar un comodín.
        Elegirá el color predominante en su mano para maximizar sus probabilidades de ganar.
        """
        colores = {"Azul": 0, "Verde": 0, "Rojo": 0, "Amarillo": 0}
        for carta in self.mano:
            if carta.color_claro in colores:
                colores[carta.color_claro] += 1

        # Elegir el color con mayor cantidad de cartas
        color_predominante = max(colores, key=colores.get)
        print(f"[DEBUG] Color elegido para comodín: {color_predominante}")
        return color_predominante

    def __str__(self):
        """Devuelve el nombre del jugador para representarlo como texto."""
        return self.nombre
