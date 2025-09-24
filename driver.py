from machine import Pin
from time import sleep

STEPS_PER_MM_X = 80
STEPS_PER_MM_Y = 80
PULSE_DELAY = 0.001

motors = {
    'X': {'ENA': Pin(4, Pin.OUT), 'DIR': Pin(2, Pin.OUT), 'PUL': Pin(15, Pin.OUT)},
    'Y': {'ENA': Pin(5, Pin.OUT), 'DIR': Pin(17, Pin.OUT), 'PUL': Pin(16, Pin.OUT)},
}

laser = Pin(12, Pin.OUT)
laser.value(0)
laser_on = False

# posición actual
pos = {'X': 0, 'Y': 0}

def pulse(pin):
    pin.value(1); sleep(PULSE_DELAY)
    pin.value(0); sleep(PULSE_DELAY)

def move_xy_simultaneous(x_steps, y_steps):
    # signo lógico de destino (en pasos, puede ser +/-)
    sign_x = 1 if x_steps >= 0 else -1
    sign_y = 1 if y_steps >= 0 else -1

    # Dirección de pines (Y INVERTIDO)
    dir_x = 1 if x_steps >= 0 else 0
    dir_y = 0 if y_steps >= 0 else 1    # <<--- invertimos Y

    motors['X']['DIR'].value(dir_x)
    motors['Y']['DIR'].value(dir_y)

    # Magnitudes absolutas a pulsar
    x_steps = abs(x_steps)
    y_steps = abs(y_steps)

    if max(x_steps, y_steps) == 0:
        return

    # Bresenham simple
    err = 0
    sx, sy = x_steps, y_steps
    if sx >= sy:
        for _ in range(sx):
            pulse(motors['X']['PUL'])
            err += sy
            if (err << 1) >= sx:
                pulse(motors['Y']['PUL'])
                err -= sx
    else:
        for _ in range(sy):
            pulse(motors['Y']['PUL'])
            err += sx
            if (err << 1) >= sy:
                pulse(motors['X']['PUL'])
                err -= sy

    # Actualizamos la posición lógica según el signo real del movimiento
    pos['X'] += sign_x * x_steps
    pos['Y'] += sign_y * y_steps
    pass

def laser_set(state: bool):
    global laser_on
    if state and not laser_on:
        laser.value(1); laser_on = True
    elif not state and laser_on:
        laser.value(0); laser_on = False

