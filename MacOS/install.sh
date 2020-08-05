
echo You only need to do this once
echo ****************************************************************
echo Your python version is:
python --version
echo If you do not have python installed, Please use python-3.8.5-macosx10.9.pkg to install it.
read -p "Make sure python is installed and then press any key to continue ..."
xcode-select --install
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew update
brew tap brewsci/bio
sudo easy_install pip
sudo pip install --upgrade pip
pip install sockets
pip install numpy
pip install opencv-python
pip install os-sys
sudo pip install pillow
pip3 install pillow

ECHO ****************************************************************
ECHO Run the Holographic Remoting on your HoloLens 2 to get your HoloLens IP Address
ECHO Replace the value of host in the detectSocket.py with your HoloLens IP Address
PAUSE

echo ****************************************************************
echo If Please install python using python-3.8.5-macosx10.9.pkg
read -p "Press any key to continue ..."