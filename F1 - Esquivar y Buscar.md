## F. Esquivar y Buscar

El sensor de ultrasonidos se utiliza para medir la distancia entre el mBot2 y cualquier objeto que tenga delante (hasta unos 200 cm).
Puede usarse para esquivar obstáculos o para buscar un objeto y moverse hacia él.

- La distancia mínima detectada es de **4 cm**.
- Las distancias menores dan una lectura de 300.

Prueba tu sensor de ultrasonidos con este código. Poner todo el código de lectura del sensor dentro de una **función** ayuda a mantener el bucle principal más limpio y organizado.

```python
#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#VARIABLES GLOBALES----------------------------
distancia = 300

#FUNCIONES-------------------------------------
def obtener_valores(output=True):
    global distancia
    # Lee la distancia del sensor ultrasónico en el puerto 1
    distancia = cpi.ultrasonic2.get(index=1)
    if mostrar:
        cpi.console.println( str(distancia) )
    time.sleep(0.1)

#ESPERAR PARA EMPEZAR--------------------------
cpi.console.println('Pulsa A')
while not cpi.controller.is_press('a'):
    cpi.led.on(255,0,0)
    cpi.led.on(0,255,0)

#BUCLE PRINCIPAL-------------------------------
while True:
    obtener_valores(output=True)
```

### Evitar Obstáculos

```python
#BUCLE PRINCIPAL---------------------------------
while True:
    # Obtenemos la distancia sin imprimirla en pantalla cada vez
    obtener_valores(output=False)

    if distancia < 10: # Prueba de colisión (menos de 10 cm)
        cpi.mbot2.EM_stop(port = "all")    # Parada de emergencia
        cpi.mbot2.straight(-5, speed = 50) # Retroceder 5 cm
        cpi.mbot2.turn(135, speed = 50)    # Girar 135 grados para esquivar
    else:
        cpi.mbot2.forward(speed = 50)      # Avanzar si el camino está libre
```

### Frenar cuando se está cerca de una colisión

Para evitar impactos bruscos, podemos programar el mBot2 para que reduzca su velocidad a medida que se acerca a un objeto. En lugar de detenerse de golpe, el robot ajustará su potencia proporcionalmente a la distancia detectada por el sensor de ultrasonidos.

```python
#BUCLE PRINCIPAL--------------------------------------
while True:
    obtener_valores(output=False)

    if distancia < 10: # Prueba de colisión
        cpi.mbot2.EM_stop(port = "all")    # Parar
        cpi.mbot2.straight(-5, speed = 50) # Retroceder 5cm
        cpi.mbot2.turn(135, speed = 50)    # Girar 135 grados

    elif distancia < 30:
        # Calcula la velocidad reducida según la distancia
        nueva_velocidad = round(50 * (distancia - 10) / 20)
        cpi.mbot2.forward(speed = nueva_velocidad) # Avanzar más lento

    else:
        cpi.mbot2.forward(speed = 50) # Avanzar normal
```

### Retos

5. Coloca 4 objetos en las esquinas de un cuadrado. Encuentra uno de ellos y detente antes de golpearlo. Gira y busca el siguiente objeto, hasta que hayas encontrado los cuatro.
6. Encuentra el camino de forma autónoma a través de un laberinto sencillo (las paredes deben tener al menos 10 cm de altura).
