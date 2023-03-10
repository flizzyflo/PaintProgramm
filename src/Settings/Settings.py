BUTTON_START_POSITION: int = 5
BUTTON_FRAME_BORDER_SIZE: int = 2
CANVAS_FRAME_BORDER_SIZE: int = 6

COLOR: str = "Black"
BACKGROUND_COLOR: str = "White"
COLORS: list[str] = ["Red", "Green", "Blue", "Purple", "Black", "Yellow", "Brown", "Orange", "Lightgreen"]
INITIAL_SIZE: str = "8"


def get_initial_color() -> str:

    """
    Returns the color value which is stored within the color variable in the settings as initial value.
    :return: The constant color as string
    """

    return COLOR
