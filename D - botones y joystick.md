## 🔘 D. Botones y Joystick

El mBot2 se controla mediante el módulo **CyberPi**. Este dispositivo incluye:

- Un **Joystick** de 5 posiciones.
- Un **Botón central** (Home).
- Dos **Botones pulsadores** (A y B).
- Sensores integrados: Sensor de luz y micrófono.

Mientras no pulsesmos el botón A, el led se quedará rojo, al pulsarlo saldremos del bucle y se pondrá verde.

```python
import cyberpi as cpi  # Importa la librería para controlar el mBot2
import time            # Importa la librería para gestionar tiempos y pausas

# --- ESPERA A QUE SE PULSE EL BOTÓN A ---
cpi.console.print("Pulsa A para iniciar") # Muestra instrucciones en la pantalla del robot

# Bucle de espera: se repite mientras el botón A NO esté presionado
while not cpi.controller.is_press('a'):
    cpi.led.on(255, 0, 0) # Mantiene los LEDs en color rojo (estado de espera)
cpi.led.on(0, 255, 0) # Poner los leds verdes
```

### Control mediante bucles y condiciones

En lugar de que el código se ejecute automáticamente al cargarse, vamos a hacer que el robot espere a que interactuemos con él. Utilizaremos un bucle `while` que mantenga las luces en rojo hasta que pulsemos el **botón A**.

```python
import cyberpi as cpi  # Importa la librería para controlar el mBot2
import time            # Importa la librería para gestionar tiempos y pausas

# --- ESPERA A QUE SE PULSE EL BOTÓN A ---
cpi.console.print("Pulsa A para iniciar") # Muestra instrucciones en la pantalla del robot

# Bucle de espera: se repite mientras el botón A NO esté presionado
while not cpi.controller.is_press('a'):
    cpi.led.on(255, 0, 0) # Mantiene los LEDs en color rojo (estado de espera)
    time.sleep(0.1)       # Pausa de 0.1s para que el procesador no trabaje en exceso

# Una vez que presionas el botón A, el programa sale del bucle y sigue aquí:
cpi.led.on(0, 255, 0)     # Cambia el color de los LEDs a verde (estado activo)
cpi.console.clear()       # Borra el mensaje anterior de la pantalla
cpi.console.print("¡Iniciado!") # Escribe el nuevo mensaje de confirmación
cpi.audio.play('hello')   # Reproduce el sonido de saludo por el altavoz
```
