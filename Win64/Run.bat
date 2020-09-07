@ECHO OFF
ECHO ****************************************************************
ECHO Run the Holographic Remoting APP on your HoloLens 2 to get your HoloLens IP Address
ECHO Make sure the value of "host" in the ../pythonCode/faceDetection.py matches your HoloLens IP Address
rem PAUSE
ECHO ****************************************************************
ECHO Start running the App on your HoloLens Device.  
python ../pythonCode/Client.py
ECHO DONE!
PAUSE