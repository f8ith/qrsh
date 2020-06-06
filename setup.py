from setuptools import setup, find_packages

setup(
    name='qrcode',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyzbar',
        'imutils',
        'pillow',
        'pynput',
        'pyscreenshot',
        'mss'
    ],
    entry_points={
        'console_scripts': ['scanqr=qrcode.video:main',
                            'captureqr=qrcode.clipboard:main'],
    }
)
