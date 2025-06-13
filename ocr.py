import cv2
import mlflow
import argparse

# OCR Options
import pytesseract
import easyocr

def run_ocr_pytesseract(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def run_ocr_easyocr(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)

def main(image_path, engine):
    mlflow.start_run()
    mlflow.log_param("engine", engine)
    mlflow.log_param("image", image_path)
    # data_dir = "data"

    # for fname in os.listdir(data_dir):
    if image_path.lower().endswith((".png", ".jpg", ".jpeg")):
        # path = os.path.join(data_dir, fname)

        if engine == "pytesseract":
            text = run_ocr_pytesseract(image_path)
        elif engine == "easyocr":
            text = run_ocr_easyocr(image_path)
        else:
            raise ValueError("Unsupported OCR engine. Use 'pytesseract' or 'easyocr'.")

        mlflow.log_text(text, "output.txt")

         # Save and log output text
        output_path = "output/"+ image_path + ".txt"
        with open(output_path, "w") as f:
            f.write(text)
        mlflow.log_artifact(output_path)

        print("OCR Output:\n", text)

    mlflow.end_run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OCR Pipeline")
    parser.add_argument("--image", required=True, help="Path to image file")
    parser.add_argument("--engine", type=str, default="pytesseract", choices=["pytesseract", "easyocr"], help="Choose OCR engine: pytesseract or easyocr")
    args = parser.parse_args()

    main(image_path = args.image, engine = args.engine)
