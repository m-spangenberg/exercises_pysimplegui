import PySimpleGUI as sg
from time import time


def main():
    """A simple stopwatch with styling."""

    window = create_window()

    start_time = 0
    active = False
    lap_count = 1

    while True:
        event, values = window.read(timeout=10)
        if event in [sg.WIN_CLOSED, "-CLOSE-"]:
            break

        if event == "-STARTSTOP-":
            if active:
                active = False
                window["-STARTSTOP-"].update("Reset")
                window["-LAP-"].update(visible=False)
            elif start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
            else:
                start_time = time()
                active = True
                window["-STARTSTOP-"].update("Stop")
                window["-LAP-"].update(visible=True)

        if active:
            elapsed_time = round(time() - start_time, 1)
            window["-TIMER-"].update(elapsed_time)

        if event == "-LAP-":
            window.extend_layout(
                window["-LAPS-"],
                [[sg.Text(lap_count), sg.VSeparator(), sg.Text(elapsed_time)]],
            )
            lap_count += 1

    window.close()


def create_window():
    """"""
    sg.theme("GrayGrayGray")

    layout = [
        [
            sg.Push(),
            sg.Image(
                "cross.png", pad=0, size=(16, 16), enable_events=True, key="-CLOSE-"
            ),
        ],
        [sg.VPush()],
        [sg.Text("Time", font="Calibri 50", key="-TIMER-")],
        [
            sg.Button(
                "Start",
                button_color=("#FFFFFF", "#FF0000"),
                border_width=0,
                key="-STARTSTOP-",
            ),
            sg.Button(
                "Lap",
                button_color=("#FFFFFF", "#FF0000"),
                border_width=0,
                key="-LAP-",
                visible=False,
            ),
        ],
        [sg.Column([[]], key="-LAPS-")],
        [sg.VPush()],
    ]

    return sg.Window(
        "Stopwatch App",
        layout,
        size=(300, 300),
        no_titlebar=False,
        element_justification="center",
    )


if __name__ == "__main__":
    main()
