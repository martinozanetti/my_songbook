import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_subfolders(root_dir, output_file):
    merger = PdfMerger()
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(foldername, filename)
                merger.append(pdf_path)

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    root_dir = os.getcwd()  # Ottiene la directory corrente
    output_file = os.path.join(root_dir, 'merged_pdf.pdf')
    merge_pdfs_in_subfolders(root_dir, output_file)
    print("PDF files merged successfully into", output_file)
