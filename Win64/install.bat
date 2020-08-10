@ECHO OFF
python --version
ECHO You only need to do this once
ECHO ****************************************************************
ECHO Please install python 3.8 (or higher)
PAUSE
python -m pip install --upgrade pip
pip install sockets
pip install numpy
pip install opencv-python
pip install os-sys
pip install Pillow

ECHO ****************************************************************
ECHO Run the Holographic Remoting on your HoloLens 2 to get your HoloLens IP Address
ECHO Replace the value of host in the detectSocket.py with your HoloLens IP Address
PAUSE