from curses import KEY_BTAB
import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO


def main():
    """"""
    image_path = sg.popup_get_file("Open", no_window=True)

    sg.theme("DarkTeal7")

    control_col = sg.Column(
        [
            [sg.Checkbox("Emboss", key="-EMBOSS-")],
            [sg.Checkbox("Contour", key="-CONTOUR-")],
            [sg.Checkbox("Flip X", key="-FLIPX-")],
            [sg.Checkbox("Flip Y", key="-FLIPY-")],
            [
                sg.Frame(
                    "Contrast",
                    layout=[
                        [
                            sg.Slider(
                                range=(0, 10),
                                orientation="horizontal",
                                key="-CONTRAST-",
                            )
                        ]
                    ],
                )
            ],
            [
                sg.Frame(
                    "Blur",
                    layout=[
                        [
                            sg.Slider(
                                range=(0, 10), orientation="horizontal", key="-BLUR-"
                            )
                        ]
                    ],
                )
            ],
            [sg.Button("Save Image", key="-SAVE-")],
        ]
    )

    image_col = sg.Column([[sg.Image("test.png", key="-IMAGE-")]])

    layout = [
        [control_col, image_col],
    ]

    original = Image.open(image_path)
    window = sg.Window("Image Editor App", layout)

    while True:
        event, values = window.read(timeout=50)
        if event == sg.WIN_CLOSED:
            break

        if event == "-SAVE-":
            save_path = sg.popup_get_file("Save", save_as=True, no_window=True) + ".png"
            image.save(save_path, "PNG")

        update_image(
            window,
            original,
            values["-EMBOSS-"],
            values["-CONTOUR-"],
            values["-FLIPX-"],
            values["-FLIPY-"],
            values["-CONTRAST-"],
            values["-BLUR-"],
        )

    window.close()


def update_image(window, original, emboss, contour, flipx, flipy, contrast, blur):
    """Modify and update the imported image"""
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())

    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format="PNG")

    window["-IMAGE-"].update(data=bio.getvalue())


if __name__ == "__main__":
    main()
