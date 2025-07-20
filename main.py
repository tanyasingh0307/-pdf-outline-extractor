from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import json
import os

def extract_outline(pdf_path):
    outline = []
    max_font_size = 0
    title = ""

    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    font_sizes = [char.size for char in text_line if isinstance(char, LTChar)]
                    if font_sizes:
                        avg_font = sum(font_sizes) / len(font_sizes)
                        text = text_line.get_text().strip()

                        if avg_font > max_font_size:
                            max_font_size = avg_font
                            title = text

                        if avg_font >= 18:
                            level = "H1"
                        elif avg_font >= 14:
                            level = "H2"
                        elif avg_font >= 12:
                            level = "H3"
                        else:
                            continue

                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return {"title": title, "outline": outline}

def process_all_pdfs(input_dir, output_dir):
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            result = extract_outline(pdf_path)
            output_file = os.path.splitext(file)[0] + ".json"
            with open(os.path.join(output_dir, output_file), "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    process_all_pdfs("/app/input", "/app/output")
