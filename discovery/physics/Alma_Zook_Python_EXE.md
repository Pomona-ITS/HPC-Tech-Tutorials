# This page is for documenting the process of making and independent Python executable that can run on Windows without having to install Python (requested by Alma Zook)

The source code is [here](https://github.com/Pomona-ITS/hpc/blob/master/discovery/physics/Phys3fft_NoPulldowns_CleanedUp.py).

The wav file is [here](https://github.com/Pomona-ITS/hpc/blob/master/discovery/physics/ClarF4_Edit.wav)

The final result (zipped folder with the executable and the source wav file) is [here](https://pomona.box.com/s/m9d894gcyd88xw3183vdsxm61yd45nw5).

Used:

1) VirtualBox on Mac
2) Windows 10 VM
3) Anaconda
4) Python 2.7 environment
5) Additional modules numpy and matplotlib
6) PyInstaller for generating the exe
7) Added qt.conf to dist folder to fix the Qt path error
8) Added wav file to dist folder
9) Zipped dist folder and saved to Box

Alma asked for the same process on Mac:

1) Anaconda
2) Virtual environment with Python 3.6 (there is a problem with 2.7 on Macs)
3) numpy was already installed automatically with 3.6, added matplotlib
4) pip install pyinstaller
5) upgraded pip (because why not)
6) Added wav file to dist
7) zipped and uploaded to Box
