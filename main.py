from graphics import *


def main() -> None:
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    line.draw(win.canvas, fillColor="black")
    win.waitForClose()

main()