#!/bin/env python3
"""pip install pymupdf
   pip install EbookLib
   pip install python-magic
   pip install textract
"""
import fitz  # PyMuPDF
from ebooklib import epub
import magic
import textract
def type(self):
    """ renvoie le type (EPUB, PDF, ou autre) du livre """
    mime = magic.Magic()
    type_fichier = mime.from_file(self.ressource)
    return type_fichie