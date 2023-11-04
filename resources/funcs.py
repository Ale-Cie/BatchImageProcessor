import subprocess
import os
import datetime

from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size
from time import sleep


def open_directory(directory_name, input_path=None, processed_files_frame=None):
    """
    This simple function serves as a command to two different buttons.
    If either of the buttons is pressed a specified folder within './user/' directory opens in a new window.
    """

    try:
        subprocess.run(["start", f"./{directory_name}"])
    except:
        subprocess.run(["open", f"./{directory_name}"])

    if input_path and processed_files_frame:
        path = "./input_folder"
        input_path.set(path)
        processed_files_frame.track_progress()


def select_input_path(input_path, processed_files_frame):
    selected_path = filedialog.askdirectory()
    if selected_path != "":
        input_path.set(selected_path)
        y = len(os.listdir(input_path.get()))
        processed_files_frame.track_progress(
            y=y, state="waiting", path=input_path.get())
    else:
        pass


def clear_dimensions(width, height, proportions, height_field, selected_resizing_label):
    cleared_width = "10"
    cleared_height = "10"
    cleared_proportions = "free"
    width.set(cleared_width)
    height.set(cleared_height)
    proportions.set(cleared_proportions)
    height_field["state"] = "!disabled"
    schedule_resize(selected_resizing_label, mode="clear")


def schedule_extension(extension, selected_extension_label):
    selected_extension_label["text"] = extension


def schedule_resize(selected_resizing_label, width=10, height=10, mode="schedule"):
    if mode == "schedule":
        selected_resizing_label["text"] = f"{width} X {height}"
    elif mode == "clear":
        selected_resizing_label["text"] = "None"
    else:
        pass


def schedule_filter(filter, selected_filter_label):
    selected_filter_label["text"] = filter


def show_preview(filter, preview_label):
    preview_img = PhotoImage(
        file=f"./resources/images/filters/{filter}.png").subsample(2, 2)
    preview_label.configure(image=preview_img)
    preview_label.image = preview_img


def clear_filters(filter, preview_label, selected_filter_label):
    filter.set("None")
    show_preview("preview", preview_label)
    schedule_filter(filter.get(), selected_filter_label)


def clear_extension(extension, selected_extension_label):
    extension.set("None")
    selected_extension_label["text"] = "None"


def force_proportions(proportions, width, height, height_field):
    if proportions != "free":
        x, y = proportions.split(":")
        calcualted_height = int(int(width) * int(y) / int(x))
        height.set(calcualted_height)
        height_field.text = str(height.get())
        height_field["state"] = "disabled"
    else:
        height_field["state"] = "!disabled"


def save_image(img, output_path, file_name, extension):
    try:
        img.save(f"{output_path}/{file_name}.{extension}", extension)
    except:
        img.save(f"{output_path}/{file_name}{extension}", extension[1:])


def process_images(input_path, output_path, extension, filter, resizing, processed_files_frame):
    from PIL import Image
    import PIL.ImageFilter as filters

    none_tasks = 0
    for task in [extension, filter, resizing]:
        none_tasks += 1 if task == "None" else 0
    filters_dict = {
        "BLUR": filters.BLUR,
        "CONTOUR": filters.CONTOUR,
        "DETAIL": filters.DETAIL,
        "EDGE_ENHANCE": filters.EDGE_ENHANCE,
        "EDGE_ENHANCE_MORE": filters.EDGE_ENHANCE_MORE,
        "EMBOSS": filters.EMBOSS,
        "FIND_EDGES": filters.FIND_EDGES,
        "SMOOTH": filters.SMOOTH,
        "SMOOTH_MORE": filters.SMOOTH_MORE,
        "SHARPEN": filters.SHARPEN
    }
    processed_images = 0
    omitted_files = []
    num_images = len(os.listdir(input_path))
    state = ""
    for file in os.listdir(input_path):
        try:
            img = Image.open(f"{input_path}/{file}")
            file_name = file.split(".")[0]
            if resizing != "None":
                width, height = resizing.replace(" ", "").split("X")
                img = img.resize((int(width), int(height)))
            if filter != "None":
                img = img.filter(filters_dict[filter])
            if extension != "None":
                processed_images += 1
                save_image(img, output_path, file_name, extension)
                state = "done"
            else:
                if none_tasks != 3:
                    ext = file.split(".")[1] if file.split(".")[
                        1] != "jpg" else "jpeg"
                    save_image(img, output_path, file_name, ext)
                    state = "done"
                else:
                    state = "error"
                    break
        except:
            omitted_files.append(file)

    if num_images != len(omitted_files):
        processed_files_frame.track_progress(
            x=processed_images, y=len(omitted_files), state=state)
    else:
        processed_files_frame.track_progress(
            y=len(omitted_files), state="all_omitted")

    if len(omitted_files) != 0:
        with open(f"{output_path}/omitted_files.txt", "w+") as log_file:
            head = f"BIP Session {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} - List of {len(omitted_files)} omitted files\n\n"
            if num_images == len(omitted_files):
                head += f"Selected extension - {extension}\n\n"
            body = "\n".join(omitted_files)
            log_file.writelines(head+body)


def app_rescaling(frame, grid_size):
    try:
        columns, rows = grid_size
        for idx in range(columns):
            frame.columnconfigure(idx, weight=3)
        for idx in range(rows):
            frame.rowconfigure(idx, weight=3)
    except:
        pass


def app_init(app_version="0.2.0", display_message=None, mode="new"):
    config_dict = {}
    if mode == "edit":
        with open("./resources/config.ini", "w") as config:
            new_config = [
                f"version:{app_version}",
                f"display_message:{display_message}"
            ]
            text = "\n".join(new_config)
            config.write(text)
    elif mode == "new":
        try:
            with open("./resources/config.ini", "r") as config:
                for line in config.readlines():
                    key, value = line.split(":")
                    config_dict[key] = value
                return config_dict
        except:
            with open("./resources/config.ini", "w") as config:
                if mode == "new":
                    new_config = [
                        f"version:{app_version}",
                        f"display_message:True"
                    ]
                    text = "\n".join(new_config)
                    config.writelines(text)
                    for line in new_config:
                        key, value = line.split(":")
                        config_dict[key] = value
                return config_dict
