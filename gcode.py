from driver import move_xy_simultaneous, laser_set, pos, STEPS_PER_MM_X, STEPS_PER_MM_Y

def parse_line(line):
    line = line.split(';')[0].strip()
    if not line:
        return None
    parts = line.split()
    cmd = parts[0]
    coords = {}
    for p in parts[1:]:
        axis = p[0]
        if axis in ['X','Y','F','S']:
            coords[axis] = float(p[1:])
    return cmd, coords

def to_steps(x_mm=None, y_mm=None):
    tx = pos['X'] if x_mm is None else int(x_mm * STEPS_PER_MM_X)
    ty = pos['Y'] if y_mm is None else int(y_mm * STEPS_PER_MM_Y)
    return tx, ty

def execute(cmd, coords):
    if cmd == 'G0':
        tx, ty = to_steps(coords.get('X'), coords.get('Y'))
        move_xy_simultaneous(tx - pos['X'], ty - pos['Y'])
    elif cmd == 'G1':
        tx, ty = to_steps(coords.get('X'), coords.get('Y'))
        move_xy_simultaneous(tx - pos['X'], ty - pos['Y'])
    elif cmd == 'M3':
        laser_set(True)
    elif cmd == 'M5':
        laser_set(False)

