## E. Funcionamiento de los Motores

Existen varias formas en las que podemos querer mover el mBot2. Las velocidades de los motores hacia adelante están entre **0 y 100**. Las velocidades hacia atrás están entre **0 y -100**. El movimiento sigue ocurriendo incluso a velocidades muy cercanas a cero.

### Forward or backward forever.

(Should only be used when the ultrasonic sensor or colour sensors are used to control when the motors should stop)

```python
cpi.mbot2.forward(speed = 50)
cpi.mbot2.backward(speed = 50)
cpi.mbot2.forward(speed = -50)
cpi.mbot2.EM_stop(port = "all")
```

### Forward or backward for a length of time

```python
cpi.mbot2.forward(speed = 50, run_time = 1)
cpi.mbot2.backward(speed = 50, run_time = 1)
cpi.mbot2.forward(speed = -50, run_time = 1)
```

### Forward or backward for a fixed distance

cpi.mbot2.straight(40, speed = 50)
cpi.mbot2.straight(-40, speed = 50)

### Turn on the spot for a length of time

(wheels turning in different directions)
cpi.mbot2.turn_left(speed = 50, run_time = 1)
cpi.mbot2.turn_right(speed = 50, run_time = 1)

### Turn for a number of degrees of heading

cpi.mbot2.turn(90, speed = 50)

### Gradual turn for a length of time

(wheels turning in the same direction or one wheel stopped)
cpi.mbot2.drive_power(60, -40) #left +, right -
time.sleep(2)
cpi.mbot2.EM_stop(port = "all")

### Stop motors

cpi.mbot2.EM_stop(port = "all")

## 📄 Plantillas de Código

Existen dos plantillas de código básicas que utilizamos al trabajar con motores. En ambos casos, usamos el botón A para activar el mBot2 e iniciar las acciones.

Separar el código en secciones hace que sea mucho más fácil de entender y de realizar cambios en él. Más adelante, añadiremos más secciones según las vayamos necesitando.

# Programación de mBot2 / CyberPi con Python

### 1. Acciones Únicas (Single Actions)

Utiliza este bloque cuando quieras que las acciones del mBot2 ocurran solo una vez al iniciar el programa.

```python
#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#ESPERAR PARA EMPEZAR--------------------------
cpi.console.println('Pulsa A')
while not cpi.controller.is_press('a'):
    cpi.led.on(255,0,0) # Rojo
    cpi.led.on(0,255,0) # Verde

#ACCIONES DEL ROBOT----------------------------
cpi.mbot2.forward(speed = 50, run_time = 2)  # Avanzar (velocidad 50, durante 2 seg)
cpi.mbot2.backward(speed = 50, run_time = 2) # Retroceder (velocidad 50, durante 2 seg)
cpi.led.off()
```

Si tenemos acciones que se repiten un número específico de veces, podemos usar un bucle for. Por ejemplo, para moverse en cuadrado:

```python
#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#ESPERAR PARA EMPEZAR--------------------------
cpi.console.println('Pulsa A')
while not cpi.controller.is_press('a'):
    cpi.led.on(255,0,0)
    cpi.led.on(0,255,0)

#ACCIONES DEL ROBOT----------------------------
# El robot hará un cuadrado (4 lados)
for i in range(4):
    cpi.mbot2.straight(40, speed = 50) # Avanza 40 cm
    cpi.mbot2.turn(90, speed = 50)     # Gira 90 grados

cpi.led.off()
```

### RETOS

**Reto 1**

- Coloca uno o más objetos grandes en el suelo. Navega con el mBot2 a través o alrededor de ellos.

**Reto 2**

- Consiste en una serie de tableros que forman un laberinto.
- No conoces la forma del laberinto hasta la competición.
- Gana la persona que mantenga al robot sobre los tableros y consiga el tiempo más rápido.

### 2. Acciones Infinitas (Forever Actions)

Este código utiliza un bucle while True que repite las acciones indefinidamente, o hasta que presiones el botón "Home" junto a la conexión USB.

```python
#IMPORTACIONES---------------------------------
import cyberpi as cpi
import time

#ESPERAR PARA EMPEZAR--------------------------
cpi.console.println('Pulsa A')
while not cpi.controller.is_press('a'):
    cpi.led.on(255,0,0)
    cpi.led.on(0,255,0)

#BUCLE PRINCIPAL-------------------------------
while True:
    # El robot se moverá adelante y atrás continuamente
    cpi.mbot2.forward(speed = 50, run_time = 2)  # Avanza (velocidad 50, 2 segundos)
    cpi.mbot2.backward(speed = 50, run_time = 2) # Retrocede (velocidad 50, 2 segundos)
```

Este tipo de código se utiliza principalmente en conjunto con el joystick, los botones o los sensores (ultrasónico y sigue-líneas), donde el mBot2 debe responder constantemente a los cambios en el entorno.

### RETOS

**Reto 1**

- Coloca dos objetos pequeños en el suelo a una distancia mínima de 1 metro.
- Conduce alrededor de ellos varias veces formando un "8".
- Cuando gires, utiliza los LED para indicar tus giros.

**Reto 2**

- Coloca un objeto grande en el suelo y gira alrededor de él 3 veces en un círculo grande y suave (Utiliza la función cpi.mbot2.drive_power()).
