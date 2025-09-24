# CNC INTERPRETER ESP32

📌 Proyecto en **MicroPython** para controlar un **plotter CNC / grabador láser** usando un **ESP32**.  
Interpreta comandos **G-code** básicos (G0, G1, M3, M5) y permite **dibujar texto vectorial** definido en un diccionario de fuentes.

---

## 🚀 Características
- Control de motores paso a paso (X, Y) mediante pines configurables.
- Encendido/apagado de láser por pin digital.
- Conversión de coordenadas en **mm → pasos**.
- Interpretación simple de G-code (`G0`, `G1`, `M3`, `M5`).
- Fuente vectorial incluida (A–Z).
- Modular: código dividido en `driver.py`, `gcode.py`, `font.py`, `utils.py`.

---

## 📂 Archivos principales
- `main.py`: flujo principal (pedir texto y grabarlo).
- `driver.py`: control de pines, motores y láser.
- `gcode.py`: parser y ejecución de G-code.
- `font.py`: definición de letras vectoriales.
- `utils.py`: funciones auxiliares (tiempo, reverso de string).

---

## ⚡ Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/CNC-INTERPRETER-ESP32.git
   cd CNC-INTERPRETER-ESP32
