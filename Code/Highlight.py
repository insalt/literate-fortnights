# your code goes here! /usr/bin/python
import docx
from docx import Document

with open("Broad_Terms.txt") as Broad_Dict:
    Broad_Dict = [y.strip() for y in Broad_Dict.readlines()]

document = Document('contract1.docx')

for paragraph in document.paragraphs:
    for run in paragraph.runs:
        for i in Broad_Dict:
            if i in run.text:
                text = run.text.split(i)
                run.text = text[0] + i.font.highlight_color = WD_COLOR_INDEX.BRIGHT_GREEN + text[1]




document.save('contract1_hl.docx')
