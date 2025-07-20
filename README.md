# Adobe Hackathon – PDF Outline Extractor

## 🧠 Approach
Uses `pdfminer.six` to:
- Parse text elements and font size
- Identify headings by font size ranges
- Capture page numbers and structure

## 🔧 How to Run
```
docker build --platform linux/amd64 -t mysolution:uniqueid .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolution:uniqueid
```

## 📦 Dependencies
- Python 3.10
- pdfminer.six
