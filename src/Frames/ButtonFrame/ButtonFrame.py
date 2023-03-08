import tkinter as tk
from src.Canvas.Canvas import PaintCanvas
from src.Settings.Settings import COLORS

class ButtonFrame(tk.Frame):

    def __init__(self, master: tk.Tk,  initial_size: int, **kwargs) -> None:
        super().__init__(master=master, **kwargs)
        self.size = initial_size
        self.paint_canvas = None
        self.clear_button = tk.Button(master=self,
                                      text="Clear painting",
                                      command=lambda: self.paint_canvas.clear_canvas())
        self.clear_button.grid(row=0,
                               column=1)

        self.undo_button = tk.Button(master=self,
                                     text="Undo last step",
                                     command=lambda: self.paint_canvas.undo_last_step())
        self.undo_button.grid(row=0,
                              column=2)

        values=[str(value) for value in range(1, 21)]
        self.string_var = tk.StringVar(value=self.size)
        self.size_selection = tk.OptionMenu(self,
                                            self.string_var,
                                            *values,
                                            command=lambda x: self.set_size_value())
        self.size_selection.grid(row=0,
                                 column=3)

        color_buttons = list()
        for column_pos, color in enumerate(COLORS, start=4):
            tk.Button(master=self,
                      bg=color,
                      command=lambda: self.select_color(color=color)).grid(row=0,
                                                                           column=column_pos)
    def set_canvas(self, paint_canvas: PaintCanvas) -> None:

        self.paint_canvas = paint_canvas
        self.paint_canvas.grid(row=1,
                               column=1,
                               columnspan=3)

    def set_size_value(self) -> None:
        pencil_size=self.string_var.get()
        self.paint_canvas.size = int(pencil_size)


    def select_color(self, color) -> None:
        self.paint_canvas.set_new_color(color=color)
