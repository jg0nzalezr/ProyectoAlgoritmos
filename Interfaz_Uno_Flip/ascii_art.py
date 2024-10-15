# ascii_art.py

def mostrar_bienvenida():
    """Muestra el menú principal con arte ASCII"""
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

def mostrar_carta_jugada(color, valor):
    """Muestra la carta jugada en arte ASCII"""
    ascii_art = f"""
    ╔════════════════════════╗
    ║    {color.upper():^13} ║
    ║                        ║
    ║       {valor:^7}       ║
    ║                        ║
    ╚════════════════════════╝
    """
    print(ascii_art)

def mostrar_accion_jugar():
    """Muestra en arte ASCII que el jugador ha elegido jugar una carta"""
    ascii_jugar_carta = """
    ╔══════════════════════╗
    ║  ¡HAS ELEGIDO JUGAR! ║
    ╚══════════════════════╝
    """
    print(ascii_jugar_carta)

def mostrar_accion_robar():
    """Muestra en arte ASCII que el jugador ha elegido robar una carta"""
    ascii_robar_carta = """
    ╔═════════════════════╗
    ║   ¡HAS ROBADO UNA!  ║
    ╚═════════════════════╝
    """
    print(ascii_robar_carta)

def mostrar_flip(lado):
    """Muestra en arte ASCII que ha ocurrido un Flip"""
    ascii_flip = f"""
    ╔═════════════════════╗
    ║      ¡FLIP!         ║
    ║   Cambiando al      ║
    ║    lado {lado.upper():^9}   ║
    ╚═════════════════════╝
    """
    print(ascii_flip)
