import PySimpleGUI as sg
import cv2


def main():
    """"""
    layout = [
        [sg.Image(key="-IMAGE-")],
        [sg.Text("People in frame: 0", key="-TEXT-", expand_x=True, justification="c")],
    ]

    window = sg.Window("Face Detection App", layout)

    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break

        _, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7, minSize=(50, 50))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x + w, y + h), (255,255,255), 2)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

        window['-TEXT-'].update(f'People in frame: {len(faces)}')

    window.close()


if __name__ == "__main__":
    main()
