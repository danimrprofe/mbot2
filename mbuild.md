# 🔥 Makeblock AI & IoT Scientist

**IES Ramon Llull**

## 📋 Índice

1. [Introducción](#1-introducción)
2. [Hardware e Interconexión](#2-hardware-e-interconexión)
3. [Inventario de Componentes](#3-inventario-de-componentes)
4. [Especificaciones Técnicas Detalladas](#4-especificaciones-técnicas-detalladas)
5. [Guía de Programación en mBlock 5](#5-guía-de-programación-en-mblock-5)

---

## 1. Introducción

### ¿Qué es mBuild?

El sistema **mBuild** es una plataforma modular de sensores y actuadores inteligentes diseñados para la educación STEAM, IA e Internet de las Cosas.

- **Modularidad:** Conecta sensores en cadena sin necesidad de una placa de expansión compleja.
- **Compatibilidad:** Nativo para **CyberPi** y el **mBot2 Shield**.
- **Programación:** Soporta mBlock 5 (Bloques) y Python.

### ¿Qué es el AI & IoT Scientist Add-on Pack?

Es un pack de ampliación orientado a la experimentación avanzada. Su objetivo es permitir al alumno analizar datos reales y crear proyectos inteligentes conectados a la red.

---

## 2. Hardware e Interconexión

### Conexión Modular en Cadena (Daisy Chain)

- **Cables:** Se utilizan cables de 4 hilos.
- **Puertos:** Los módulos tienen dos puertos laterales para interconexión en serie.
- **Flujo de datos:** CyberPi reconoce todos los módulos en serie, ya estén conectados a su puerto lateral o a los puertos del mBot2 Shield.
- **Extensores:** Piezas específicas para ampliar la distancia física entre módulos.

### Gestión de Energía

- **Módulo de Batería:** Incluye botón de encendido/apagado y puerto USB de carga. Ideal para proyectos autónomos.
- **Alimentación vía CyberPi:** En modo conectado al PC, la CyberPi puede alimentar cadenas básicas por USB.

---

## 3. Inventario de Componentes

### I. Interfaz y Visualización

| Módulo                | Características                                       |
| :-------------------- | :---------------------------------------------------- |
| **Anillo LED RGB**    | 2 unidades de 12 LEDs. Control individual por LED.    |
| **Matriz de LEDs**    | Pantalla de 8x16 puntos azules para texto y gráficos. |
| **Speaker (Altavoz)** | Reproducción de notas, alarmas y sonidos.             |
| **Joystick**          | Control analógico en ejes X e Y.                      |
| **Slider**            | Potenciómetro deslizante para entrada de valores.     |

### II. Sensores y Actuadores

- **Sensores de entrada:** Luz, Gas, Llama, Temperatura, Humedad de suelo, Rango (distancia) y Campo Magnético.
- **Controladores (Drivers):** \* **Driver de Motor:** Para bombas de agua o motores DC.
  - **Driver de Servo:** Para servomotores (180º $\pm$ 10).
  - **Driver LED:** Para tiras de LEDs externas.

---

## 4. Especificaciones Técnicas Detalladas

### Actuadores Principales

- **Bomba de agua:** Motor especializado para circuitos hidráulicos.
- **Servomotor:** Control preciso de posición. Rango: 180º $\pm$ 10.

### Sensores Críticos

- **Sensor de Gas:** Detecta humo, metano, alcohol, etc. Rango: 300 a 10,000 ppm.
- **Sensor de Temperatura:** Rango de -55 a 125 °C ($\pm$ 0.5 °C). Consumo: 14 mA.
- **Sensor de Humedad (Suelo):** \* `0 - 20`: Suelo muy seco (Peligro).
  - `20 - 60`: Humedad ideal.
  - `60 - 100`: Suelo saturado.

### Iluminación

- **Controlador LED:** Actúa como puente entre CyberPi y periféricos de luz para animaciones y feedback visual.

---

## 5. Guía de Programación en mBlock 5

### Configuración de Extensiones

Es obligatorio añadir los módulos manualmente en el software para ver los bloques:

1. Conecta la **CyberPi** y selecciónala en "Dispositivos".
2. Haz clic en el botón **(+) Añadir Extensión**.

3. Busca el módulo específico (ej: "Matriz de LEDs", "Altavoz", "Joystick").
4. Tras añadirlo, los bloques aparecerán en el menú lateral.

> **Tip:** Para una ejecución estable, utiliza el **"Modo Carga"** al trabajar con múltiples módulos mBuild.
