

'''
Find packages

sudo apt-cache search tesseract-ocr

Select Languages
https://manpages.ubuntu.com/manpages/eoan/en/man1/tesseract.1.html

'''

import os
import time
import shutil
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
import logging



def _runCLargs(cmd,showCMD=True):
    '''
    executes command passed in. Vulnerable to attacks

    '''
    print(cmd)
    p = Popen(cmd , stdout = PIPE, stderr = STDOUT, shell = True)
    s = ''
    for line in p.stdout:
        #logging.info(line)
        print(line.decode("utf-8").rstrip())
        s+= line.decode("utf-8")
    
    return s


def run_basic(source_image):

    img_name, img_ext =os.path.splitext(os.path.basename(source_image))
    tes_cmd = "tesseract "+source_image+" temp/tesseractOutput/"+img_name+" -l eng"
    _runCLargs(tes_cmd)

    return