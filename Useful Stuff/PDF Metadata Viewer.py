from pymupdf import fitz

pdf_doc = input("Specify PDF file name: ")
doc = fitz.open(pdf_doc)

print("Page count", doc.pagecount)
print("Metadata", doc.metada)
