from code128 import Code128BarcodeGenerator
from code39 import Code39BarcodeGenerator
from code39_reader import Code39BarcodeReader

# Créer un code-barres Code 128
barcode = Code128BarcodeGenerator("Hello, World!")
barcode.generate()
barcode.show()

# Créer un code-barres Code 39
barcode = Code39BarcodeGenerator("HELLO WORLD")
barcode.generate()
barcode.show()

# Lire un code-barres Code 39 avec une taille de barre différente
# Taille de barre : 2 pixels
reader = Code39BarcodeReader("code39_code39_2.png")
decoded_data = reader.decode()
print(decoded_data)

# Taille de barre : 3 pixels
reader = Code39BarcodeReader("code39_code39_3.png")
decoded_data = reader.decode()
print(decoded_data)

