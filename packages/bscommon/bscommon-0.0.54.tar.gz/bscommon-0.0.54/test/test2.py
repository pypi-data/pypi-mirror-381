import os
import sys
scriptDir = os.path.dirname(__file__)+os.sep
rootDir=scriptDir+".."+os.sep
sys.path.append(rootDir)
from src.bscommon import Com
from src.bscommon import Ssh
from src.bscommon import SysTask
sys.path.remove(rootDir)


Com.cmd("echo 111; echo 222; echo 333; ls /; ls -l /;")