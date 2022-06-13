import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def main():
    """"""
    table_content = []

    sg.theme("GrayGrayGray")

    layout = [
        [
            sg.Table(
                headings=["Observation", "Results"],
                values=table_content,
                expand_x=True,
                hide_vertical_scroll=True,
                key="-TABLE-",
            )
        ],
        [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Submit")],
        [sg.Canvas(key="-CANVAS-")],
    ]

    window = sg.Window("Graph App", layout, finalize=True)

    fig = matplotlib.figure.Figure(figsize=(5, 4))
    fig.add_subplot(111).plot([], [])
    figure_canvas_agg = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Submit":
            new_value = values["-INPUT-"]
            if new_value.isnumeric():
                table_content.append([len(table_content) + 1, float(new_value)])
                window["-TABLE-"].update(table_content)
                window["-INPUT-"].update("")
                update_fig(table_content, fig, figure_canvas_agg)

    window.close()


def update_fig(data, fig, figure_canvas_agg):
    """Update the graph"""
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x, y, "r-")

    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


if __name__ == "__main__":
    main()
