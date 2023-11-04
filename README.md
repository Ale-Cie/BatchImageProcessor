# BIP - BatchImageProcessor

<p align="center">
    <img src="./resources/images/bip_banner.png" />
</p>

BatchImageProcessor (or BIP for short) is a simple, Pillow based app that takes a batch of images from a specified directory and applies scheduled changes to them. I'll go into detail below.

If you'd like to you can follow the project on my portfolio website, you just have to click <a href="https://aleksanderc.pythonanywhere.com/wip.html">this link</a>.

## Requirements

- Currently supported operating systems:
  - 🍎 MacOS - ✅
  - 🪟 Windows - ⛔️ - I haven't tested it. Might work, might not, I'll check later after I'm done with the backend
  - 🐧 Linux - ❓ - It could work...?

## Background

At long last I upload a project that sort of started my interest in programmig. Why do I write that? Well it was the first bit of code that actuall showed me, that learning Python won't just boil down to writing silly exercises and that I can actually solve some real-life problems.

Answering the question from the introduction - what scheduled changes? For now you can quickly change extensions, resize the images and apply filters. Why may you need it? Well if you've read so far either a use came to your mind by now. Myself, I found it usefull while preparing images for a neural network I wanted to test. This app made it quite easy to resize the images, apply filters to mix up the data etc.

Currently (v. 0.2.0), the app is fully functional, but I have not made any efforts to optimize it in any way. You can now resize, apply filters, change extensions all with the help of an (more or less) intuitive GUI. Some changes are bound to the app happen in future iterations, but for now this is BIP.

## What's already happened?

<i>-- 03.11.2023 --</i>

A rather big update this time! Say hello to BatchImageProcessor v. 0.2.0 - not just a GUI anymore, it comes with functionality now! From this update Mac users can feed batches of images to BIP, change their extensions en masse, resize them to either a freeform size or a selected width:height ratio and apply one of ten different filters. A `config.ini` file gets created upon booting up the app, which for now serves as just a way to either display or not a welcome screen at startup of the app. Feel free to play around with the app, it should work as intended!

<i>-- 05.10.2023 --</i>

A tiny little update to version 0.1.1 in which I added a third (but second in order) tab to the main screen. It will allow the user to handle resizing files either freely or by using set width to height ratio. Other than that no changes in functionality. Some new images were added to the resources. They will probably be used in the future, however I will see about that and might change them at some point.

<i>-- 25.09.2023 --</i>

The repository was created, uncomplete 0.1.0 version of the frontend was uploaded, `README.md` was created and updated. From this point onward any changes will get directly commited to this repository and then descirbed here and on my portfolio page.
