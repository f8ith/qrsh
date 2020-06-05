import platform
import sys

from qrcode import _decode

# chose an implementation, depending on os
if platform.system() == 'Windows':  # sys.platform == 'win32':
    from PIL.ImageGrab import grabclipboard as gc
elif platform.system() == 'Linux':
    from pyscreenshot.ImageGrab import grabclipboard as gc
elif platform.system() == 'Darwin':
    from PIL.ImageGrab import grabclipboard as gc
else:
    raise ImportError(
        "Sorry: no implementation for your platform ('{}') available".format(
            platform.system
        )
    )


def main():
    try:
        _decode(gc())
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sys.exit()
