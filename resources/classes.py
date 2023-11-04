import subprocess
import os

from math import ceil
from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size
from PIL import Image, ImageTk

from resources import funcs


class ExtensionsFrame(ttk.Frame):
    def __init__(self, parent, selected_extension_label):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.extension = StringVar()
        self.extension.set("None")
        self.selected_extension_label = selected_extension_label

        label_text = "If you need a uniform extension for a collection of images, pick\none of the file formats below and press 'Schedule Tasks'.\nWhen you later on click 'Process Images' changes will apply."
        self.banner = PhotoImage(
            file="./resources/images/extension_manager.png")
        self.clear = PhotoImage(
            file="./resources/images/clear_button.png").subsample(2, 2)
        self.banner_frame = ttk.Frame(self)
        self.image_label = ttk.Label(self.banner_frame, image=self.banner)
        self.description_frame = ttk.Label(
            self, text=label_text, justify="center")
        self.basic_checkboxes_frame = ttk.Frame(self)
        self.other_checkboxes_frame = ttk.Frame(self)
        self.schedule_img = PhotoImage(
            file="./resources/images/schedule_task.png").subsample(2, 2)
        self.schedule_button = Button(self, image=self.schedule_img, command=lambda: funcs.schedule_extension(
            self.extension.get(), self.selected_extension_label))
        self.clear_button = Button(
            self, image=self.clear, command=lambda: funcs.clear_extension(self.extension, self.selected_extension_label))

        self.basic_checkboxes_creator()
        self.other_checkboxes_creator()
        self.frame_setup()

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def basic_checkboxes_creator(self):
        basic_formats = ttk.Label(
            self.basic_checkboxes_frame, text="Available file formats:", font="TkSmallCaptionFont")
        jpg_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="JPEG", variable=self.extension, value=".jpeg")
        png_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="PNG", variable=self.extension, value=".png")
        bmp_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="BMP", variable=self.extension, value=".bmp")
        tiff_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="TIFF", variable=self.extension, value=".tiff")
        gif_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="GIF", variable=self.extension, value=".gif")
        ico_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="ICO", variable=self.extension, value=".ico")
        icns_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="ICNS", variable=self.extension, value=".icns")
        webp_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="WEBP", variable=self.extension, value=".webp")
        pdf_box = ttk.Radiobutton(
            self.basic_checkboxes_frame, text="PDF", variable=self.extension, value=".pdf")

        basic_boxes = [jpg_box, png_box, bmp_box, tiff_box,
                       gif_box, ico_box, icns_box, webp_box, pdf_box]
        basic_formats.grid(column=0, row=0, columnspan=3)

        column_length = ceil(len(basic_boxes) / 3)
        column_idx, row_idx = 0, 1

        for box in basic_boxes:
            try:
                if row_idx != column_length:
                    box.grid(column=column_idx, row=row_idx,
                             sticky=(N, S, E, W))
                    row_idx += 1
                else:
                    box.grid(column=column_idx, row=row_idx,
                             sticky=(N, S, E, W))
                    row_idx = 1
                    column_idx += 1
            except:
                pass

    def other_checkboxes_creator(self):
        other_formats = ttk.Label(
            self.other_checkboxes_frame, text="Other file formats:", font="TkSmallCaptionFont")
        blp_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="BLP", variable=self.extension, value=".blp")
        dds_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="DDS", variable=self.extension, value=".dds")
        dib_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="DIB", variable=self.extension, value=".dib")
        im_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="IM", variable=self.extension, value=".im")
        ppm_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="PPM", variable=self.extension, value=".ppm")
        sgi_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="SGI", variable=self.extension, value=".sgi")
        spider_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="SPIDER", variable=self.extension, value=".spider")
        tga_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="TGA", variable=self.extension, value=".tga")
        xbm_box = ttk.Radiobutton(
            self.other_checkboxes_frame, text="XBM", variable=self.extension, value=".xbm")

        other_boxes = [blp_box, dds_box, dib_box, im_box,
                       ppm_box, sgi_box, tga_box, xbm_box, spider_box]
        other_formats.grid(column=0, row=0, columnspan=3)

        column_length = ceil(len(other_boxes) / 3)
        column_idx, row_idx = 0, 1

        for box in other_boxes:
            try:
                if row_idx != column_length:
                    box.grid(column=column_idx, row=row_idx,
                             sticky=(N, S, E, W))
                    row_idx += 1
                else:
                    box.grid(column=column_idx, row=row_idx,
                             sticky=(N, S, E, W))
                    row_idx = 1
                    column_idx += 1
            except:
                pass

    def frame_setup(self):
        self.banner_frame.grid(column=0, row=0, columnspan=2)
        self.image_label.grid(column=0, row=0)
        self.description_frame.grid(column=0, row=1, columnspan=2)
        self.basic_checkboxes_frame.grid(column=0, row=2, sticky=(N, S, E, W))
        self.other_checkboxes_frame.grid(column=1, row=2, sticky=(N, S, E, W))
        self.schedule_button.grid(column=1, row=3)
        self.clear_button.grid(column=0, row=3)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=3)

        for child in self.basic_checkboxes_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in self.other_checkboxes_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.banner_frame.grid_configure(padx=0)


class FiltersFrame(ttk.Frame):
    def __init__(self, parent, selected_filters_label):
        ttk.Frame.__init__(self, parent)
        self.filter = StringVar()
        self.selected_filters_label = selected_filters_label
        label_text = "If you want to apply a filter to an entire collection of images, pick\none of the filters listed below and press 'Schedule Tasks'.\nWhen you later on click 'Process Images' changes will apply."
        self.banner = PhotoImage(file="./resources/images/filters_manager.png")
        self.preview = PhotoImage(
            file="./resources/images/filters/preview.png").subsample(2, 2)
        self.schedule = PhotoImage(
            file="./resources/images/schedule_task.png").subsample(2, 2)
        self.clear = PhotoImage(
            file="./resources/images/clear_button.png").subsample(2, 2)
        self.banner_frame = ttk.Frame(self)
        self.image_label = ttk.Label(self.banner_frame, image=self.banner)
        self.description_label = ttk.Label(
            self, text=label_text, justify="center")
        self.checkboxes_frame = ttk.Frame(self)
        self.preview_frame = ttk.Frame(self)
        self.preview_label = ttk.Label(self.preview_frame, image=self.preview)
        self.schedule_button = Button(self, image=self.schedule, command=lambda: funcs.schedule_filter(
            self.filter.get(), self.selected_filters_label))
        self.clear_button = Button(self, image=self.clear, command=lambda: funcs.clear_filters(
            self.filter, self.preview_label, self.selected_filters_label))

        self.checkboxes_creator()
        self.frame_setup()

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def checkboxes_creator(self):
        header_label = ttk.Label(
            self.checkboxes_frame, text="Available filters:", font="TkSmallCaptionFont")
        blur_box = ttk.Radiobutton(self.checkboxes_frame, text="BLUR", variable=self.filter,
                                   value="BLUR", command=lambda: funcs.show_preview("BLUR", self.preview_label))
        contour_box = ttk.Radiobutton(self.checkboxes_frame, text="CONTOUR", variable=self.filter,
                                      value="CONTOUR", command=lambda: funcs.show_preview("CONTOUR", self.preview_label))
        detail_box = ttk.Radiobutton(self.checkboxes_frame, text="DETAIL", variable=self.filter,
                                     value="DETAIL", command=lambda: funcs.show_preview("DETAIL", self.preview_label))
        enhance_box = ttk.Radiobutton(self.checkboxes_frame, text="EDGE ENHANCE", variable=self.filter,
                                      value="EDGE_ENHANCE", command=lambda: funcs.show_preview("EDGE_ENHANCE", self.preview_label))
        enhance_more_box = ttk.Radiobutton(self.checkboxes_frame, text="EDGE ENHANCE MORE", variable=self.filter,
                                           value="EDGE_ENHANCE_MORE", command=lambda: funcs.show_preview("EDGE_ENHANCE_MORE", self.preview_label))
        emboss_box = ttk.Radiobutton(self.checkboxes_frame, text="EMBOSS", variable=self.filter,
                                     value="EMBOSS", command=lambda: funcs.show_preview("EMBOSS", self.preview_label))
        find_edges_box = ttk.Radiobutton(self.checkboxes_frame, text="FIND EDGES", variable=self.filter,
                                         value="FIND_EDGES", command=lambda: funcs.show_preview("FIND_EDGES", self.preview_label))
        sharpen_box = ttk.Radiobutton(self.checkboxes_frame, text="SHARPEN", variable=self.filter,
                                      value="SHARPEN", command=lambda: funcs.show_preview("SHARPEN", self.preview_label))
        smooth_box = ttk.Radiobutton(self.checkboxes_frame, text="SMOOTH", variable=self.filter,
                                     value="SMOOTH", command=lambda: funcs.show_preview("SMOOTH", self.preview_label))
        smooth_more_box = ttk.Radiobutton(self.checkboxes_frame, text="SMOOTH MORE", variable=self.filter,
                                          value="SMOOTH_MORE", command=lambda: funcs.show_preview("SMOOTH_MORE", self.preview_label))

        boxes = [blur_box, contour_box, detail_box, enhance_box,
                 emboss_box, find_edges_box, sharpen_box, smooth_box]
        column_idx, row_idx = 0, 1

        header_label.grid(column=0, row=0, columnspan=2)
        for box in boxes:
            if row_idx != 4:
                box.grid(column=column_idx, row=row_idx, sticky=(N, S, E, W))
                row_idx += 1
            else:
                box.grid(column=column_idx, row=row_idx, sticky=(N, S, E, W))
                row_idx = 1
                column_idx = 1

        enhance_more_box.grid(
            column=0, row=5, columnspan=2, sticky=(N, S, E, W))
        smooth_more_box.grid(
            column=0, row=6, columnspan=2, sticky=(N, S, E, W))

    def frame_setup(self):
        self.banner_frame.grid(column=0, row=0, columnspan=2)
        self.image_label.grid(column=0, row=0)
        self.description_label.grid(column=0, row=1, columnspan=2)
        self.checkboxes_frame.grid(column=0, row=2)
        self.preview_frame.grid(column=1, row=2)
        self.preview_label.grid(column=0, row=0)
        self.schedule_button.grid(column=1, row=3, rowspan=2)
        self.clear_button.grid(column=0, row=3)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=3)


class ResizingFrame(ttk.Frame):
    def __init__(self, parent, selected_resizing):
        ttk.Frame.__init__(self, parent)
        self.proportions = StringVar()
        self.width = StringVar()
        self.height = StringVar()
        self.width.set("10")
        self.height.set("10")

        self.proportions.set("free")
        self.selected_resizing = selected_resizing
        self.banner = PhotoImage(
            file="./resources/images/resizing_manager.png")
        self.schedule = PhotoImage(
            file="./resources/images/schedule_task.png").subsample(2, 2)
        self.clear = PhotoImage(
            file="./resources/images/clear_button.png").subsample(2, 2)
        self.banner_frame = ttk.Frame(self)
        self.banner_label = ttk.Label(self.banner_frame, image=self.banner)
        description_label = "If you want to resize an entire collection of images, put the\ndimensions below, select proportions and press 'Schedule Tasks'.\nWhen you later on click 'Process Images' changes will apply."
        self.description_label = ttk.Label(
            self, text=description_label, justify="center")
        self.values_frame = ttk.Frame(self)
        self.proportions_frame = ttk.Frame(self, width=20)
        self.error_text = ""
        self.error_label = ttk.Label(self, text=self.error_text)
        self.schedule_button = Button(self, image=self.schedule, command=lambda: funcs.schedule_resize(self.selected_resizing,
                                                                                                       self.width.get(), self.height.get()))
        self.clear_button = Button(self, image=self.clear, command=lambda: funcs.clear_dimensions(
            self.width, self.height, self.proportions, self.height_field, self.selected_resizing))

        self.resizing_setup()
        self.proportions_setup()
        self.frame_setup()

        self.width_field.focus()
        self.width_field.bind("<Return>", self.update_height)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def resizing_setup(self):

        self.resizing_label = ttk.Label(
            self.values_frame, text="Set Width & Height\nPress RETURN to save input", font="TkSmallCaptionFont", justify="center")
        self.width_label = ttk.Label(self.values_frame, text="Width:")
        self.by_label = ttk.Label(
            self.values_frame, text="X", justify="center")
        self.height_label = ttk.Label(self.values_frame, text="Height:")
        self.width_field = ttk.Entry(
            self.values_frame, textvariable=self.width, width=5)
        self.height_field = ttk.Entry(
            self.values_frame, textvariable=self.height, width=5)
        self.height_field.text = funcs.force_proportions(
            self.proportions.get(), self.width.get(), self.height, self.height_field)

        self.resizing_label.grid(
            column=0, row=0, columnspan=2, sticky=(N, S, E, W))
        self.width_label.grid(column=0, row=1)
        self.width_field.grid(column=1, row=1)
        self.by_label.grid(column=0, row=2, columnspan=2)
        self.height_label.grid(column=0, row=3)
        self.height_field.grid(column=1, row=3)

    def proportions_setup(self):
        self.proportions_label = ttk.Label(
            self.proportions_frame, text="Select Proportions", font="TkSmallCaptionFont")
        freeform_box = ttk.Radiobutton(self.proportions_frame, text="Free", variable=self.proportions, value="free",
                                       command=lambda: funcs.force_proportions(self.proportions.get(), self.width.get(), self.height, self.height_field))
        one_by_one_box = ttk.Radiobutton(self.proportions_frame, text=" 1:1 ", variable=self.proportions, value="1:1",
                                         command=lambda: funcs.force_proportions(self.proportions.get(), self.width.get(), self.height, self.height_field))
        three_by_four_box = ttk.Radiobutton(self.proportions_frame, text=" 3:4 ", variable=self.proportions, value="3:4",
                                            command=lambda: funcs.force_proportions(self.proportions.get(), self.width.get(), self.height, self.height_field))
        four_by_five_box = ttk.Radiobutton(self.proportions_frame, text=" 4:5 ", variable=self.proportions, value="4:5",
                                           command=lambda: funcs.force_proportions(self.proportions.get(), self.width.get(), self.height, self.height_field))
        sixteen_by_nine = ttk.Radiobutton(self.proportions_frame, text=" 16:9", variable=self.proportions, value="16:9",
                                          command=lambda: funcs.force_proportions(self.proportions.get(), self.width.get(), self.height, self.height_field))

        self.proportions_label.grid(column=0, row=0)
        freeform_box.grid(column=0, row=1)
        one_by_one_box.grid(column=0, row=2)
        three_by_four_box.grid(column=0, row=3)
        four_by_five_box.grid(column=0, row=4)
        sixteen_by_nine.grid(column=0, row=5)

    def frame_setup(self):
        self.banner_frame.grid(column=0, row=0, columnspan=2)
        self.banner_label.grid(column=0, row=0)
        self.description_label.grid(column=0, row=1, columnspan=2)
        self.values_frame.grid(column=0, row=2)
        self.proportions_frame.grid(column=1, row=2, )
        self.clear_button.grid(column=0, row=3)
        self.schedule_button.grid(column=1, row=3)
        self.error_label.grid(column=0, row=4, columnspan=2)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=3)

    def update_height(self, event):
        funcs.force_proportions(self.proportions.get(
        ), self.width.get(), self.height, self.height_field)


class ProcessedFiles(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent)
        self.parent = parent

        self.processed_label = ttk.Label(
            self, text="Temporary", justify="center")

        self.track_progress(0, )
        self.frame_setup()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=0)

    def frame_setup(self):
        self.processed_label.grid(column=0, row=0)

        self.columnconfigure(0, weight=3)
        self.rowconfigure(0, weight=3)

    def track_progress(self, x=0, y=0, state=None, path=None):
        match state:
            case "waiting":
                self.processed_label["text"] = f"There are {y} files waiting to be processed in the {path} directory."
            case "done":
                if y != 0:
                    self.processed_label["text"] = f"Processing done. {x} processed files saved to Output Folder, {y} omitted files' names saved to a .txt log."
                else:
                    self.processed_label["text"] = f"Processing done. {x} processed files saved to Output Folder"
            case "error":
                self.processed_label["text"] = "Please schedule at least one task to start processing the images."
            case "all_omitted":
                self.processed_label["text"] = f"An error occured. All {y} files were omitted. Saved a log to the Output Folder"
            case _:
                y = len(os.listdir("./input_folder"))
                self.processed_label[
                    "text"] = f"Currently accessing the default input folder. There are {y} files within this directory."


class WelcomeScreen(ttk.Frame):

    def __init__(self, parent, width_multiplier, app_version):
        ttk.Frame.__init__(self, parent)

        img = Image.open("./resources/images/bip_banner.png")
        banner_ratio = img.height/img.width
        img_width = int(820*width_multiplier)
        img = img.resize((img_width, int(banner_ratio*img_width)))
        message = """Welcome to the 0.2.0 version of BatchImageProcessor!

As of 1st of November 2023 I am proud to introduce you to the first fully usable version of BIP! After some time off work I spent making sure that
the app works correctly on Mac computers I can finally release a version I am proud of. Although it's not much, there are only three functions it 
provides, the looks of the app could be made better and there are probably ways to optimize the code I'm releasing it! Here is the list of all the
new features that the version 0.2.0 provides:

    1. With the first launch of the app a 'config.ini' file is created and it will remember user settings (for now it's only the decision to 
        show/hide this screen on start).
    2. You can select extension which you'd like to apply to all pictures provided.
    3. Now the resizing tab actually works and you can select from one of the width to height ratios.
    4. Applying filters is now a thing, the preview picture changed to something that represents the filters better.
    5. Scheduling at least one task makes processing possible, no tasks = no processing.
    6. For now, the outputs are saved in the './output_folder' in app's main directory.
    7. You can select any folder to be an input folder or use the default './input_folder'.
    
Thank you for your attention, now let's allow BatchImageProcessor to speak for itself!"""
        self.display_message = StringVar()
        self.welcome_banner = ImageTk.PhotoImage(img)
        self.begin_img = PhotoImage(
            file="./resources/images/begin_button.png").subsample(1, 1)

        self.banner_label = ttk.Label(
            self, image=self.welcome_banner)
        self.display_frame = ttk.LabelFrame(self)
        self.message = ttk.Label(
            self.display_frame, text=message, justify="center")
        self.display_checkbox = ttk.Checkbutton(
            self, text="Don't show this screen again.", variable=self.display_message, onvalue="False", offvalue="True", command=lambda: funcs.app_init(app_version, self.display_message.get(), "edit"))
        self.begin_button = Button(self, image=self.begin_img,
                                   command=lambda: (self.destroy()))

        self.banner_label.grid(column=0, row=0)
        self.display_frame.grid(
            column=0, row=1, rowspan=2, sticky=(N, S))
        self.display_checkbox.grid(column=0, row=3, sticky=(S))
        self.begin_button.grid(column=0, row=4, sticky=(S))
        self.message.grid(column=0, row=0)

        self.banner_label.grid_configure(pady=1)
        self.display_frame.grid_configure(pady=1)
        self.display_checkbox.grid_configure(pady=0)
        self.begin_button.grid_configure(pady=5)
