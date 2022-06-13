import PySimpleGUI as sg
from pathlib import Path


def main():
    """A simple text editor app."""
    emotes = [
        "happy",
        [":)", ":D", ";)"],
        "sad",
        [":(", "D:", ";("],
        "other",
        [":^)", "B)", ";_;"],
    ]

    emote_events = emotes[1] + emotes[3] + emotes[5]

    sg.theme("GrayGrayGray")

    menu_layout = [
        ["File", ["Open", "Save", "---", "Exit"]],
        ["Tools", ["Word Count"]],
        ["Add", emotes],
    ]

    layout = [
        [sg.Menu(menu_layout)],
        [sg.Text("Untitled", key="-DOCNAME-")],
        [sg.Multiline(no_scrollbar=True, size=(40, 30), key="-TEXTAREA-")],
    ]

    window = sg.Window("Text Editor App", layout)

    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, "Exit"]:
            break

        if event == "Open":
            file_path = sg.popup_get_file("open", no_window=True)
            if file_path:
                file = Path(file_path)
                window["-TEXTAREA-"].update(file.read_text())
                window["-DOCNAME-"].update(file_path.split("/")[-1])

        if event == "Save":
            file_path = (
                sg.popup_get_file("Save As", no_window=True, save_as=True) + ".txt"
            )
            file = Path(file_path)
            file.write_text(values["-TEXTAREA-"])
            window["-DOCNAME-"].update(file_path.split("/")[-1])

        if event == "Word Count":
            full_text = values["-TEXTAREA-"]
            word_count = len(full_text.split(" "))
            sg.popup(f"Word Count: {word_count}")

        if event in emote_events:
            current_text = values["-TEXTAREA-"]
            new_text = f"{current_text} {event}"
            window["-TEXTAREA-"].update(new_text)

    window.close()


if __name__ == "__main__":
    main()
