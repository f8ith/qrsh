from imutils.video import VideoStream
from pyzbar.pyzbar import decode
import sys
import webbrowser

print('[INFO] Camera starting up...')


def main():
    vs = VideoStream(src=0).start()
    try:
        while True:
            frame = vs.read()
            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                if barcode_data is not None:
                    print(barcode_data)
                    if not barcode_data.startswith('http://') \
                            and not barcode_data.startswith('https://'):
                        webbrowser.open('http://' + barcode_data)
                    sys.exit()
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sys.exit()
