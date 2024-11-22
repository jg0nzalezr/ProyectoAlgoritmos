import random

class JugadorIA:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def agregar_cartas(self, cartas):
        """Agrega cartas a la mano del jugador."""
        self.mano.extend(cartas)

    def jugar_carta(self, carta):
        """Juega una carta específica de la mano."""
        if carta in self.mano:
            self.mano.remove(carta)

    def seleccionar_jugada(self, carta_actual, color_actual, lado_oscuro_activo):
        """
        Selecciona la mejor carta para jugar acorde a las reglas del juego y la situación actual.
        La lógica prioriza:
        1. Cartas de acción que afecten al oponente (como "Toma 2", "Reversa", etc.).
        2. Cartas que coincidan en color o valor.
        3. Cartas numéricas si no hay acciones disponibles.
        """
        cartas_validas = []
        mejor_carta = None

        # Buscar cartas válidas
        for carta in self.mano:
            if lado_oscuro_activo:
                if (carta.color_oscuro == color_actual or
                    carta.valor_oscuro == carta_actual.valor_oscuro or
                    carta.tipo_accion == carta_actual.tipo_accion or
                    carta.tipo_accion == "Comodín"):
                    cartas_validas.append(carta)
            else:
                if (carta.color_claro == color_actual or
                    carta.valor_claro == carta_actual.valor_claro or
                    carta.tipo_accion == carta_actual.tipo_accion or
                    carta.tipo_accion == "Comodín"):
                    cartas_validas.append(carta)

        # Si no hay cartas válidas, debe robar
        if not cartas_validas:
            return "ROBAR"

        # Priorizar cartas de acción
        for carta in cartas_validas:
            if carta.tipo_accion in ["Toma 2", "Toma 5", "Salta", "Reversa", "Flip", "Comodín"]:
                mejor_carta = carta
                break

        # Si no hay cartas de acción, priorizar cartas del mismo color
        if mejor_carta is None:
            for carta in cartas_validas:
                if lado_oscuro_activo and carta.color_oscuro == color_actual:
                    mejor_carta = carta
                    break
                elif not lado_oscuro_activo and carta.color_claro == color_actual:
                    mejor_carta = carta
                    break

        # Si no hay cartas del mismo color, priorizar por número o acción general
        if mejor_carta is None:
            mejor_carta = cartas_validas[0]  # Seleccionar la primera carta válida como última opción

        return mejor_carta

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
        return color_predominante

    def evaluar_estado_juego(self, carta_actual, color_actual, lado_oscuro_activo):
        """
        Evalúa el estado del juego y calcula la probabilidad de ganar.
        Este método puede usarse para mejorar las decisiones estratégicas del jugador IA.
        """
        # Calcular cartas jugables
        cartas_jugables = []
        for carta in self.mano:
            if lado_oscuro_activo:
                if (carta.color_oscuro == color_actual or
                    carta.valor_oscuro == carta_actual.valor_oscuro or
                    carta.tipo_accion == carta_actual.tipo_accion or
                    carta.tipo_accion == "Comodín"):
                    cartas_jugables.append(carta)
            else:
                if (carta.color_claro == color_actual or
                    carta.valor_claro == carta_actual.valor_claro or
                    carta.tipo_accion == carta_actual.tipo_accion or
                    carta.tipo_accion == "Comodín"):
                    cartas_jugables.append(carta)

        # Calcular probabilidad de ganar (cartas jugables / total de cartas)
        probabilidad_ganar = len(cartas_jugables) / len(self.mano) if self.mano else 0
        return probabilidad_ganar
