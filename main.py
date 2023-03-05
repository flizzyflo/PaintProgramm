import tkinter as tk
import math

from src.Canvas.Canvas import PaintCanvas

if __name__ == '__main__':
    root = tk.Tk()
    root.title("PaintProgramm")
    cv = PaintCanvas(master=root,
                     bg="White",
                     size=15)


    cv.pack()
    tk.Button(master=root, text="clear", command=lambda: cv.clear_canvas()).pack()
    tk.Button(master=root, text="undo", command=lambda: cv.undo_last_step()).pack()

    root.mainloop()