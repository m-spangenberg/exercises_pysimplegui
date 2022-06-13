import PySimpleGUI as sg


def main(theme="LightGrey6"):
    """A simple calculator app."""
    sg.theme(theme)

    sg.set_options(
        font="Franklin 12",
    )

    theme_menu = [
        "menu",
        ["LightGrey6", "DarkBlack", "DarkTeal2", "DarkBlue14"],
    ]

    layout = [
        [
            sg.Text(
                "",
                font=("Franklin 26"),
                expand_x=True,
                justification="right",
                pad=(10, 20),
                right_click_menu=theme_menu,
                key="-OUTPUT-",
            )
        ],
        [
            sg.Button("AC", size=(4, 3), key="-BUTTONAC-"),
            sg.Button("+/-", size=(4, 3), key="-BUTTONP2N-", disabled=True),
            sg.Button("%", size=(4, 3), key="-BUTTONPER-", disabled=True),
            sg.Button("/", size=(4, 3)),
        ],
        [
            sg.Button(7, size=(4, 3)),
            sg.Button(8, size=(4, 3)),
            sg.Button(9, size=(4, 3)),
            sg.Button("*", size=(4, 3)),
        ],
        [
            sg.Button(4, size=(4, 3)),
            sg.Button(5, size=(4, 3)),
            sg.Button(6, size=(4, 3)),
            sg.Button("-", size=(4, 3)),
        ],
        [
            sg.Button(1, size=(4, 3)),
            sg.Button(2, size=(4, 3)),
            sg.Button(3, size=(4, 3)),
            sg.Button("+", size=(4, 3)),
        ],
        [
            sg.Button(0, size=(4, 3)),
            sg.Button(".", size=(4, 3)),
            sg.Button("MOD", size=(4, 3), key="-BUTTONMOD-", disabled=True),
            sg.Button("=", size=(4, 3), key="-BUTTONEQU-"),
        ],
    ]

    window = sg.Window("Calculator", layout)

    current_value = []
    current_operation = []

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event in theme_menu[1]:
            window.close()
            window = main(event)

        # parse every number pressed into a string.
        if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            current_value.append(event)
            value_string = "".join(current_value)
            window["-OUTPUT-"].update(value_string)

        if event in ["+", "-", "/", "*"]:
            current_operation.append("".join(current_value))
            current_value = []
            current_operation.append(event)
            window["-OUTPUT-"].update("")

        if event == "-BUTTONEQU-":
            try:
                current_operation.append("".join(current_value))
                result = eval(" ".join(current_operation))
                current_value.clear()
                window["-OUTPUT-"].update(result)
            except SyntaxError:
                pass

        # Perform AC: Clear current value and current operations from memory.
        if event == "-BUTTONAC-":
            window["-OUTPUT-"].update("CLEARED")
            current_value.clear()
            current_operation.clear()

    window.close()


if __name__ == "__main__":
    main()
