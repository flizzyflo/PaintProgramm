import tkinter as tk
from src.Frames.ButtonFrame.ButtonFrame import ButtonFrame
from src.Settings.Settings import INITIAL_SIZE, BACKGROUND_COLOR, BUTTON_FRAME_BORDER_SIZE, CANVAS_FRAME_BORDER_SIZE
from src.Canvas.Canvas import PaintCanvas
from src.Frames.CanvasFrame.CanvasFrame import CanvasFrame

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My deluxe Paint-Program")

    bf = ButtonFrame(master=root,
                     initial_size=INITIAL_SIZE,
                     paint_canvas=None,
                     relief="groove",
                     borderwidth=BUTTON_FRAME_BORDER_SIZE)
    bf.pack(fill=tk.X,
            expand=True)

    canvas_frame = CanvasFrame(master=root,
                               relief="groove",
                               borderwidth=CANVAS_FRAME_BORDER_SIZE)
    canvas_frame.pack(fill=tk.X,
                      expand=True)

    cv = PaintCanvas(master=canvas_frame,
                     bg=BACKGROUND_COLOR,
                     size=INITIAL_SIZE)
    bf.set_canvas(cv)
    cv.pack(fill=tk.X)

    root.mainloop()
