import subprocess
from math import ceil

from tkinter import *
from tkinter import ttk, filedialog
from pyautogui import size

class ExtensionsFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.extension = StringVar()
        self.extension.set("None")

        label_text = "If you need a uniform extension for a collection of images, pick\none of the file formats below and press 'Schedule Tasks'.\nWhen you later on click 'Process Images' to apply changes."
        self.banner = PhotoImage(file= "./resources/images/extension_manager.png")
        self.clear = PhotoImage(file= "./resources/images/clear_button.png").subsample(2, 2)
        self.banner_frame = ttk.Frame(self)
        self.image_label = ttk.Label(self.banner_frame, image=self.banner)
        self.description_frame = ttk.Label(self, text= label_text, justify="center")
        self.basic_checkboxes_frame = ttk.Frame(self)
        self.other_checkboxes_frame = ttk.Frame(self)
        self.schedule_img = PhotoImage(file="./resources/images/schedule_task.png").subsample(2, 2)
        self.schedule_button = Button(self, image= self.schedule_img, text="")
        self.clear_button = Button(self, image= self.clear, command=lambda: self.extension.set("None"))

        self.basic_checkboxes_creator()
        self.other_checkboxes_creator()
        self.frame_setup()
        
        self.columnconfigure(0, weight= 3)
        self.columnconfigure(1, weight= 3)

        for child in self.winfo_children():
            child.grid_configure(padx= 5, pady= 5)

    def basic_checkboxes_creator(self):
        basic_formats = ttk.Label(self.basic_checkboxes_frame, text="Available file formats:", font="TkSmallCaptionFont")
        jpg_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "JPEG", variable= self.extension, value= ".jpeg")
        png_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "PNG", variable= self.extension, value= ".png")
        bmp_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "BMP", variable= self.extension, value= ".bmp")
        tiff_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "TIFF", variable= self.extension, value= ".tiff")
        gif_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "GIF", variable= self.extension, value=".gif")
        ico_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "ICO", variable= self.extension, value= ".ico")
        icns_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "ICNS", variable= self.extension, value= ".icns")
        webp_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "WEBP", variable= self.extension, value= ".webp")
        pdf_box = ttk.Radiobutton(self.basic_checkboxes_frame, text= "PDF", variable= self.extension, value=".pdf")

        basic_boxes = [jpg_box, png_box, bmp_box, tiff_box, gif_box, ico_box, icns_box, webp_box, pdf_box]
        basic_formats.grid(column= 0, row= 0, columnspan= 3)

        column_length = ceil(len(basic_boxes) / 3)
        column_idx, row_idx = 0, 1 

        for box in basic_boxes:
            try:
                if row_idx != column_length:
                    box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                    row_idx += 1
                else:
                    box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                    row_idx = 1
                    column_idx += 1
            except:
                pass

    def other_checkboxes_creator(self):
        other_formats = ttk.Label(self.other_checkboxes_frame, text= "Other file formats:", font= "TkSmallCaptionFont")
        blp_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "BLP", variable= self.extension, value= ".blp")
        dds_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "DDS", variable= self.extension, value= ".dds")
        dib_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "DIP", variable= self.extension, value= ".dib")
        im_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "IM", variable= self.extension, value= ".im")
        ppm_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "PPM", variable= self.extension, value= ".ppm")
        sgi_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "SGI", variable= self.extension, value= ".sgi")
        spider_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "SPIDER", variable= self.extension, value= ".spider")
        tga_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "TGA", variable= self.extension, value= ".tga")
        xbm_box = ttk.Radiobutton(self.other_checkboxes_frame, text= "XBM", variable= self.extension, value= ".xbm")

        other_boxes = [blp_box, dds_box, dib_box, im_box, ppm_box, sgi_box, tga_box, xbm_box, spider_box]
        other_formats.grid(column= 0, row= 0, columnspan= 3)

        column_length = ceil(len(other_boxes) / 3)
        column_idx, row_idx = 0, 1 

        for box in other_boxes:
            try:
                if row_idx != column_length:
                    box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                    row_idx += 1
                else:
                    box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                    row_idx = 1
                    column_idx += 1
            except:
                pass

    def frame_setup(self):
        self.banner_frame.grid(column= 0, row= 0, columnspan= 2)
        self.image_label.grid(column= 0, row= 0)
        self.description_frame.grid(column= 0, row= 1, sticky= (N,S,E,W), columnspan= 2)
        self.basic_checkboxes_frame.grid(column= 0, row= 2, sticky= (N,S,E,W))
        self.other_checkboxes_frame.grid(column= 1, row= 2, sticky= (N,S,E,W))
        self.schedule_button.grid(column= 1, row= 3)
        self.clear_button.grid(column= 0, row= 3)

        self.columnconfigure(0, weight= 3)
        self.columnconfigure(1, weight= 3)
        self.rowconfigure(0, weight=3)

        for child in self.basic_checkboxes_frame.winfo_children():
            child.grid_configure(padx= 5, pady= 5)
        for child in self.other_checkboxes_frame.winfo_children():
            child.grid_configure(padx= 5, pady= 5)
        self.banner_frame.grid_configure(padx=0)

class FiltersFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.filter = StringVar()
        label_text = "This is work in progres.\nCome back later.\nEnjoy the rest of the view"
        self.banner = PhotoImage(file= "./resources/images/filters_manager.png")
        self.preview = PhotoImage(file= "./resources/images/preview.png").subsample(3, 3)
        self.schedule = PhotoImage(file= "./resources/images/schedule_task.png").subsample(2, 2)
        self.clear = PhotoImage(file= "./resources/images/clear_button.png").subsample(2, 2)
        self.banner_frame = ttk.Frame(self)
        self.image_label = ttk.Label(self.banner_frame, image=self.banner)
        self.description_label = ttk.Label(self, text= label_text)
        self.checkboxes_frame = ttk.Frame(self)
        self.preview_frame = ttk.Frame(self)
        self.preview_label = ttk.Label(self.preview_frame, image=self.preview)
        self.schedule_button = Button(self, image= self.schedule)
        self.clear_button = Button(self, image= self.clear, command=lambda: self.filter.set("None"))

        self.checkboxes_creator()
        self.frame_setup()

        self.columnconfigure(0, weight= 3)
        self.columnconfigure(1, weight= 3)

        for child in self.winfo_children():
            child.grid_configure(padx= 5, pady= 5)

    def checkboxes_creator(self):
        header_label = ttk.Label(self.checkboxes_frame, text= "Available filters:", font= "TkSmallCaptionFont")
        blur_box = ttk.Radiobutton(self.checkboxes_frame, text= "BLUR", variable= self.filter, value= "BLUR")
        contour_box = ttk.Radiobutton(self.checkboxes_frame, text= "CONTOUR", variable= self.filter, value= "CONTOUR")
        detail_box = ttk.Radiobutton(self.checkboxes_frame, text= "DETAIL", variable= self.filter, value= "DETAIL")
        enhance_box = ttk.Radiobutton(self.checkboxes_frame, text= "EDGE ENHANCE", variable= self.filter, value="EDGE_ENHANCE")
        enhance_more_box = ttk.Radiobutton(self.checkboxes_frame, text= "EDGE ENHANCE MORE", variable= self.filter, value="EDGE_ENHANCE_MORE")
        emboss_box = ttk.Radiobutton(self.checkboxes_frame, text= "EMBOSS", variable= self.filter, value= "EMBOSS")
        find_edges_box = ttk.Radiobutton(self.checkboxes_frame, text= "FIND EDGES", variable= self.filter, value= "FIND_EDGES")
        sharpen_box = ttk.Radiobutton(self.checkboxes_frame, text= "SHARPEN", variable= self.filter, value= "SHARPEN")
        smooth_box = ttk.Radiobutton(self.checkboxes_frame, text= "SMOOTH", variable= self.filter, value= "SMOOTH")
        smooth_more_box = ttk.Radiobutton(self.checkboxes_frame, text= "SMOOTH MORE", variable= self.filter, value= "SMOOTH_MORE")

        boxes = [blur_box, contour_box, detail_box, enhance_box, emboss_box, find_edges_box, sharpen_box, smooth_box]
        column_idx, row_idx = 0, 1

        header_label.grid(column= 0, row= 0, columnspan= 2)
        for box in boxes:
            if row_idx != 4:
                box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                row_idx +=1
            else:
                box.grid(column= column_idx, row= row_idx, sticky= (N,S,E,W))
                row_idx = 1
                column_idx = 1
        
        enhance_more_box.grid(column= 0, row= 5, columnspan= 2, sticky= (N,S,E,W))
        smooth_more_box.grid(column=0, row= 6, columnspan= 2, sticky= (N,S,E,W))

    def frame_setup(self):
        self.banner_frame.grid(column=0, row=0, columnspan= 2)
        self.image_label.grid(column= 0, row= 0)
        self.description_label.grid(column=0, row= 1, columnspan= 2, sticky= (N,S,E,W))
        self.checkboxes_frame.grid(column=0, row=2)
        self.preview_frame.grid(column=1, row=2)
        self.preview_label.grid(column= 0, row= 0)
        self.schedule_button.grid(column=1, row= 3, rowspan= 2)
        self.clear_button.grid(column=0, row= 3)

       