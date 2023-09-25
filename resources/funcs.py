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
        