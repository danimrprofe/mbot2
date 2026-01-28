#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#VARIABLES GLOBALES----------------------------
distancia = 300
L2 = 0
L1 = 0
R1 = 0
R2 = 0
hay_linea = 0

#FUNCIONES-------------------------------------
def obtener_valores(mostrar=True, linea_negra=True):
    global distancia, L1, L2, R1, R2, hay_linea

    # Obtener distancia del sensor de ultrasonidos
    distancia = cpi.ultrasonic2.get(index=1)

    # Obtener valores de escala de grises de los 4 sensores (L=Izquierda, R=Derecha)
    L2 = cpi.quad_rgb_sensor.get_gray('l2', index = 1)
    L1 = cpi.quad_rgb_sensor.get_gray('l1', index = 1)
    R1 = cpi.quad_rgb_sensor.get_gray('r1', index = 1)
    R2 = cpi.quad_rgb_sensor.get_gray('r2', index = 1)

    # Detectar si alguno de los sensores está sobre una línea (umbral de 50)
    if linea_negra:
        hay_linea = (L2 < 50) or (L1 < 50) or (R1 < 50) or (R2 < 50)
    else:
        hay_linea = (L2 > 50) or (L1 > 50) or (R1 > 50) or (R2 > 50)

    if mostrar:
        # Muestra los valores de los 4 sensores en la pantalla del CyberPi
        cpi.console.println(str(L2)+' '+str(L1)+' '+str(R1)+' '+str(R2) )
    return distancia, hay_linea

# --- PREPARACIÓN INICIAL ---
time.sleep(3) # Espera de seguridad de 3 segundos
encontrado = False
cpi.mbot2.straight(20, speed = 40) # Entrar 20 cm al ring

# --- BUCLE PRINCIPAL DE COMBATE ---
while True:
    # Obtenemos valores. black_line=False busca líneas blancas (reflectancia alta)
    distancia, hay_linea = obtener_valores()

    if hay_linea:
        # ¡Peligro! Borde del ring detectado (línea blanca)
        encontrado = False
        cpi.led.show('yellow yellow yellow yellow yellow')
        cpi.mbot2.EM_stop(port = "all")
        # Maniobra de supervivencia: retroceder y girar
        cpi.mbot2.straight(-10, speed = 40)
        cpi.mbot2.turn(90, speed = 40)

    elif distancia < 80 or encontrado:
        # ¡Oponente localizado!
        encontrado = True
        cpi.led.show('red red red red red')
        cpi.mbot2.forward(speed = 100) # Ataque a máxima velocidad

    else:
        # Buscando al oponente
        cpi.led.show('green green green green green')
        cpi.mbot2.turn_left(speed = 30) # Girar para localizar