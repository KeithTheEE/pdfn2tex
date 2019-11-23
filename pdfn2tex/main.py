

import argparse, textwrap
import logging
import os

from utils import extractEmbeddedValues
from utils import pdfToImg
from utils import tesseractProcessor




def interface():
    args = argparse.ArgumentParser(
        prog='pdfn2tex', 
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A program to convert pdfs to latex files',
        epilog=textwrap.dedent('''\
            PDFn2Tex assumes that the pdf was sourced from a simple latex
            file, and that latex file did not push the boundaries when it
            comes to formatting. 
        '''))
    args.add_argument('-i', '--input-file', type=str, default='infile.pdf',\
                      help='The input file path for the pdf to be converted')
    args.add_argument('-o', '--output-file', type=str, default='outfile.tex',\
                      help='The output file name path for the resulting latex documents')
    args.add_argument('-t', '--run-tests', action='store_true', \
                      help="Rather than convert a file, run through test suit. Will override input/output files if given")
    args = args.parse_args()
    return args


def verify_input_args(args):

    ifl = ""
    ofl = ""
    return ifl, ofl


def cleanup():
    extractEmbeddedValues.clear_images()
    pdfToImg.clear_images()

def pipeline_on_pdf(pdf):
    # Get low hanging fruit for later
    extractEmbeddedValues.get_embedded_text(pdf)
    extractEmbeddedValues.get_embedded_images(pdf)

    # Convert pdf to images for OCR
    images = pdfToImg.make_image(pdf)

    # Bound images for OCR


    # Run Tesseract
    for image in images:
        tesseractProcessor.run_basic(image)

    # Remove temp files
    #cleanup()

def run_starting_test():
    simple_pdf='tests/SimpleAndPlain.pdf'
    pipeline_on_pdf(simple_pdf)
    complex_pdf='tests/complex_example.pdf'
    pipeline_on_pdf(complex_pdf)
    pass
    


if __name__ == "__main__":
    args = interface()
    if args.run_tests:
        print("HEllo")
        run_starting_test()
    else:
        ifl, ofl = verify_input_args(args)
    pass