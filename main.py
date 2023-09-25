import os
import subprocess

from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size

from resources import funcs, classes

app_version = "0.1.0"

root = Tk()
root.title(f"BatchImageProcessor v. {app_version}")

# Variables
width, height = size()
width_multiplier = int(width)/1440
height_multiplier = int(height)/900
input_path = StringVar()
output_folder = StringVar()

# Frames
controls = ttk.LabelFrame(root)
display = ttk.LabelFrame(root)
scheduled_tasks = ttk.LabelFrame(root)
mainframe = ttk.Notebook(display)
extensions_frame = classes.ExtensionsFrame(mainframe)
filters_frame = classes.FiltersFrame(mainframe)


# Widgets
input_img = PhotoImage(file="./resources/images/input_button.png").subsample(2, 2)
output_img = PhotoImage(file="./resources/images/output_button.png").subsample(2, 2)
process_img = PhotoImage(file="./resources/images/process_button.png").subsample(2, 2)

input_selector = Button(controls, image= input_img, command=lambda: input_path.set(filedialog.askdirectory()))
output_folder = Button(controls, image= output_img, command=lambda: funcs.open_directory("output_folder"))
extension_label = ttk.Label(scheduled_tasks, text= "Selected Extension: ")
selected_extension = ttk.Label(scheduled_tasks, text= "None",)
filter_label = ttk.Label(scheduled_tasks, text= "Selected Filter: ")
selected_filter = ttk.Label(scheduled_tasks, text= "None",)
process_button = Button(scheduled_tasks, image= process_img)
spacer = ttk.Label(root)
progress_bar = ttk.Progressbar(root)

# Setup
display.grid(column= 1, row= 0, sticky= (N,S,W))
controls.grid(column=0, row=0, sticky= (N,S,W))
scheduled_tasks.grid(column= 2, row= 0, sticky= (N,S,E,W))
mainframe.grid(column= 0, row=0, sticky= (N,S,E,W))
mainframe.add(extensions_frame, text= "Change Extensions")
mainframe.add(filters_frame, text= "Apply Filters")
input_selector.grid(column= 1, row= 0, sticky= (S,E,W))
output_folder.grid(column= 1, row= 1, sticky= (N,E,W))
extension_label.grid(column=0, row= 0, sticky= (N,S,E,W))
selected_extension.grid(column= 0, row= 1, sticky= (N,S,E,W))
filter_label.grid(column= 0, row= 2, sticky= (N,S,E,W))
selected_filter.grid(column= 0, row= 3, sticky= (N,S,E,W))
process_button.grid(column= 0, row= 4)
spacer.grid(column= 0, row= 1, columnspan= 3)
progress_bar.grid(column= 0, row= 2, sticky= (N,S,E,W), columnspan= 3)


display.columnconfigure(0, weight=3)
display.columnconfigure(1, weight= 3)
display.rowconfigure(0, weight= 3)
controls.columnconfigure(0, weight= 3)
controls.rowconfigure(0, weight= 3)
controls.rowconfigure(1, weight= 3)

for child in root.winfo_children():
    child.grid_configure(padx= 5, pady= 5)
    for sub_child in child.winfo_children():
        sub_child.grid_configure(padx= 5, pady= 5)

controls.grid_configure(pady= 0)
display.grid_configure(padx= 0, pady=0)
scheduled_tasks.grid_configure(pady= 0)
spacer.grid_configure(pady= 0)
progress_bar.grid_configure(padx= 20, pady= 0)

for child in scheduled_tasks.winfo_children():
    child.grid_configure(pady= 20)


root.minsize(width=850, height=560)
root.maxsize(width=850, height=560)

root.mainloop()