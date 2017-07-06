# sip-lab
For Debian Linux like Ubuntu,Mint<br/>
1.Download the folder <br/>
2.Run test.py in Python2 <br/>
3.Go to exp <br/>
4.Input Image file <br/> 
5.Enter Inputs and click submit<br/>

Requirements: <br/>
1.Scilab<br/>


2.SIVP toolbox <br/>

3.Python2.7<br/>

4.kivy<br/>
sudo add-apt-repository ppa:kivy-team/kivy<br/>
sudo apt-get install python-kivy<br/>

5. scipy<br/>
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose<br/>
or (incase above didn't work)<br/>
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose<br/>

6.scilab2py</br>
pip install scilab2py<br/>


For Windows<br/>
scilab
SIVP Toolbox
Python 2.7.any
kivy
if you get any depnedency error like widow thing then run this command 
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

You can install scipy and numpy using their wheels.

First install wheel package if it's already not there...

pip install wheel
Just select the package you want from http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy

Then go to the command line and change the directory to the downloads folder and install the above wheel using pip.

Example:
cd C:\Users\[user]\Downloads
pip install numpy-1.11.3+mkl-cp27-cp27m-win_amd64.whl
pip install scipy-0.18.1-cp35-cp35m-win_amd64.whl

if you get any error like NUMPY_MKL
then uninstall numpy which installed using normal 'pip install numpy'
Becasue scipy whl package need numpy whl package not normal numpy package.


scilab2py
pip install scilab2py
 if you geting any error like
 Scilab not found.  Please see documentation at:
http://blink1073.github.io/scilab2py/source/installation.html
then uninstall wheel using pip uninstall wheel
then install scilab2py using pip install scilab2py


Now we are ready to go




Links:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
https://stackoverflow.com/questions/26657334/installing-numpy-and-scipy-on-64-bit-windows-with-pip

