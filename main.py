import tkinter as tk
from src.Frames.ButtonFrame.ButtonFrame import ButtonFrame
from src.Settings.Settings import INITIAL_SIZE, BACKGROUND_COLOR
from src.Canvas.Canvas import PaintCanvas

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My deluxe Paint-Programm")
    bf = ButtonFrame(master=root,
                     initial_size=INITIAL_SIZE,
                     paint_canvas=None)

    cv = PaintCanvas(master=root,
                     bg=BACKGROUND_COLOR,
                     size=INITIAL_SIZE)
    bf.set_canvas(cv)

    bf.grid(row=0,
            column=0)
    cv.grid(row=1,
            column=0,
            sticky="NSWE")

    print(cv.get_current_color())

    print(cv.get_current_color())


    root.mainloop()
