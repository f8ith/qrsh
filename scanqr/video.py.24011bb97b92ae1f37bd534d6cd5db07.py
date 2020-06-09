from imutils.video import VideoStream
import sys

from scanqr import _decode

print('[INFO] Camera starting up...')


def main():
    vs = VideoStream(src=0).start()
    try:
        while True:
            _decode(vs.read())
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sys.exit()
