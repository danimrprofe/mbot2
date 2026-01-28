import cyberpi as cpi
import time

# --- VARIABLES DE ESTADO ---
distancia_ataque = 50
distancia_embestida = 20

vel_embestida = 100
vel_ataque = 50

objetivo_avistado = False
objetivo_delante = False

def atacar():
    # Oponente a la vista (blanco/aire libre)
    cpi.console.clear()
    cpi.console.println("OPONENTE DETECTADO")
    cpi.audio.play("angry")
    cpi.led.on(0, 0, 255) 
    
    cpi.mbot2.drive_power(vel_ataque, vel_ataque)   # Aproximación controlada
    
def embestir():    
    cpi.console.clear()
    cpi.console.println("EMBISTIENDO")
    cpi.audio.play("angry")
    cpi.led.on(0, 0, 255) 
    cpi.mbot2.drive_power(vel_embestida, vel_embestida) # Embestida final
    

def detectar_objetivo():

    distancia = cpi.ultrasonic2.get(index=1)
    if distancia < distancia_embestida:
        objetivo_delante = True
        objetivo_avistado = False
    elif distancia < distancia_ataque:
        objetivo_avistado = True
        objetivo_delante = False
    else:
        objetivo_avistado = False
        objetivo_delante = False


        
def buscar_linea():
    L1, L2, R1, R2, hay_linea
    
    # Sensores de escala de grises
    L2 = cpi.quad_rgb_sensor.get_gray('l2', index = 1)
    L1 = cpi.quad_rgb_sensor.get_gray('l1', index = 1)
    R1 = cpi.quad_rgb_sensor.get_gray('r1', index = 1)
    R2 = cpi.quad_rgb_sensor.get_gray('r2', index = 1)

    # Detectar borde negro (valores bajos)
    
    hay_linea = (L2 < 40) or (L1 < 40) or (R1 < 40) or (R2 < 40)
    if hay_linea:
        cpi.console.clear()
        cpi.console.println("LINEA NEGRA DETECTADA")
        cpi.audio.play("buzzing")
        cpi.led.on(255, 0, 0) 
    
    # Formato compatible con CyberPi
    cpi.console.println("{} {} | {} {}".format(L2, L1, R1, R2))
    return hay_linea

def maniobra_escapar():
    # Maniobra de escape al tocar negro
    cpi.mbot2.EM_stop(port = "all")
    cpi.mbot2.straight(-15, speed = 60)
    cpi.mbot2.turn(120, speed = 50)

# --- BUCLE PRINCIPAL ---
cpi.console.clear()
cpi.console.println("SUMOBOT")
cpi.console.println("Pulsa el TRIANGULO para comenzar.")

while True:
    # 1. CONTROL POR BOTONES (A para PARAR, B para EMPEZAR)

    if cpi.controller.is_press('b'):
        if not ejecutando: # Solo si no estaba ya funcionando
            ejecutando = True
            cpi.console.clear()
            cpi.console.println("MODO: COMBATE (B)")
            cpi.audio.play("happy")
            # Salida inicial al ring
            cpi.mbot2.straight(15, speed = 40)
        time.sleep(0.2)

    if cpi.controller.is_press('a'):
        if ejecutando: # Solo si estaba funcionando
            ejecutando = False
            cpi.console.clear()
            cpi.console.println("MODO: STOP (A)")
            cpi.audio.play("sad")
            cpi.mbot2.EM_stop(port = "all")
        time.sleep(0.2)

    # 2. LÓGICA DE MOVIMIENTO
    if ejecutando:

        if buscar_linea():
            maniobra_escapar()
        elif detectar_objetivo():
            if objetivo_delante:
                embestir()
            elif objetivo_avistado:
                atacar()
        else:
            # Buscando en el área blanca
            cpi.led.on(255, 255, 255) 
            cpi.mbot2.turn_left(speed = 40)
            
    else:
        # Asegurar parada total si ejecutando es False
        cpi.mbot2.EM_stop(port = "all")
        cpi.led.on(0, 50, 0)