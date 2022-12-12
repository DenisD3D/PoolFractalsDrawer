import gui


def set_slash(drawing: list[list[str]], x: int, y: int, sens: bool, toggle: bool) -> bool:
    if toggle:
        drawing[y][x] = '/' if sens else '\\'
    return not toggle


def compute(width: int, height: int) -> list[list[str]]:
    drawing = [['*' for _ in range(width)] for _ in range(height)]
    x = 0
    y = 0
    x_direction = 1
    y_direction = 1
    toggle = True
    sens = False
    x_flag = True
    y_flag = True
    while True:
        toggle = set_slash(drawing, x, y, sens, toggle)
        if ((x == width - 1 and y == height - 1) or (x == 0 and y == 0) or (x == width - 1 and y == 0) or (
                x == 0 and y == height - 1)) and not x_flag and not y_flag:
            break
        elif x == width - 1 and not x_flag:
            y += y_direction
            x_direction = -1
            sens = not sens
            toggle = set_slash(drawing, x, y, sens, toggle)
            toggle = not toggle
            x_flag = True
        elif x == 0 and not x_flag:
            y += y_direction
            x_direction = 1
            sens = not sens
            toggle = set_slash(drawing, x, y, sens, toggle)
            toggle = not toggle
            x_flag = True
        elif y == height - 1 and not y_flag:
            x += x_direction
            y_direction = -1
            sens = not sens
            toggle = set_slash(drawing, x, y, sens, toggle)
            toggle = not toggle
            y_flag = True
        elif y == 0 and not y_flag:
            x += x_direction
            y_direction = 1
            sens = not sens
            toggle = set_slash(drawing, x, y, sens, toggle)
            toggle = not toggle
            y_flag = True
        else:
            x += x_direction
            y += y_direction
            x_flag = False
            y_flag = False
    return drawing


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw = compute(355, 113)
    # print(draw)
    # print('-' * 11)
    # for row in draw:
    #     print('|', end='')
    #     for cell in row:
    #         print(cell, end='')
    #     print('|')
    # print('-' * 11)

    gui.render(draw)
