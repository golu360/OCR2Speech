from PIL import Image, ImageEnhance,ImageFilter
import pytesseract
import os
from gtts import gTTS
import argparse as ap
import PyPDF2 as pdf
import sys



def set_image_dpi(file_name):
	im = Image.open(file_name)
	length_x,length_y = im.size
	factor = min(1,float(1024.0/length_x))
	size = int(factor*length_x),int(factor*length_y)
	im_resized = im.resize(size,Image.ANTIALIAS)
	temp_file = tempFile.NamedTemporaryFile(delete = False,suffix = '.jpg')
	tempfile_name = temp_file.name
	im_resized.save(tempfile_name,dpi = (300,300))
	return tempfile_name



parser = ap.ArgumentParser()
parser.add_argument("-image","--Image",help = "Path to image",required = False)
parser.add_argument("-pdf","--PDF",help = "Path to PDF File",required = False)
args = vars(parser.parse_args())

print("Output Audio file name:")
name = str(input())





if args["Image"] is not None:

	  
	im = Image.open(args["Image"])

	txt = pytesseract.image_to_string(im)
	


	obj = gTTS(text =txt,lang = 'en-uk',slow = False)
	obj.save( name+ ".mp3")



if args["PDF"] is not None:
	pdfObj = open(args["PDF"],"rb")
	pdfReader = pdf.PdfFileReader(pdfObj)
	for i in range(0,pdfReader.numPages):
		pageObj = pdfReader.getPage(i)
		txt = pageObj.extractText()
		out = gTTS(text = txt,lang = 'en-uk',slow = False)
		out.save(name + str(i) +".mp3")

if args["Image"] and args["PDF"] is None:
	print("No args")
	sys.exit()           


sys.exit()


