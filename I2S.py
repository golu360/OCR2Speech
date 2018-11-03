from PIL import Image
import pytesseract
import os
from gtts import gTTS
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument("-image","--Image",help = "Path to image",required = True)
args = vars(parser.parse_args())

print("Output Audio file name:")
name = str(input())



im = Image.open(args["Image"])
text = pytesseract.image_to_string(im)
#print(text)

obj = gTTS(text =text,lang = 'en-uk',slow = False)
obj.save( name+ ".mp3")
sys.exit()
