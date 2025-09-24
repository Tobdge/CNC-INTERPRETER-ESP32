from gcode import parse_line, execute
from font import FONT, LETTER_SPACING
from driver import laser_set
from utils import reverse_str, now_ms, elapsed

def emit_gcode_move(x=None, y=None, cut=False):
    cmd = "G1" if cut else "G0"
    parts = [cmd]
    if x is not None: parts.append(f"X{float(x)}")
    if y is not None: parts.append(f"Y{float(y)}")
    parsed = parse_line(" ".join(parts))
    if parsed:
        c, coords = parsed
        execute(c, coords)

def draw_letter(letter, x_offset=0.0):
    paths = FONT.get(letter.upper())
    if not paths:
        return
    for path in paths:
        if not path:
            continue
        laser_set(False)
        x0, y0 = path[0]
        emit_gcode_move(x=x0 + x_offset, y=y0, cut=False)
        laser_set(True)
        for (x, y) in path[1:]:
            emit_gcode_move(x=x + x_offset, y=y, cut=True)
        laser_set(False)

# --- flujo principal ---
for line in ["G21","G90","G17","F600","G0 X0 Y0","M5"]:
    parsed = parse_line(line)
    if parsed:
        cmd, coords = parsed
        execute(cmd, coords)

text = input("Escribe un texto (A-Z, máx 5): ").upper()
text = "".join([c for c in text if 'A' <= c <= 'Z'])[:5]

inicio = now_ms()

x_offset = 0.0
for ch in reverse_str(text):
    draw_letter(ch, x_offset)
    x_offset += LETTER_SPACING

for line in ["M5","G0 X0 Y0","M30"]:
    parsed = parse_line(line)
    if parsed:
        cmd, coords = parsed
        execute(cmd, coords)

fin = now_ms()
print("Tiempo total:", elapsed(inicio, fin), "segundos")

