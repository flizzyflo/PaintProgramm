import tkinter as tk
from src.Frames.ButtonFrame.ButtonFrame import ButtonFrame
from src.Settings.Settings import INITIAL_SIZE
from src.Canvas.Canvas import PaintCanvas

if __name__ == '__main__':
    root = tk.Tk()
    root.title("PaintProgramm")
    bf = ButtonFrame(master=root,
                     initial_size=INITIAL_SIZE,
                     paint_canvas=None)

    cv = PaintCanvas(master=root, bg="White", size=INITIAL_SIZE)
    bf.set_canvas(cv)

    bf.grid(row=0,
            column=0)
    cv.grid(row=1,
            column=0,
            sticky="NSWE")
    root.mainloop()