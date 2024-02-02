from PIL import Image

class Code39BarcodeReader:
    CODE39_MAP = {
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

    def __init__(self, filename):
        self.filename = filename
        self.barcodeImage = Image.open(self.filename)
        self.image_width, self.image_height = self.barcodeImage.size
        self.vertical_midpoint = self.image_height // 2
        self.binary_string = ''

    def decode(self):
        self._convert_to_binary()
        self._transform_binary_string()
        self._remove_separator_zeros()
        self._decode_binary_string()
        return self.decoded_data

    def _convert_to_binary(self):
        barcodeBinary = []
        lastChar = ''
        for pixel in range(self.image_width-1):
            r, g, b = self.barcodeImage.getpixel((pixel, self.vertical_midpoint))
            if (r, g, b) == (255, 255, 255):
                currentChar = '0'
            elif (r, g, b) == (0, 0, 0):
                currentChar = '1'
            else:
                continue
            
            if currentChar != lastChar:
                barcodeBinary.append(' ')
            barcodeBinary.append(currentChar)
            lastChar = currentChar

        self.binary_string = ''.join(barcodeBinary)

    def _transform_binary_string(self):
        transformd_binary_string = self.binary_string.split(' ')
        length_map = [{'length': len(i), 'binary': i} for i in transformd_binary_string]
        # Normlaisation de la longueur
        average_length = (max(i['length'] for i in length_map) + min(i['length'] for i in length_map)) // 2
        length_map = [i for i in length_map if i['length'] >= average_length]
        self.new_binary_string = ''.join([i['binary'][0] * (i['length'] // average_length) for i in length_map])
        self.new_binary_string += '1' 

    def _remove_separator_zeros(self):
        self.new_binary_string = ''.join([self.new_binary_string[i] for i in range(len(self.new_binary_string)) if (i + 1) % 13 != 0])

    def _decode_binary_string(self):
        CODE39_MAP_INVERTED = {v: k for k, v in self.CODE39_MAP.items()}
        valid_segments = []
        for i in range(0, len(self.new_binary_string), 12):
            segment = self.new_binary_string[i:i+12]
            if segment in CODE39_MAP_INVERTED:
                valid_segments.append(segment)
        self.decoded_data = ''.join(CODE39_MAP_INVERTED.get(seg, '?') for seg in valid_segments)
