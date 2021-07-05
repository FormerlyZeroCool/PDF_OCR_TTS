from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
pdf = "Renner.pdf"
outfile = "output.txt"
if len(sys.argv) > 1:
    pdf = sys.argv[1]
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
print("Converting pdf to jpeg for ocr.")
pages = convert_from_path(pdf, 500)
print("pdf conversion complete.")
im_counter = 0


f = open(outfile, "a")
for page in pages:
    print(round(im_counter/len(pages)*100),"% complete with ocr",im_counter,"pages read.")
    text = str(((pytesseract.image_to_string(page))))
    f.write(text)
    im_counter += 1

        