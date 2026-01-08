# 🚀 C. Nuestro primer programa – Hola

Nuestro primer programa:

- Escribirá "hola" en la consola
- Lo reproducirá por el altavoz
- Encenderá todos los LEDs en verde durante 2 segundos.

## La librería cyberpi

La librería que vamos a utilizar se llama `cyberpi`.

```python
import cyberpi
```

Es la instrucción que se usa en Python para cargar la librería (biblioteca) oficial que permite controlar la placa CyberPi.
Sin esta línea de código, Python no sabría qué es la CyberPi ni cómo hablar con sus sensores, luces o pantalla.

## Alias

Un alias es una variable que podemos utilizar para hacer referencia a otra palabra.

```python
import cyberpi as cpi  # Importa la librería de CyberPi
```

Ahora, cuando usemos `cpi` será como escribir `cyberpi`.

## Mostrar información por pantalla

```python
import cyberpi as cpi  # Importa la librería de CyberPi
cpi.console.print("hola")    # Escribe "hello" en la pantalla del robot
```

```python
import cyberpi as cpi  # Importa la librería de CyberPi
import time            # Importa la librería de tiempo

cpi.console.print("hello")    # Escribe "hello" en la pantalla del robot
cpi.audio.play('hello')       # Reproduce el sonido "hello" por el altavoz
cpi.led.on(0, 255, 0)         # Enciende los LEDs en verde (Rojo=0, Verde=255, Azul=0)
time.sleep(2)                 # Espera 2 segundos antes de seguir
cpi.led.off()                 # Apaga todos los LEDs
cpi.console.clear()           # Borra el texto de la pantalla
```

## Temporizador

```python
import cyberpi as cpi  # Importa la librería de CyberPi
import time            # Importa la librería de tiempo

cpi.console.print("hola")    # Escribe "hello" en la pantalla del robot
time.sleep(2)                 # Espera 2 segundos antes de seguir
cpi.console.clear()           # Borra el texto de la pantalla
```

## Encender LEDs

```python
import cyberpi as cpi  # Importa la librería de CyberPi
import time            # Importa la librería de tiempo

cpi.led.on(0, 255, 0)         # Enciende los LEDs en verde (Rojo=0, Verde=255, Azul=0)
time.sleep(2)                 # Espera 2 segundos antes de seguir
cpi.led.on(255, 0, 0)         # Enciende los LEDs en verde (Rojo=0, Verde=255, Azul=0)
time.sleep(2)                 # Espera 2 segundos antes de seguir
cpi.led.on(0, 0, 255)         # Enciende los LEDs en verde (Rojo=0, Verde=255, Azul=0)
time.sleep(2)                 # Espera 2 segundos antes de seguir
cpi.led.off()                 # Apaga todos los LEDs
```

Si quieres un color que no sea básico, usas valores RGB (Rojo, Verde, Azul) de 0 a 255:

```
cpi.led.show(r, g, b): Enciende todos los LEDs con la mezcla exacta.
```

cpi.led.show(255, 255, 0) #crea color amarillo.

Como hay 5 luces, puedes controlar cada una por separado usando su número (del 1 al 5):
cpi.led.set_rgb(r, g, b, id) #Cambia el color de un solo LED.

```
cpi.led.set_rgb(255, 0, 0, 1) #pone solo el primer LED en rojo.
```

Brillo:

```
cpi.led.set_brightness(valor): Ajusta qué tan fuerte brilla la luz (de 0 a 100).
```

Efectos:

```
cpi.led.play(nombre_efecto): Activa animaciones predefinidas como "rainbow" (arcoíris) o "meteor".
```

## 📤 Carga del programa al mBot2

Haz clic en el botón **Upload** (Cargar) para enviar tu código al mBot2.
El código comenzará a ejecutarse inmediatamente después de que la carga finalice.

## ❌ Carga fallida (Unsuccessful Upload)

Si la carga falla, comprueba estos tres puntos:

1. **Interruptor:** Que el mBot2 esté encendido (el interruptor de encendido está en el lado izquierdo).
2. **Conexión:** Que el cable esté bien enchufado y se haya establecido la conexión (consulta la sección B4).
3. **Modo:** Asegúrate de que el editor esté en modo "Upload" y no en modo "Live".

## 💾 Guardar el proyecto y exportar a la CyberPi

Para guardar el proyecto en tu ordenador:

1. Haz clic en el menú **File** (Archivo).
2. Elige la opción **Export project**.

> **💡 Consejo:** Es muy recomendable crear una carpeta específica para organizar todos tus proyectos. Asegúrate de escribir un nombre descriptivo para cada archivo (por ejemplo: `01_hola_mundo.mblock`) para encontrarlos fácilmente después.

## 💬 Retroalimentación del programa (Feedback)

Puedes ayudarte a ti mismo a entender qué está haciendo el robot usando la función `print()`.

**Es importante notar la diferencia:**

1. `cpi.console.print()`: Escribe el texto en la **pantalla pequeña** del CyberPi.
2. `print()`: Envía el texto a la **consola de Python en tu ordenador**. Esto es ideal para depurar (debug) sin llenar la pantallita del robot.

Prueba este código para ver la diferencia:

```python
import cyberpi as cpi  # Importa las funciones del cerebro CyberPi
import time            # Importa las funciones para controlar el tiempo

# Mensaje para el programador (aparece en la consola del PC, no en el robot)
print("Iniciando secuencia de prueba...")

cpi.console.print("Hola Mundo") # Escribe el texto en la pantalla física del robot
time.sleep(1)                   # Mantiene el mensaje en pantalla durante 1 segundo

# Mensaje de finalización (aparece solo en la consola del PC)
print("Cerrando programa.")
```

## Comentarios y activación/desactivación de líneas de código

Coloca una # delante de cualquier línea para crear comentarios o para convertir sentencias de código en comentarios para que no se ejecuten.
