def mostrar_bienvenida():
    """ Muestra el arte ASCII de bienvenida """
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

def ascii_jugar_carta():
    """ Devuelve el arte ASCII de jugar una carta """
    return """
    ╔══════════════════════╗
    ║  ¡HAS ELEGIDO JUGAR! ║
    ╚══════════════════════╝
    """

def ascii_robar_carta():
    """ Devuelve el arte ASCII de robar una carta """
    return """
    ╔═════════════════════╗
    ║   ¡HAS ROBADO UNA!  ║
    ╚═════════════════════╝
    """

def mostrar_carta_mesa(color, valor):
    """ Muestra la carta en la mesa usando arte ASCII """
    ascii_art = f"""
    ╔════════════════════════╗
    ║    {color.upper():^13} ║
    ║                        ║
    ║       {valor:^7}       ║
    ║                        ║
    ╚════════════════════════╝
    """
    print(ascii_art)
