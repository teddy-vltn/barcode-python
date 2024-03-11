from PIL import Image, ImageDraw

# TODO : Ajouter la quiet zone
class Code39BarcodeGenerator:
    def __init__(self, data, barcode_type="code39"):
        self.data = data.upper()  # Le Code 39 est toujours en majuscules
        self.barcode_type = barcode_type
        self.barcode_map = self._get_code39_map()
        self.image = None

    def _get_code39_map(self):
        # Mapping des caractères aux séquences pour Code 39
        # voir https://en.wikipedia.org/wiki/Code_39
        return {
            '1': '110100101011', '2': '101100101011', '3': '110110010101', '4': '101001101011',
            '5': '110100110101', '6': '101100110101', '7': '101001011011', '8': '110100101101',
            '9': '101100101101', '0': '101001101101', 'A': '110101001011', 'B': '101101001011',
            'C': '110110100101', 'D': '101011001011', 'E': '110101100101', 'F': '101101100101',
            'G': '101010011011', 'H': '110101001101', 'I': '101101001101', 'J': '101011001101',
            'K': '110101010011', 'L': '101101010011', 'M': '110110101001', 'N': '101011010011',
            'O': '110101101001', 'P': '101101101001', 'Q': '101010110011', 'R': '110101011001',
            'S': '101101011001', 'T': '101011011001', 'U': '110010101011', 'V': '100110101011',
            'W': '110011010101', 'X': '100101101011', 'Y': '110010110101', 'Z': '100110110101',
            '-': '100101011011', '.': '110010101101', ' ': '100110101101', '*': '100101101101',
        }

    def generate(self, width=2, height=100):
        # Convertir la chaîne d'entrée en motif de code-barres
        encoded_data = '*' + self.data + '*'  # Ajoute les caractères de début et de fin
        # Ajoute un espace entre chaque caractère
        pattern = ''.join([self.barcode_map[char] + '0' for char in encoded_data])[:-1]

        # Calculer la largeur de l'image
        image_width = sum([width if bit == '1' else width for bit in pattern])
        
        # Créer l'image
        self.image = Image.new('RGB', (image_width, height), 'white')
        draw = ImageDraw.Draw(self.image)

        # Dessiner le code-barres
        x = 0
        for bit in pattern:
            if bit == '1':
                draw.rectangle([x, 0, x + width - 1, height], fill='black')
            x += width

    def save(self, filepath):
        if self.image:
            self.image.save(filepath)
        else:
            print("Aucun code-barres généré.")

    def show(self):
        if self.image:
            self.image.show()
        else:
            print("Aucun code-barres généré.")

