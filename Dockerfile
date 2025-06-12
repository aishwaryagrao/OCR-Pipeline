# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean 

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app


# Run the OCR script with default engine (can override with --image and --engine)
CMD ["python", "ocr.py", "data/569669.jpg", "pytesseract"]
