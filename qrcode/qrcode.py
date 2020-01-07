from imutils.video import VideoStream
from pyzbar.pyzbar import decode
import time
import sys

print('[INFO] Camera starting up...')
vs = VideoStream(src=0).start()
time.sleep(1.0)

try:
    while True:
        frame = vs.read()
        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data
            if barcode_data is not None:
                print(barcode_data)
                break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sys.exit()