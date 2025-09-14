import fitz  # PyMuPDF
import json


def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def simple_parse_licensing_text(raw_text):

    #Searching for wors with common conditions 
    
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]
    
    # Takes sections with key words 
    
    keywords = ["גז", "בשר", "משלוח", "מטבח", "תפוסה", "מזון"]
    extracted = []
    for line in lines:
        for k in keywords:
            if k in line:
                extracted.append(line)
                break
    return extracted




def save_processed_data(extracted_lines, output_file="data\processed.json"):
    data = []
    for i, line in enumerate(extracted_lines):
        data.append({
            "id": i+1,
            "text": line,
            "tags": [] # אפשר להוסיף תגיות לפי מילת מפתח 
        })
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return output_file

#For Testing
if __name__ == "__main__":
    from pathlib import Path
    pdf_path = Path("data\Business_Licence.pdf")
    text = extract_text_from_pdf(pdf_path)
    extracted = simple_parse_licensing_text(text)
    save_processed_data(extracted)
    print("Processed JSON saved successfully.")


