from PyPDF2 import PdfReader
from PyPDF2.generic import IndirectObject
import sys

def list_all_objects(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)

        for page_num, page in enumerate(reader.pages):
            print(f"Page {page_num + 1}")
            if '/Annots' in page:
                annotations = page['/Annots']
                for annot in annotations:
                    
                    annot_obj = annot.get_object()
                    if '/A' in annot_obj:
                        action = annot_obj['/A']
                        uri = action.get('/URI', {})
                        print(f"Link: {uri}")
                        print("-" * 50)

                    # obj_id = annot_obj.get('/P').idnum 
                    page_obj = annot_obj.get('/A', {})
                    if page_obj:
                        print("-" * 50)
                        try:
                            uri = annot_obj.get('/URI', {})
                            if uri:
                                print(f"Link: {uri}")
                                print("-" * 50)
                        except:
                            pass

            else:
                print("No annotations found on this page.")
                print("-" * 50)


if len(sys.argv) > 1:
    list_all_objects(sys.argv[1])
else:
    print("argv1 - PDF path")