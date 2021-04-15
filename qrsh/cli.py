import sys
import time
import subprocess

import typer
import cv2
from PIL.ImageGrab import grab, grabclipboard

from qrsh import _decode

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
def scan_clipboard(capture: bool = typer.Option(False, '-c')):
    '''
    Capture QR code from your screen
    '''
    if capture:
        if sys.platform == 'darwin':
            subprocess.run(['screencapture', '-c', '-s'])
    _decode(grabclipboard(), pillow=True)

if __name__ == '__main__':
    app()
