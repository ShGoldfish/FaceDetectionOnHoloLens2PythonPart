@ECHO OFF
ECHO ****************************************************************
ECHO ****************************************************************
ECHO Run the Holographic Remoting APP on your HoloLens 2 to get your HoloLens IP Address
ECHO Make sure the value of "host" in the faceDetection.py with your HoloLens IP Address
PAUSE
ECHO Start running the App on your HoloLens Device. once it is running press any key to start Face Detection: 
PAUSE
python faceDetection.py
ECHO DONE!
PAUSE