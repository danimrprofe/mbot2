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

