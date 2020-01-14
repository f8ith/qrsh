from setuptools import setup, find_packages

setup(
    name='qrcode',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'pyzbar',
        'imutils'
    ],
    entry_points={
        'console_scripts': ['qrcode=qrcode.qrcode:main'],
    }
)
