# 🤖 MakeBlock mBot2 / CyberPi con Python

## 📚 Documentación Oficial

* **Centro de ayuda mBlock Python:** [mBlock Python Editor](https://www.yuque.com/makeblock-help-center-en/mcode/mblock-python)
* **API de CyberPi:** [CyberPi Python API](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api)
    *(Incluye Pocket Shield, mBot2 Shield y módulos mBuild)*

---

## 🔄 Actualización de Firmware
Para actualizar el firmware de tu CyberPi, sigue estos pasos:

1.  Abre el IDE en línea: [ide.mblock.cc](https://ide.mblock.cc/#/)
2.  Haz clic en **Dispositivos** (Devices) y añade el dispositivo **CyberPi** a la lista.
3.  Haz clic en **Conectar** (Connect) para vincular tu CyberPi.
4.  Ve a **Ajustes** (Settings) y selecciona **Actualización de Firmware** (Firmware Update).

---

## 🏎️ A. El Vehículo mBot2

### Enlaces de Referencia
* **Introducción al mBot2:** [Conceptos básicos](https://education.makeblock.com/help/cyberpi-series/cyberpi-series-cyberpi-series-packages-and-extensions/mbot2-introduction/)
* **Guía Operativa:** [Manual de funcionamiento](https://education.makeblock.com/help/cyberpi-series/cyberpi-series-cyberpi-series-packages-and-extensions/mbot2-operational-guide/)
* **Referencia de Python (Shields):** [CyberPi Shields API](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api-shields#9eo89)
* **Módulos mBuild:** *(Sensor Ultrasónico 2, Sensor Quad RGB)*
    * [Opción 1: Yuque Documentation](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api-mbuild)
    * [Opción 2: Makeblock Help Center](https://education.makeblock.com/help/mblock-python/mblock-python-editor-python-api-documentation-for-devices/mblock-python-editor-python-api-documentation-for-cyberpi/mblock-python-editor-apis-for-mbuild-modules/)

### 🛠️ Montaje y Conexiones
Para que el robot funcione correctamente, asegúrate de cumplir con lo siguiente:

* **Sensores:** El sensor de ultrasonidos debe ir conectado al puerto **mBuild**.
* **Motores:** Los motores deben conectarse a los puertos **EM1** y **EM2**.
* **Energía:** El interruptor de encendido **debe estar en posición ON** antes de intentar cargar o subir cualquier código desde el ordenador.

## 🛠️ B. Introducción y Configuración

### 1. Descarga e Instalación del Software
* Descarga e instala el software mBlock para Windows o Mac desde: [mblock.makeblock.com](https://mblock.makeblock.com/en-us/download/)
* *(Nota: La versión de escritorio suele ser más estable que la versión web).*

### 2. Configuración del Editor
1. Ejecuta el software y selecciona el **Editor de Python**.
2. Se abrirá el programa del Editor de Python. Puedes cerrar el editor de bloques si lo deseas.

### 3. Encendido y Verificación física
* **ENCIENDE EL MBOT2** usando el interruptor lateral.
* **Verificación:** Las luces del sensor de ultrasonidos y del sensor de seguimiento de línea deben encenderse. Si no lo hacen, comprueba que los cables estén bien conectados.

### 4. Conexión del Robot
1. Selecciona el modo **Upload** (Carga). Si aparece un mensaje, marca "Don't remind me" (No volver a mostrar) y haz clic en *Sure*.
2. Conecta el mBot2 al puerto USB del ordenador.
3. Haz clic en el botón **Connect** (Conectar).
4. Selecciona tu puerto USB de la lista y haz clic en **Connect**.

### 🔍 Cómo encontrar tu puerto USB
Si tienes dudas de cuál es el puerto correcto, sigue este truco:
1. Deja el mBot **desconectado**.
2. Haz clic en **Connect** y observa la lista de puertos disponibles.
3. Cierra la ventana de conexión.
4. Conecta tu mBot2 al USB.
5. Haz clic en **Connect** de nuevo: el puerto que acaba de aparecer en la lista es el de tu robot.

### 5. Empezar a programar
1. Ve al menú **File** (Archivo).
2. Selecciona **New Project** (Nuevo proyecto).
3. ¡Ya puedes empezar a escribir tu código!

## 🚀 C. Nuestro primer programa – Hola

Nuestro primer programa escribirá "hola" en la consola, lo reproducirá por el altavoz y encenderá todos los LEDs en verde durante 2 segundos.

```python
import cyberpi as cpi
import time

cpi.console.print("hello")
cpi.audio.play('hello')
cpi.led.on(0, 255, 0) #red, green, blue values from 0 to 255
time.sleep(2)         #time delay in seconds
cpi.led.off()
cpi.console.clear()
```
     
### 📤 Carga del programa al mBot2

Haz clic en el botón **Upload** (Cargar) para enviar tu código al mBot2.
El código comenzará a ejecutarse inmediatamente después de que la carga finalice.

---

### ❌ Carga fallida (Unsuccessful Upload)

Si la carga falla, comprueba estos tres puntos:
1. **Interruptor:** Que el mBot2 esté encendido (el interruptor de encendido está en el lado izquierdo).
2. **Conexión:** Que el cable esté bien enchufado y se haya establecido la conexión (consulta la sección B4).
3. **Modo:** Asegúrate de que el editor esté en modo "Upload" y no en modo "Live".

### 💾 Guardar el proyecto y exportar a la CyberPi

Para guardar el proyecto en tu ordenador:
1. Haz clic en el menú **File** (Archivo).
2. Elige la opción **Export project**.

> **💡 Consejo:** Es muy recomendable crear una carpeta específica para organizar todos tus proyectos. Asegúrate de escribir un nombre descriptivo para cada archivo (por ejemplo: `01_hola_mundo.mblock`) para encontrarlos fácilmente después.

### 💬 Retroalimentación del programa (Feedback)

Puedes ayudarte a ti mismo a entender qué está haciendo el robot usando la función `print()`. 

**Es importante notar la diferencia:**
1. `cpi.console.print()`: Escribe el texto en la **pantalla pequeña** del CyberPi.
2. `print()`: Envía el texto a la **consola de Python en tu ordenador**. Esto es ideal para depurar (debug) sin llenar la pantallita del robot.

Prueba este código para ver la diferencia:

```python
import cyberpi as cpi
import time

# Mensaje para el programador (aparece en el PC)
print("Iniciando secuencia de prueba...") 

cpi.console.print("Hola Mundo") # Aparece en el robot
time.sleep(1)

print("Cerrando programa.")
```

### Comments and turning on/off code statements

Put a # in front of any line to create comments or to turn code statements into comments so they are not executed.

## 🔘 D. Botones y Joystick

El mBot2 se controla mediante el módulo **CyberPi**. Este dispositivo incluye:
* Un **Joystick** de 5 posiciones.
* Un **Botón central** (Home).
* Dos **Botones pulsadores** (A y B).
* Sensores integrados: Sensor de luz y micrófono.

### Control mediante bucles y condiciones
En lugar de que el código se ejecute automáticamente al cargarse, vamos a hacer que el robot espere a que interactuemos con él. Utilizaremos un bucle `while` que mantenga las luces en rojo hasta que pulsemos el **botón A**.

```python
import cyberpi as cpi
import time

# --- ESPERA A QUE SE PULSE EL BOTÓN A ---
cpi.console.print("Pulsa A para iniciar")

# Mientras el botón A NO esté pulsado...
while not cpi.controller.is_press('a'):
    cpi.led.on(255, 0, 0) # Luces rojas de espera
    time.sleep(0.1)       # Pequeña pausa para no saturar el procesador

# Una vez pulsado A, el código continúa aquí
cpi.led.on(0, 255, 0)     # Cambia a verde
cpi.console.clear()
cpi.console.print("¡Iniciado!")
cpi.audio.play('hello')
```

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

- Coloca uno o más objetos grandes en el suelo. Navega con el mBot2 a través o alrededor de ellos.
- Una de las competiciones de RoboRAVE es "AMAZE-ing". Consiste en una serie de tableros que forman un laberinto. No conoces la forma del laberinto hasta la competición. Gana la persona que mantenga al robot sobre los tableros y consiga el tiempo más rápido.

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

- Coloca dos objetos pequeños en el suelo a una distancia mínima de 1 metro. Conduce alrededor de ellos varias veces formando un "8". Cuando gires, utiliza los LED para indicar tus giros.
- Coloca un objeto grande en el suelo y gira alrededor de él 3 veces en un círculo grande y suave (Utiliza la función cpi.mbot2.drive_power()).
   
## F. Avoid or Seek

The Ultrasonic Sensor is used to measure the distance between the mBot2 and anything in front of it (up to about 200cm). It can be used to avoid obstacles or seek out an object and move toward it.

The minimum distance detected in 4cm. Smaller distances give a reading of 300.

Test your Ultrasonic Sensor with this code. Putting all the sensor reading code into a function unclutters the main loop.

```python
#IMPORTACIONES--------------------------------- 
import cyberpi as cpi 
import time 

#VARIABLES GLOBALES---------------------------- 
distancia = 300 

#FUNCIONES------------------------------------- 
def obtener_valores(mostrar=True): 
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
    obtener_valores(mostrar=True)
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
        
### Slow Down when Close to a Collision 

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

5. Place 4 objects at the corners of a square. Find one of them and stop before you hit it. Turn and find the next object, until you have found all four. 
6. Find your way autonomously through a simple maze (sides are 10cm high)

# G. Detect and Follow a Line

The Quad RGB Sensor (color sensor) enables us to detect and follow lines, and detect colours and respond to the colours in different ways.
Test the Sensor using this code, by passing the mBot2 over a black line on a white background.

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

## 🏁 F. Seguimiento de Línea (Conceptos Básicos)

El sensor del mBot2 detecta cuánta luz rebota del suelo.

- Línea Negra: Rebota poca luz (valor bajo, menos de 50%).
- Suelo Blanco: Rebota mucha luz (valor alto, más de 50%).

1. La Lógica de Decisión

Para que el robot siga la línea, debe decidir según lo que ven sus dos sensores centrales (L1 y R1):

- Si L1 y R1 ven negro: El robot está centrado → Avanza recto.
- Si solo L1 ve negro: El robot se está saliendo por la derecha → Gira a la izquierda.
- Si solo R1 ve negro: El robot se está saliendo por la izquierda → Gira a la derecha.

2. Código del Programa

Este es el programa completo y simplificado. Primero pruébalo solo con luces; cuando funcione, quita el símbolo # de los motores.

```python
import cyberpi as cpi

# BUCLE PRINCIPAL
while True:
    # Leer valores de los sensores de línea
    # L1 y R1 son los sensores internos
    L1 = cpi.quad_rgb_sensor.get_gray('L1')
    R1 = cpi.quad_rgb_sensor.get_gray('R1')

    if L1 < 50 and R1 < 50:
        # AMBOS EN NEGRO: Recto
        cpi.mbot2.drive_power(20, -20) 
        cpi.led.on('red', id=2) # Luz izquierda
        cpi.led.on('red', id=4) # Luz derecha
        
    elif L1 < 50:
        # SOLO IZQUIERDA EN NEGRO: Girar a la izquierda
        cpi.mbot2.drive_power(5, -20) 
        cpi.led.on('red', id=2)
        cpi.led.off(id=4)
        
    elif R1 < 50:
        # SOLO DERECHA EN NEGRO: Girar a la derecha
        cpi.mbot2.drive_power(20, -5) 
        cpi.led.on('red', id=4)
        cpi.led.off(id=2)
        
    else:
        # FUERA DE LA LÍNEA (Blanco): Luces verdes
        cpi.led.on('green')
```

To follow the line faster, you might need the change:
• The power to the left and right wheels
• The difference in power between the left and right wheels
• How you interpret the percentage color sensor values
• Use the L2 and R2 sensors as well

### CHALLENGES 

5. Oval Race. Follow an oval line from start to finish. Time the run. The robot that does the quickest time wins. 
6. RoboRAVE Line Follower Race. Be the fastest robot to get from home to the box.

## H. SumoBot

SumoBots use the ultrasonic sensor to seek and destroy another robot vehicle in the Sumo ring, while using the color sensor to sense the white border and avoid falling off the edge.

### H1. Basic Sumo Code

Las acciones fundamentales de un SumoBot son:

- Espera de seguridad: Tres segundos de pausa antes de cualquier acción (norma común en competiciones).
- Entrada al ring: Avanzar 20 cm desde el borde inicial.
- Búsqueda: Girar hasta que el sensor de ultrasonidos localice al oponente (a menos de 80 cm).
- Ataque: Conducir a máxima velocidad hacia el otro vehículo.
- Supervivencia: Si se detecta el borde blanco (valor de reflectancia alto), detenerse, retroceder y girar para volver a buscar al oponente.

Este código utiliza la lógica de detección de línea blanca (fondo oscuro, borde claro) y detección de objetos.

```python
# --- PREPARACIÓN INICIAL ---
time.sleep(3) # Espera de seguridad de 3 segundos
encontrado = False
cpi.mbot2.straight(20, speed = 40) # Entrar 20 cm al ring

# --- BUCLE PRINCIPAL DE COMBATE ---
while True:
    # Obtenemos valores. black_line=False busca líneas blancas (reflectancia alta)
    obtener_valores(mostrar=False, linea_negra=False)
    
    if hay_linea: 
        # ¡Peligro! Borde del ring detectado (línea blanca)
        encontrado = False
        cpi.led.on(0, 255, 0) # LEDs en verde
        cpi.mbot2.EM_stop(port = "all")
        # Maniobra de supervivencia: retroceder y girar
        cpi.mbot2.straight(-10, speed = 40)
        cpi.mbot2.turn(90, speed = 40) 

    elif distancia < 80 or encontrado:
        # ¡Oponente localizado!
        encontrado = True
        cpi.led.on(0, 0, 255) # LEDs en azul (modo ataque)
        cpi.mbot2.forward(speed = 100) # Ataque a máxima velocidad
        
    else:
        # Buscando al oponente
        cpi.led.on(255, 0, 0) # LEDs en rojo (modo búsqueda)
        cpi.mbot2.turn_left(speed = 30) # Girar para localizar
```

🔍 Explicación de las mejoras añadidas:

- encontrado = True: He añadido esta "bandera" para que, una vez que el robot detecta al oponente, no deje de avanzar aunque lo pierda de vista un milisegundo, asegurando un empuje constante.
- linea_negra=False: Es crucial en la función obtener_valores. En un ring de sumo, el suelo es negro y el borde es blanco, por lo que buscamos valores de reflectancia altos (mayores a 50).
- Velocidad de ataque: He subido la velocidad en el ataque (forward(speed = 100)) para maximizar la fuerza de empuje.

### H2. Enhancements

• Don’t waste time moving forward at the start before starting to find the other vehicle
• Only scan left and right up to 90 degrees the first time
• Stop every 10 degrees when scanning to make sure scan detects vehicle (moving too fast doesn’t work)
• Use movement sensor to detect a collision or the bot lifted off the ground (pitch or roll) and respond to that (see Appendix 1)
• If motion is stopped for x seconds, use a series of rapid wheel movements (e.g. back and forth) to try and get free
• Use a different strategy:
▪ Follow white line around the outside (use L2 or R2)
▪ Drive to a random place
▪ Drive forward until white line and turn and randomly go somewhere else until white line
• Use more than one ultrasonic sensor at different angles

Aquí tienes la traducción y adaptación de la guía de hardware y bucles avanzados para el mBot2 y CyberPi, organizada en formato Markdown para mayor claridad.

## 🛠️ I. Conexión de Servos, Sensores y Motores

### Servos

Puedes conectar hasta 4 servos en los puertos específicos de la derecha (S3 y S4) o en los puertos de entrada/salida (IO) de la izquierda (S1 y S2).

```python
import cyberpi as cpi
import time

while True:
    cpi.mbot2.servo_set(90, 'S1')   # Mover servo en S1 a 90 grados
    time.sleep(1)
    cpi.mbot2.servo_set(140, 'S1')  # Mover a 140 grados
    time.sleep(2)
    cpi.mbot2.servo_set(40, 'S1')   # Mover a 40 grados
    time.sleep(2)
```

### Lectura de Sensores Analógicos

Lee sensores analógicos (como potenciómetros o sensores de humedad de suelo) usando los puertos S1 y S2.

```python
# Retorna un valor de voltaje entre 0 – 5V
valor = cpi.mbot2.read_analog('S1')
```

### Lectura y Escritura Digital

Puedes leer estados (encendido/apagado) o enviar señales digitales.

```python
# Escribir (val = True, False, 0, 1)
cpi.mbot2.write_digital(1, 'S1') 

# Leer (retorna True o False)
estado = cpi.mbot2.read_digital('S1')
```

### Motores de Corriente Continua (DC)

Se pueden conectar motores adicionales en los puertos M1 y M2.

```python
# Ajustar potencia individual (-100 a 100)
cpi.mbot2.motor_set(50, 'M1') 

# Detener un motor específico
cpi.mbot2.motor_stop('M1') 

# Ajustar potencia a M1 y M2 simultáneamente
cpi.mbot2.motor_drive(50, 50)
```

### 🔁 Bucles Avanzados (Loops)

Puedes usar rangos para controlar LEDs específicos, por ejemplo: for i in range(4, 6): encenderá los LEDs del 4 al 5.

Este ejemplo utiliza los botones A y B para alternar patrones de colores en los LEDs:

```python
import cyberpi as cpi
import time

while True:
    if cpi.controller.is_press('a'):
        # Enciende LEDs 1, 3 y 5 en VERDE
        for i in range(1, 6, 2): 
            cpi.led.on(0, 255, 0, id = i) 
        cpi.console.print('verde\n')
        
    elif cpi.controller.is_press('b'):
        cpi.led.off() # Apaga todos antes de cambiar
        # Enciende LEDs 2 y 4 en AZUL
        for i in range(2, 5, 2): 
            cpi.led.on(0, 0, 255, id = i)
        cpi.console.print('azul\n')
        
    time.sleep(0.1) # Pequeña pausa para estabilidad
```

Aquí tienes la traducción y organización de los extras de CyberPi en formato Markdown. He agrupado los comandos por su función para que te sirvan como una guía de referencia rápida.

## 📚 Apéndice 1: Extras de CyberPi

### Sensores externos (Ultrasonidos, Deslizador y Multitáctil)

Este código lee la distancia, el valor de un potenciómetro deslizante y si se está tocando un sensor táctil.

```python
import cyberpi as cpi
import time

while True:
    distancia = cpi.ultrasonic2.get(index=1)
    potenciometro = cpi.slider.get()
    tocado = cpi.multi_touch.is_touch(ch = 1) # Canal 1-8 o "any" (cualquiera)
    
    print(distancia, potenciometro, tocado)
    time.sleep(0.1)
```

### Sensores integrados de CyberPi

#### Sensor de luz: mide el brillo ambiental.

```python
luz = cpi.get_bri()
```

#### Sensor de sonido: mide el volumen ambiental.

```python
volumen = cpi.get_loudness(mode = "maximum")
```

### Comandos de Audio

Controla el altavoz interno para generar tonos o ajustar el volumen.

```python
cpi.audio.play_tone(440, 1) # Toca una frecuencia (Hz) durante (t) segundos
cpi.audio.add_vol(10)       # Ajusta volumen (-100 a 100)
```

### Acelerómetro y Giroscopio (Detección de movimiento)

CyberPi puede detectar su inclinación y orientación en el espacio.

#### Inclinación básica

```python
adelante = cpi.is_tiltforward()
atras = cpi.is_tiltback()
izquierda = cpi.is_tiltleft()
derecha = cpi.is_tiltright()
```

#### Detección de agitación:

```python
cpi.is_shake()              # Devuelve True si se agita
valor_giro = cpi.get_shakeval() # Intensidad del agitado (0-100)
```

#### Ángulos de orientación:

```python
cpi.get_pitch()   # Ángulo de inclinación (adelante/atrás)
cpi.get_roll()    # Ángulo de balanceo (izquierda/derecha)
cpi.get_yaw()     # Ángulo de guiñada (rotación horizontal)
cpi.reset_yaw()   # Restablece el ángulo de guiñada a cero
```
### Resumen de variables de orientación

Para que lo visualices mejor en tus proyectos de robótica:

- Pitch (Inclinación): Imagina el morro de un avión subiendo o bajando.
- Roll (Alabeo): El avión inclinando sus alas a los lados.
- Yaw (Guiñada): El avión girando a izquierda o derecha sin inclinarse.
