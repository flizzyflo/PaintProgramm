import tkinter as tk
import math
from src.Settings.Settings import COLOR
from src.Frames.CanvasFrame.CanvasFrame import CanvasFrame


class PaintCanvas(tk.Canvas):

    def __init__(self, master: CanvasFrame, bg: str, size: str, **kwargs) -> None:

        super().__init__(master=master,
                         bg=bg,
                         **kwargs)

        self.color = None
        self.set_new_color()
        self.size = int(size)
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

        """
        Deletes the last object which is created to be shown on the canvas object.
        Deletes the elements according to the order stored in the 'stack' list.
        Pops elements until list is empty

        :return: Nothing
        """

        if self.stack:
            last_element_created = self.stack.pop()
            self.delete(last_element_created)

        else:
            print("Nothing to be undone...")

    @staticmethod
    def get_current_color() -> str:

        """Returns the color value which is stored within the color variable in the settings as initial value."""

        return COLOR

    def set_new_color(self, color: str = None) -> None:

        """
        Method to set new color for creating objects within the canvas. Sets the instance variable
        color according to the value passed in. If 'None' as value is passed it, it sets the initial value
        from the settings file as color.
        :param color: string literal for color
        :return: Nothing
        """

        if color is None:
            self.color = self.get_current_color()

        else:
            self.color = color

    def clear_canvas(self) -> None:

        """
        Clears everything which is painted on the canvas instance.
        :return: Nothing
        """

        self.stack.clear()
        self.delete("all")
