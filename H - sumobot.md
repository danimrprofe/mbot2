# H. SumoBot

Los SumoBots utilizan el sensor de ultrasonidos para buscar y destruir al otro vehículo robótico en el ring de Sumo, mientras usan el sensor de color para detectar el borde blanco y evitar caerse por el borde.

## H1. Código Sumo Básico

Las acciones fundamentales de un SumoBot son:

- Espera de seguridad: Tres segundos de pausa antes de cualquier acción (norma común en competiciones).
- Entrada al ring: Avanzar 20 cm desde el borde inicial.
- Búsqueda: Girar hasta que el sensor de ultrasonidos localice al oponente (a menos de 80 cm).
- Ataque: Conducir a máxima velocidad hacia el otro vehículo.
- Supervivencia: Si se detecta el borde blanco (valor de reflectancia alto), detenerse, retroceder y girar para volver a buscar al oponente.

Este código utiliza la lógica de detección de línea blanca (fondo oscuro, borde claro) y detección de objetos.

```python
#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#VARIABLES GLOBALES----------------------------
distancia = 300
L2 = 0
L1 = 0
R1 = 0
R2 = 0
hay_linea = False

#FUNCIONES-------------------------------------
def obtener_valores():
    

    # Obtener distancia del sensor de ultrasonidos
    distancia = cpi.ultrasonic2.get(index=1)

    # Obtener valores de escala de grises de los 4 sensores (L=Izquierda, R=Derecha)
    L2 = cpi.quad_rgb_sensor.get_gray('l2', index = 1)
    L1 = cpi.quad_rgb_sensor.get_gray('l1', index = 1)
    R1 = cpi.quad_rgb_sensor.get_gray('r1', index = 1)
    R2 = cpi.quad_rgb_sensor.get_gray('r2', index = 1)

    # Detectar si alguno de los sensores está sobre una línea (umbral de 50)
    
    hay_linea = (L2 < 50) or (L1 < 50) or (R1 < 50) or (R2 < 50)
    
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
        cpi.console.println("LINEA NEGRA!!!")
        cpi.led.show('yellow yellow yellow yellow yellow')
        cpi.mbot2.EM_stop(port = "all")
        # Maniobra de supervivencia: retroceder y girar
        cpi.mbot2.straight(-10, speed = 40)
        cpi.mbot2.turn(90, speed = 40)

    elif distancia < 40:
        # ¡Oponente localizado!
        
        cpi.led.show('red red red red red')
        cpi.mbot2.forward(speed = 100) # Ataque a máxima velocidad

    else:
        
        # Buscando al oponente
        cpi.led.show('green green green green green')
        cpi.mbot2.turn_left(speed = 30) # Girar para localizar
```

🔍 Explicación de las mejoras añadidas:

- encontrado = True: He añadido esta "bandera" para que, una vez que el robot detecta al oponente, no deje de avanzar aunque lo pierda de vista un milisegundo, asegurando un empuje constante.
- linea_negra=False: Es crucial en la función obtener_valores. En un ring de sumo, el suelo es negro y el borde es blanco, por lo que buscamos valores de reflectancia altos (mayores a 50).
- Velocidad de ataque: He subido la velocidad en el ataque (forward(speed = 100)) para maximizar la fuerza de empuje.

## H2. Mejoras

- **No pierdas tiempo** moviéndote hacia adelante al principio antes de empezar a buscar al otro vehículo.
- La primera vez, **escanea a izquierda y derecha** solo hasta 90 grados.
- **Detente cada 10 grados** al escanear para asegurarte de que el escaneo detecta el vehículo (moverse demasiado rápido no funciona).
- Usa el **sensor de movimiento** para detectar una colisión o si el robot ha sido levantado del suelo (inclinación lateral o frontal - _pitch_ o _roll_) y responde a ello (ver Apéndice 1).
- Si el movimiento se detiene durante **x segundos**, utiliza una serie de movimientos rápidos de las ruedas (por ejemplo, hacia adelante y hacia atrás) para intentar liberarte.
- Utiliza una **estrategia diferente**:
  - Sigue la línea blanca por el exterior (usa L2 o R2).
  - Conduce hacia un lugar aleatorio.
  - Conduce hacia adelante hasta la línea blanca, gira y ve aleatoriamente a otro lugar hasta encontrar la línea blanca.
- Utiliza **más de un sensor de ultrasonidos** en diferentes ángulos.
