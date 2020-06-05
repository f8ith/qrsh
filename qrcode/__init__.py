from pyzbar.pyzbar import decode
import sys
import webbrowser


def _decode(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        if barcode_data is not None:
            print(barcode_data)
            if not barcode_data.startswith('http://') \
                    and not barcode_data.startswith('https://'):
                webbrowser.open('http://' + barcode_data)
            sys.exit()
