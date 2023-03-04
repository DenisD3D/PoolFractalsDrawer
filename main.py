import gui
import fractal_computer

if __name__ == '__main__':
    x, y = map(int, input('Enter the width and height of the fractal (separated by a space): ').split())
    draw = fractal_computer.compute(x, y)
    gui.render(draw)
