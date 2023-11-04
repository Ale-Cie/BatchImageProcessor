import os
import subprocess

from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size

from resources import funcs, classes

root = Tk()

# Variables
width, height = size()
width_multiplier = int(width)/1440
height_multiplier = int(height)/900
input_path = StringVar()
output_path = StringVar()
config_dict = funcs.app_init()
display_message = config_dict["display_message"]
app_version = config_dict["version"]
root.title(f"BatchImageProcessor v. {app_version}")

input_path.set("./input_folder")
output_path.set("./output_folder")

# Frames
controls = ttk.LabelFrame(root)
display = ttk.LabelFrame(root)
scheduled_tasks = ttk.LabelFrame(root)
processed_files_frame = classes.ProcessedFiles(root)
mainframe = ttk.Notebook(display)
selected_extension = ttk.Label(scheduled_tasks, text="None")
selected_resizing = ttk.Label(scheduled_tasks, text="None")
selected_filter = ttk.Label(scheduled_tasks, text="None")
extensions_frame = classes.ExtensionsFrame(mainframe, selected_extension)
resizing_frame = classes.ResizingFrame(mainframe, selected_resizing)
filters_frame = classes.FiltersFrame(mainframe, selected_filter)


# Widgets
default_input_img = PhotoImage(
    file="./resources/images/default_input.png").subsample(2, 2)
input_img = PhotoImage(
    file="./resources/images/input_button.png").subsample(2, 2)
output_img = PhotoImage(
    file="./resources/images/output_button.png").subsample(2, 2)
process_img = PhotoImage(
    file="./resources/images/process_button.png").subsample(2, 2)
# begin_img = PhotoImage(
#     file="./resources/images/begin_button.png").subsample(1, 1)
# welcome_banner = PhotoImage(
#     file="./resources/images/bip_banner.png").subsample(1, 1)
default_input = Button(controls, image=default_input_img,
                       command=lambda: funcs.open_directory("input_folder", input_path, processed_files_frame))
input_selector = Button(controls, image=input_img,
                        command=lambda: funcs.select_input_path(input_path, processed_files_frame))
output_folder = Button(controls, image=output_img,
                       command=lambda: funcs.open_directory("output_folder"))
extension_label = ttk.Label(scheduled_tasks, text="Selected Extension: ")
resizing_label = ttk.Label(scheduled_tasks, text="Resizing Values:")
filter_label = ttk.Label(scheduled_tasks, text="Selected Filter: ")
process_button = Button(scheduled_tasks, image=process_img, command=lambda: funcs.process_images(
    input_path.get(), output_path.get(), selected_extension["text"], selected_filter["text"], selected_resizing["text"], processed_files_frame))
# spacer = ttk.Label(root)
# banner_label = ttk.Label(welcome_screen, image=welcome_banner)
# welcome_spacer = ttk.Label(welcome_screen)
# begin_button = Button(welcome_screen, image=begin_img,
#                       command=lambda: welcome_screen.destroy())

# Setup
display.grid(column=1, row=0, sticky=(N, S, W))
controls.grid(column=0, row=0, sticky=(N, S, W))
scheduled_tasks.grid(column=2, row=0, sticky=(N, S, E, W))
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.add(extensions_frame, text="Change Extensions")
mainframe.add(resizing_frame, text="Resize Images")
mainframe.add(filters_frame, text="Apply Filters")
default_input.grid(column=1, row=0)
input_selector.grid(column=1, row=1, sticky=(S, E, W))
output_folder.grid(column=1, row=2, sticky=(N, E, W))
extension_label.grid(column=0, row=0, sticky=(N, S, E, W))
selected_extension.grid(column=0, row=1, sticky=(N, S, E, W))
resizing_label.grid(column=0, row=2, sticky=(N, S, E, W))
selected_resizing.grid(column=0, row=3, sticky=(N, S, E, W))
filter_label.grid(column=0, row=4, sticky=(N, S, E, W))
selected_filter.grid(column=0, row=5, sticky=(N, S, E, W))
process_button.grid(column=0, row=6)
# spacer.grid(column=0, row=1, columnspan=3)
processed_files_frame.grid(column=0, row=1, sticky=(N, S, E, W), columnspan=3)
# banner_label.grid(column=0, row=0)
# welcome_spacer.grid(column=0, row=1, rowspan=3)
# begin_button.grid(column=0, row=4, sticky=(S))


display.columnconfigure(0, weight=3)
display.columnconfigure(1, weight=3)
display.rowconfigure(0, weight=3)
controls.columnconfigure(0, weight=3)
controls.rowconfigure(0, weight=3)
controls.rowconfigure(1, weight=3)


for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)
    for sub_child in child.winfo_children():
        sub_child.grid_configure(padx=5, pady=5)

controls.grid_configure(pady=0)
display.grid_configure(padx=0, pady=0)
scheduled_tasks.grid_configure(pady=0)

processed_files_frame.grid_configure(pady=2)

for child in scheduled_tasks.winfo_children():
    child.grid_configure(pady=15)

funcs.app_rescaling(root, root.grid_size())
for child in root.winfo_children():
    funcs.app_rescaling(child, child.grid_size())

# root.minsize(width=850, height=620)
root.minsize(width=int(850*width_multiplier),
             height=int(625*height_multiplier))

if display_message == "True":
    welcome_screen = classes.WelcomeScreen(
        root, width_multiplier, app_version)
    welcome_screen.grid(column=0, row=0, sticky=(
        N, S, E, W), rowspan=2, columnspan=3)
    welcome_screen.columnconfigure(0, weight=3)
    welcome_screen.grid_configure(pady=0)

root.mainloop()
