from tkinter import Tk, Canvas as TkCanvas  # ✅ Fixed naming conflict
import time

class Canvas:
    def __init__(self, width, height):
        self.tk = Tk()
        self.tk.title("Canvas")
        self.canvas = TkCanvas(self.tk, width=width, height=height)  # ✅ Use renamed TkCanvas
        self.canvas.pack()
        self.tk.update()
        self._mouse_x = 0
        self._mouse_y = 0
        self._click = None
        self.canvas.bind('<Motion>', self._track_mouse)
        self.canvas.bind('<Button-1>', self._on_click)

    def _track_mouse(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_click(self, event):
        self._click = (event.x, event.y)

    def wait_for_click(self):
        self._click = None
        while self._click is None:
            self.tk.update()
            time.sleep(0.01)

    def get_last_click(self):
        return self._click

    def get_mouse_x(self):
        return self._mouse_x

    def get_mouse_y(self):
        return self._mouse_y

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def moveto(self, obj, x, y):
        coords = self.canvas.coords(obj)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(obj, x, y, x + width, y + height)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)

# ✅ You can remove CanvasTk completely if you're not using subclassing anymore,
# or leave it blank just for compatibility if needed:
class CanvasTk(TkCanvas):  # Just inherits directly from TkCanvas now
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
