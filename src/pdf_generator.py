import json
import os

class PDFGenerator:
    @staticmethod
    def load_mapping():
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, '..', 'mapping.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            mapping = json.load(file)
        return mapping

    @staticmethod
    def generate():
        mapping = PDFGenerator.load_mapping()
        print("Generating PDF...")
        print(mapping)