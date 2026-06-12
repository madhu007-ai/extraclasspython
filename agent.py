# simple reflex agent: noo memory, only reacts to current situation

# 4x4 grid: 'dirty' or 'clean'
grid = [
    ['dirty', 'clean', 'dirty', 'clean'],
    ['clean', 'dirty', 'clean', 'clean'],
    ['dirty', 'clean', 'dirty', 'dirty'],
    ['clean', 'clean', 'clean', 'dirty']
]

row, col = 0, 0  # start position
steps = 0

while steps < 14:
    print(f'Position ({row},{col}): {grid[row][col]}')

    # decision: only looks at current cell!
    if grid[row][col] == 'dirty':
        grid[row][col] = 'clean'
        print('  -> CLEAN')
    else:
        # simple zigzag movement
        if col < 3:
            col += 1
        elif row < 3:
            row += 1
        else:
            col -= 1
        print('  -> MOVE')

    steps += 1

print(f'\ndone in {steps} steps')
