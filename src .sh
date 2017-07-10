#!/bin/bash



#update
apt-get update

#configure package
dpkg --configure -a


#install python
echo "python"
apt-get install python

#install openCV
echo "openCV"
apt-get install build-essential
apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

#install scilab
echo "scilab"
apt-get install scilab

#install sivp toolbox
echo "sivp"
scilab-cli  -e "atomsInstall('SIVP'); exit;" -nb

#to run sivp
echo "for sivp"
apt-get install libjpeg62
locate libtiff
cd /usr/lib/x86_64-linux-gnu/
ln -s libtiff.so.5 libtiff.so.4

#install pip
echo "pip"
apt-get install python-pip


#install numpy, scipy
echo "numpy,scipy"
pip install --user numpy scipy

#install scilab2py
echo "scilab2py"
pip install --user scilab2py


#install kivy
echo "update"
add-apt-repository ppa:kivy-team/kivy -y
apt-get install -y python-kivy


#change permissions for executable file
chmod a+x ./SIPLauncher.py


