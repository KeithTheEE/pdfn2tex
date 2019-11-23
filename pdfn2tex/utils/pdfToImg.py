

import os
import time
import shutil
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
import logging

import kmlistfi

'''

https://stackoverflow.com/questions/11636982/how-to-figure-out-the-resolution-dpi-of-images-embedded-in-a-pdf-document

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



def make_image(pdf_path):
    # Uses Imagemagick, not recommended
    #convert_cmd = "convert -density 300 "+ pdf_path +" -depth 8 -strip -background white -alpha off temp/imgs.tiff"
    convert_cmd = "pdftoppm " + pdf_path + " temp/images/renderedimgs -png"
    resolution = " -r 300 "
    convert_cmd += resolution
    _runCLargs(convert_cmd)
    return sorted(kmlistfi.les('temp/images/'))

def clear_images(clean=True):
    imgs = kmlistfi.les('temp/images/')
    for img in imgs:
        print(img)
        if clean:
            os.remove(img)


def try_for_simple_text(pdf_path):
    '''
    If the pdf has embedded text, grab it. It won't necessarily 
    be treated as truth, but as a string-alignment attempt later on

    '''
    text_cmd = 'pdftotext ' + pdf_path + ' temp/embedded_text.txt'
    _runCLargs(text_cmd)