# G. Detectar y Seguir una Línea

El sensor Quad RGB (sensor de color) nos permite:

- Detectar y seguir líneas
- Identificar colores y reaccionar ante ellos de diferentes maneras.

Prueba el sensor con este código pasando el mBot2 sobre una línea negra en un fondo blanco.

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

#ESPERAR PARA EMPEZAR--------------------------
cpi.console.println('Pulsa A')
while not cpi.controller.is_press('a'):
    cpi.led.on(255,0,0)
    cpi.led.on(0,255,0)

#BUCLE PRINCIPAL-------------------------------
while True:
    obtener_valores(mostrar=True, linea_negra=True)
    time.sleep(0.1)
```

We can use the color sensor values to test whether the color sensor is on or off a black line.
• On a line will give a low reflectance value or off a line will give a high value.
• Assume for a start that if the reflected light value is less than 50% if we are on or near a black line.
• Place the mBot2 on the middle of the black line
• If both sensors L1 and R1 are on black – go straight ahead
• If only sensor L1 is on black – turn to the left
• If only sensor R1 is on black – turn to the right
First, test the code below without the motors driving. Then take off the comment # and try with the motors running.

Aquí tienes la explicación desglosada del código para el seguimiento de líneas, explicada paso a paso y de forma muy sencilla.
