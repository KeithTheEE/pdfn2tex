# pdfn2tex Version 0.0.00

A Skeleton Outline for a PDF->latex converter (in development)

This project makes assumptions in order to made development easier. While the assumptions do not hold for general pdf's, they should be moderate for pdf's made for research publications, dissertations, and theses, assuming the pdf's do not play with fancy formatting. 

This early version is going to play with Tesseract OCR v4 to aid the interpretation process. 

It is a portion of a larger 'Document to eReader' project. 


## Style Traits 
This project takes an approach to mapping pdf contents to tex. 

It assumes text flows top to bottom, and all sizable blocks of text can be mapped to a top-down order and position.

Images and tables are treated as additional info, to be displayed 'along side' the text, so their position is mutable. Diagrams and algorithm blocks are treated as a part of this class.

Equations and special charaters are treated as inline text, and their position is not mutable. 

## System Structure
Right now tesseract is simply going to be used to grab text and drop it into a flat file, likely a .txt, this way I can explore how to use it. Once I've got a handle on it, we can start the propper program.


First pass through the pdf should generate predicted document formating flags:

 - \documentclass
 - \usepackage
 - \newcommand (?)
 - pagenumbering (?)

 These are the packages needed to render the pdf 


## Error Measures
The generated Latex document is not intended to be a faithful reproduction of the source (assuming the training process goes Latex->PDF->Latex). The reader of the material (the important element in this project) should not care whether or not the text is formatted in one column or two columns, a word occurs on page 11 vs 12, or the exact position of an image. 

What does matter is that sections are grouped and nested correctly, internal document links are maintained (figure 1, reference 3, etc), and equations and tables are preserved.