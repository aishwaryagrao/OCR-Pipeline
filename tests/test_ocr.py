import unittest
from ocr import run_ocr_pytesseract, run_ocr_easyocr

class TestOCR(unittest.TestCase):
    def test_easyocr(self):
        result = run_ocr_easyocr("data/569669.jpg")
        self.assertTrue(len(result) > 0)

    def test_tesseract(self):
        result = run_ocr_pytesseract("data/569669.jpg")
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()