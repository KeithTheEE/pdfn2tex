



import os
import time
import shutil
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
import logging

import kmlistfi



'''
Focuses on extracted encoded information in a PDF 

Built of poppler-utils 
'''




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


def get_embedded_text(pdf_path):
    '''
    If the pdf has embedded text, grab it. It won't necessarily 
    be treated as truth, but as a string-alignment attempt later on

    '''
    text_cmd = 'pdftotext ' + pdf_path + ' temp/embedded/embedded_text.txt'
    _runCLargs(text_cmd)
    return

def get_embedded_images(pdf_path):
    # Render images as original format and as png for downstream tasks
    text_cmd = 'pdfimages -all ' + pdf_path + ' temp/embedded/images/'
    _runCLargs(text_cmd)
    text_cmd = 'pdfimages -png ' + pdf_path + ' temp/embedded/images/'
    _runCLargs(text_cmd)
    return

def get_embedded_svg_images(pdf_path):
    '''
    Ah I can dream...
    Without pre known bounds of the graph it isn't super easy

    '''
    pass

def clear_images(clean=True):
    imgs = kmlistfi.les('temp/embedded/images/')
    for img in imgs:
        print(img)
        if clean:
            os.remove(img)