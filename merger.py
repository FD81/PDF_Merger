import os
from PyPDF2 import PdfReader, PdfMerger

# Set the directory path
dir_path = "G:\My Drive\PDF Merger Folder"

# Create a list of PDF files in the directory and sort them based on file name
pdf_files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.pdf') and f != 'output.pdf'], key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

# Create a PdfMerger object

# Create a PdfMerger object
merger = PdfMerger()

# Loop through the PDF files and append them to the merger object
for pdf in pdf_files:
    merger.append(PdfReader(pdf, 'rb'))

# Write the merged PDF to a file
output_path = os.path.join(dir_path, "output.pdf")
with open(output_path, 'wb') as output:
    merger.write(output)

print("PDF files merged successfully!")
