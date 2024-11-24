# utils.py
import pytesseract
from PIL import Image
from typing import List, Dict

class OCRModel:
    print('Hello from OCRModel')
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OCRModel, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # إعدادات Tesseract (تأكد من أن Tesseract مثبت ومضاف إلى PATH)
        self.allergens = {
            'nuts', 'wheat', 'dairy', 'eggs', 'fish','sugar',
            'soybeans', 'strawberries', 'peanuts', 'shellfish'
        }

    def process_image(self, image_path: str, user_allergies: List[str]) -> Dict:
        try:
            # قراءة النص من الصورة باستخدام Tesseract
            extracted_text = pytesseract.image_to_string(Image.open(image_path))
            extracted_text = extracted_text.lower()

            found_allergens = []
            for allergen in self.allergens:
                if allergen.lower() in extracted_text:
                    found_allergens.append(allergen)

            dangerous_allergens = [
                allergen for allergen in found_allergens
                if allergen.lower() in [a.lower() for a in user_allergies]
            ]

            return {
                "extracted_text": extracted_text,
                "found_ingredients": found_allergens,
                "dangerous_allergens": dangerous_allergens,
                "is_safe": len(dangerous_allergens) == 0
            }

        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")