import PySimpleGUI as sg

# A dictionary that defines the accepted conversion rates.
conversion_chart = {
    "Pounds to Kilograms": 0.4535924,
    "Feet to Meters": 0.305,
    "US Gallons to Liters": 3.785,
    "Miles to Kilometers": 1.609,
    "Square Feet to Square Meters": 0.093,
    "Yards to Meters": 0.914,
    "Acres to Hectares": 0.405,
}


def main():
    """A simple conversion app."""
    layout = [
        [
            sg.Input(key="-INPUT-"),
            sg.Combo([cc for cc in conversion_chart], key="-SPINBOX-"),
            sg.Button("Convert", key="-BUTTON-"),
        ],
        [sg.Text("...", enable_events=True, key="-OUTPUT-")],
    ]

    window = sg.Window("Converter App", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "-BUTTON-":
            s = values["-SPINBOX-"]
            i = values["-INPUT-"]
            if i.isnumeric() and i != None:
                window["-OUTPUT-"].update(convert(s, i))

    window.close()


def convert(s, i):
    """returns a float rounded to the nearest two decimal places."""
    return f"{(conversion_chart[s] * float(i)):.2f}"


if __name__ == "__main__":
    main()
