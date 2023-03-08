import tkinter as tk
import math
from src.Settings.Settings import COLOR


class PaintCanvas(tk.Canvas):

    def __init__(self, master: tk.Tk, bg: str, size: int) -> None:

        super().__init__(master=master,
                         bg=bg)

        self.color = None
        self.set_new_color()
        self.size = size
        self.bind("<B1-Motion>", self.left_click)
        self.stack: list[int] = []

    def left_click(self, event) -> None:

        """
        Listens for click event from left mouse button. If clicked, paints oval to the canvas.
        :param event: clicking-event on the canvas
        :return: No return value
        """

        x1 = event.x - self.size
        x2 = event.x + self.size
        y1 = event.y - self.size
        y2 = event.y + self.size
        self.stack.append(self.create_oval(x1, y1, x2, y2,
                                           fill=self.color,
                                           width=math.inf))

    def undo_last_step(self) -> None:

        last_element_created = self.stack.pop()
        self.delete(last_element_created)

    @staticmethod
    def get_current_color() -> str:
        return COLOR

    def set_new_color(self, color: str = None) -> None:

        if color is None:
            self.color = self.get_current_color()

        else:
            self.color = color


    def clear_canvas(self) -> None:

        self.stack.clear()
        self.delete("all")
