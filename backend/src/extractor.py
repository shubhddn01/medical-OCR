from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PresciptionParser
from parser_patient import PatientParser

def extract(file_path,file_format):
    #extracting text from pdf file
    pages = convert_from_path(file_path)
    document_text=''

    if len(pages)>0:
        page=pages[0]
        processed_image=util.preprocess_image(page)
        text=pytesseract.image_to_string(processed_image)
        document_text='\n'+text
    
    if file_format== 'prescription' :
        details=PresciptionParser(document_text).parse()
        return print(details);
    elif file_format =='patient_details':
        details = PatientParser(document_text).parse()
        return print(details)
    else :
        raise  Exception("Invalid format")

if __name__ == '__main__':
    extract('backend/resources/patient_details/pd_1.pdf','patient_details')
    