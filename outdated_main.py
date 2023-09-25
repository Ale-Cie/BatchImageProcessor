from PIL import Image
import os
import datetime
import sys

supported_formats = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".ico"]
input_files = list(item for item in os.listdir("./Input_Folder") if item != ".DS_Store")


def get_format():
    global supported_formats
    menu_layout = """[1] - .jpeg  [2] - .png  [3] - .bmp  [4] - .tiff  [5] - .ico
Choose an output file extension: """
    ext_flag = True
    while ext_flag:
        try:
            i = int(input(menu_layout))
            if i in range(1, len(supported_formats)):
                ext_flag = False
                ext = supported_formats[i]
                return ext
        except:
            print("Value error - please try again")


def convert(ext):
    conv_num = 1
    omitted = 0
    omitted_files = []
    for file in input_files:
        file_name = os.path.splitext(file)
        if file_name[1] in supported_formats and file_name[1] != ext and len(input_files) != 0:
            input_file = Image.open(f"./Input_Folder/{file}")
            if input_file.mode != "RGBA":
                input_file.save(f"./Output_Folder/{file_name[0]}{ext}", ext[1:])
            else:
                input_file = input_file.convert(mode="RGB")
                input_file.save(f"./Output_Folder/{file_name[0]}{ext}", ext[1:])
            print(f"Converted: {conv_num}/{len(input_files)}")
            conv_num += 1
        else:
            omitted += 1
            if file_name[1] not in supported_formats:
                reason = "File not yet supported"
            elif file_name[1] == ext:
                reason = f"File is already {ext}"
            omitted_files.append(f"{file, reason}")
            print(f"Omitted {omitted} files. Adding names to a list")

    print("Conversion complete\n--------------------------------")
    if omitted != 0:
        omitted_print = "\n".join(sorted(omitted_files))
        print(f"Omitted {omitted} files:\n{omitted_print}")
        print("Omitted files saved as a .txt file in output directory.")
        with open("./Output_Folder/omitted_files.txt", "w+") as my_log:
            header = f"Conversion to {ext} - {datetime.datetime.now()}.\nOmitted {omitted} files:\n"
            omitted_print = header + omitted_print
            my_log.writelines(omitted_print)


def main():
    global input_files
    while len(input_files) == 0:
        test = input("Input_Folder seems to be empty. Please put at least 1 file inside and type in OK: ")
        if test.lower() == "ok":
            input_files = list(item for item in os.listdir("./Input_Folder") if item != ".DS_Store")
    convert(get_format())
    return "Shutting down"


if __name__ == "__main__":
    sys.exit(main())
