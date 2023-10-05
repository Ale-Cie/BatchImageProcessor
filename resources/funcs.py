import subprocess

from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size



def open_directory(directory_name):
    """
    This simple function serves as a command to two different buttons.
    If either of the buttons is pressed a specified folder within './user/' directory opens in a new window.
    """

    try:
        subprocess.run(["start", f"./{directory_name}"])
    except:
        subprocess.run(["open", f"./{directory_name}"])
        
def clear_dimensions(width, height, proportions):
    cleared_width = "1"
    cleared_height = "1"
    cleared_proportions = "free"
    return width.set(cleared_width), height.set(cleared_height), proportions.set(cleared_proportions)

# def quick_filter():
#     from PIL import Image, ImageFilter
#     from PIL.ImageFilter import (
#    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
#    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
# )

#     img = Image.open("./resources/images/filters/preview.png")
#     for filter in [BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN]:
#         img_filter = img.filter(filter)
#         filter_name = filter.name
#         img_filter.save(f"./resources/images/filters/preview{filter_name}.png")