import sys
import pyscreenshot as ImageGrab
from pynput import mouse

from scanqr import _decode

bbox = []


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        global bbox
        bbox.append(x)
        bbox.append(y)
        if not pressed:
            return False


def main():
    try:
        with mouse.Listener(on_click=on_click, suppress=True) as listener:
            listener.join()
        global bbox
        print(bbox)
        _decode(ImageGrab.grab(backend="mss",
                               childprocess=False, bbox=(tuple(bbox))))
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sys.exit()
