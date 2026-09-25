from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, title="MazeSolver"):
        self.width = width
        self.height = height
        self.rootWidget = Tk()
        self.rootWidget.title(title)
        self.rootWidget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.rootWidget, bg="white", height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.windowRunning = False
        print("Initializing Window")

    def redraw(self):
        self.rootWidget.update_idletasks()
        self.rootWidget.update()

    def drawLine(self, line, fillColor: str):
        line.draw(self.canvas, fillColor)

    def waitForClose(self):
        self.windowRunning = True
        while self.windowRunning:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.windowRunning = False

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fillColor: str):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fillColor, width=2)
