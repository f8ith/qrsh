from setuptools import setup, find_packages

setup(
    name='scanqr',
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
        'console_scripts': ['scanqr=scanqr.video:main',
                            'captureqr=scanqr.clipboard:main'],
    }
)
