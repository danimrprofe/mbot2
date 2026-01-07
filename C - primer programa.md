# 🚀 C. Nuestro primer programa – Hola

Nuestro primer programa:

- Escribirá "hola" en la consola
- Lo reproducirá por el altavoz
- Encenderá todos los LEDs en verde durante 2 segundos.

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
