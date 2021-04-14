import typer

import cv2
from PIL.ImageGrab import grab, grabclipboard
import sys
import time

from scanqr import _decode

app = typer.Typer()

@app.command('camera')
def scan_camera():
    '''
    Capture QR code from your camera
    '''

    print('[INFO] Camera starting up...')

    cap = cv2.VideoCapture(0)
    time.sleep(2)
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                _decode(frame)
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()

@app.command('screen')
def scan_screen():
    '''
    Get QR code from screen
    '''
    _decode(grab(), pillow=True)

@app.command('clipboard')
def scan_clipboard():
    '''
    Capture QR code from your screen
    '''
    _decode(grabclipboard(), pillow=True)

if __name__ == '__main__':
    app()
