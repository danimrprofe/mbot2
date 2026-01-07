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