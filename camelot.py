Here's the modified code that uses Camelot for table extraction:
Python
import camelot
import pandas as pd

def extract_text_and_tables(pdf_path):
    plain_text = ""
    tables = []

    # Extract plain text using PyPDF2
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            plain_text += page.extract_text()
    
    # Extract tables using Camelot
    tables = camelot.read_pdf(pdf_path, pages='all')

    return plain_text, tables

def save_to_excel(plain_text, tables, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Save plain text
        plain_text_df = pd.DataFrame([plain_text], columns=["Text"])
        plain_text_df.to_excel(writer, sheet_name="PlainText", index=False)

        # Save tables
        for i, table in enumerate(tables):
            table.df.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)

# Usage
pdf_path = "your_file.pdf"
output_path = "output.xlsx"
plain_text, tables = extract_text_and_tables(pdf_path)
save_to_excel(plain_text, tables, output_path)
In this modified code, we use Camelot's read_pdf function to extract tables from the PDF file. The pages='all' argument tells Camelot to extract tables from all pages in the PDF. The extracted tables are then saved to an Excel file using the save_to_excel function.
Note that Camelot returns a list of Table objects, each containing a df attribute that holds the table data as a Pandas DataFrame. We access this DataFrame using table.df when saving the tables to Excel.
