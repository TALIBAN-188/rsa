#Aahil-coding

import os, time, platform

os.system("cd $HOME/")
try:
    import futures
except ImportError:
    os.system("pip2 install futures")
try:
    import lolcat
except ImportError:
    os.system("pip2 install lolcat")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("pip install requests")

rana=platform.architecture()[0]
if rana=="32bit":
    import minirsa
    minirsa.main_system()
elif rana=="64bit":
    import rsa64bit
    rsa64bit.main_system()
