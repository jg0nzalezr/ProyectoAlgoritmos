# carta.py
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
