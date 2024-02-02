from PIL import Image, ImageDraw

class Code128BarcodeGenerator:
    def __init__(self, data):
        self.data = data
        self.weights = self._get_weights()
        self.code128a = self._get_code128a()
        self.code128b = self._get_code128b()
        self.code128c = self._get_code128c()
        self.image = None

    def _get_weights(self):
        return {0: '212222', 1: '222122', 2: '222221', 
           3: '121223', 4: '121322', 5: '131222', 
           6: '122213', 7: '122312', 8: '132212', 
           9: '221213', 10: '221312', 11: '231212',
           12: '112232', 13: '122132', 14: '122231', 
           15: '113222', 16: '123122', 17: '123221', 
           18: '223211', 19: '221132', 20: '221231', 
           21: '213212', 22: '223112', 23: '312131', 
           24: '311222', 25: '321122', 26: '321221', 
           27: '312212', 28: '322112', 29: '322211', 
           30: '212123', 31: '212321', 32: '232121', 
           33: '111323', 34: '131123', 35: '131321', 
           36: '112313', 37: '132113', 38: '132311', 
           39: '211313', 40: '231113', 41: '231311', 
           42: '112133', 43: '112331', 44: '132131', 
           45: '113123', 46: '113321', 47: '133121', 
           48: '313121', 49: '211331', 50: '231131', 
           51: '213113', 52: '213311', 53: '213131', 
           54: '311123', 55: '311321', 56: '331121', 
           57: '312113', 58: '312311', 59: '332111', 
           60: '314111', 61: '221411', 62: '431111', 
           63: '111224', 64: '111422', 65: '121124', 
           66: '121421', 67: '141122', 68: '141221', 
           69: '112214', 70: '112412', 71: '122114', 
           72: '122411', 73: '142112', 74: '142211', 
           75: '241211', 76: '221114', 77: '413111', 
           78: '241112', 79: '134111', 80: '111242', 
           81: '121142', 82: '121241', 83: '114212', 
           84: '124112', 85: '124211', 86: '411212', 
           87: '421112', 88: '421211', 89: '212141', 
           90: '214121', 91: '412121', 92: '111143', 
           93: '111341', 94: '131141', 95: '114113', 
           96: '114311', 97: '411113', 98: '411311', 
           99: '113141', 100: '114131', 101: '311141', 
           102: '411131', 103: '211412', 104: '211214', 
           105: '211232', 106: '2331112'}

    def _get_code128a(self):
        return {' ': 0, '!': 1, '"': 2, 
            '#': 3, '$': 4, '%': 5, 
            '&': 6, "'": 7, '(': 8, 
            ')': 9, '*': 10, '+': 11, 
            ',': 12, '-': 13, '.': 14, 
            '/': 15, '0': 16, '1': 17, 
            '2': 18, '3': 19, '4': 20, 
            '5': 21, '6': 22, '7': 23, 
            '8': 24, '9': 25, ':': 26, 
            ';': 27, '<': 28, '=': 29, 
            '>': 30, '?': 31, '@': 32, 
            'A': 33, 'B': 34, 'C': 35, 
            'D': 36, 'E': 37, 'F': 38, 
            'G': 39, 'H': 40, 'I': 41, 
            'J': 42, 'K': 43, 'L': 44, 
            'M': 45, 'N': 46, 'O': 47, 
            'P': 48, 'Q': 49, 'R': 50, 
            'S': 51, 'T': 52, 'U': 53, 
            'V': 54, 'W': 55, 'X': 56, 
            'Y': 57, 'Z': 58, '[': 59, 
            '\\': 60, ']': 61, '^': 62, 
            '_': 63, 'NUL': 64, 'SOH': 65, 
            'STX': 66, 'ETX': 67, 'EOT': 68, 
            'ENQ': 69, 'ACK': 70, 'BEL': 71, 
            'BS': 72, 'HT': 73, 'LF': 74, 
            'VT': 75, 'FF': 76, 'CR': 77, 
            'SO': 78, 'SI': 79, 'DLE': 80, 
            'DC1': 81, 'DC2': 82, 'DC3': 83, 
            'DC4': 84, 'NAK': 85, 'SYN': 86, 
            'ETB': 87, 'CAN': 88, 'EM': 89, 
            'SUB': 90, 'ESC': 91, 'FS': 92, 
            'GS': 93, 'RS': 94, 'US': 95, 
            'FNC3': 96, 'FNC2': 97, 'ShiftB': 98, 
            'CodeC': 99, 'CodeB': 100, 'FNC4': 101, 
            'FNC1': 102, 'StartA': 103, 'StartB': 104, 
            'StartC': 105, 'Stop': 106}

    def _get_code128b(self):
        return {' ': 0, '!': 1, '"': 2, 
            '#': 3, '$': 4, '%': 5, 
            '&': 6, "'": 7, '(': 8, 
            ')': 9, '*': 10, '+': 11, 
            ',': 12, '-': 13, '.': 14,
            '/': 15, '0': 16, '1': 17, 
            '2': 18, '3': 19, '4': 20, 
            '5': 21, '6': 22, '7': 23, 
            '8': 24, '9': 25, ':': 26, 
            ';': 27, '<': 28, '=': 29, 
            '>': 30, '?': 31, '@': 32, 
            'A': 33, 'B': 34, 'C': 35, 
            'D': 36, 'E': 37, 'F': 38, 
            'G': 39, 'H': 40, 'I': 41, 
            'J': 42, 'K': 43, 'L': 44, 
            'M': 45, 'N': 46, 'O': 47, 
            'P': 48, 'Q': 49, 'R': 50, 
            'S': 51, 'T': 52, 'U': 53, 
            'V': 54, 'W': 55, 'X': 56, 
            'Y': 57, 'Z': 58, '[': 59, 
            '\\': 60, ']': 61, '^': 62, 
            '_': 63, '`': 64, 'a': 65, 
            'b': 66, 'c': 67, 'd': 68, 
            'e': 69, 'f': 70, 'g': 71, 
            'h': 72, 'i': 73, 'j': 74, 
            'k': 75, 'l': 76, 'm': 77, 
            'n': 78, 'o': 79, 'p': 80, 
            'q': 81, 'r': 82, 's': 83, 
            't': 84, 'u': 85, 'v': 86, 
            'w': 87, 'x': 88, 'y': 89, 
            'z': 90, '{': 91, '|': 92, 
            '}': 93, '~': 94, 'DEL': 95, 
            'FNC3': 96, 'FNC2': 97, 'ShiftA': 98, 
            'CodeC': 99, 'FNC4': 100, 'CodeA': 101,
            'FNC1': 102, 'StartA': 103, 'StartB': 104, 
            'StartC': 105, 'Stop': 106}

    def _get_code128c(self):
        return {'00': 0, '01': 1, '02': 2, 
             '03': 3, '04': 4, '05': 5, 
             '06': 6, '07': 7, '08': 8, 
             '09': 9, '10': 10, '11': 11, 
             '12': 12, '13': 13, '14': 14, 
             '15': 15, '16': 16, '17': 17, 
             '18': 18, '19': 19, '20': 20, 
             '21': 21, '22': 22, '23': 23, 
             '24': 24, '25': 25, '26': 26, 
             '27': 27, '28': 28, '29': 29, 
             '30': 30, '31': 31, '32': 32, 
             '33': 33, '34': 34, '35': 35, 
             '36': 36, '37': 37, '38': 38, 
             '39': 39, '40': 40, '41': 41, 
             '42': 42, '43': 43, '44': 44, 
             '45': 45, '46': 46, '47': 47, 
             '48': 48, '49': 49, '50': 50, 
             '51': 51, '52': 52, '53': 53, 
             '54': 54, '55': 55, '56': 56, 
             '57': 57, '58': 58, '59': 59, 
             '60': 60, '61': 61, '62': 62, 
             '63': 63, '64': 64, '65': 65, 
             '66': 66, '67': 67, '68': 68, 
             '69': 69, '70': 70, '71': 71, 
             '72': 72, '73': 73, '74': 74, 
             '75': 75, '76': 76, '77': 77, 
             '78': 78, '79': 79, '80': 80, 
             '81': 81, '82': 82, '83': 83, 
             '84': 84, '85': 85, '86': 86, 
             '87': 87, '88': 88, '89': 89, 
             '90': 90, '91': 91, '92': 92, 
             '93': 93, '94': 94, '95': 95, 
             '96': 96, '97': 97, '98': 98, 
             '99': 99, 'CodeB': 100, 'CodeA': 101, 
             'FNC1': 102, 'StartA': 103, 'StartB': 104, 
             'StartC': 105, 'Stop': 106}

    def _get_weight_sequence(self, codes):
        # Méthode pour convertir codes en séquence de poids
        # C'est à dire, convertir les codes en séquence de barres et d'espaces de largeur variable
        # Sous le format NBNBNBNBNBN où N est une barre ou un espace noir et B est une barre ou un espace blanc
        # Le nombre associé a chaque code est utilisé pour déterminer la largeur de la barre ou de l'espace
        # Donc 3321 correspond a une barre noire de largeur 3, une barre blanche de largeur 3, une barre noire de largeur 2 et une barre blanche de largeur 1
        return ''.join(self.weights[code] for code in codes)

    def _calculate_checksum(self, codes):
        # Méthode pour calculer le code de somme de contrôle
        # voir https://en.wikipedia.org/wiki/Code_128#Check_digit_calculation
        checksum = codes[0]
        for i in range(1, len(codes)):
            checksum += i * codes[i]
        return checksum % 103

    def _encode_data_with_dynamic_charset(self):
        # Méthode pour encoder les données en utilisant le jeu de caractères dynamique
        # voir https://en.wikipedia.org/wiki/Code_128#Subtypes
        text = str(self.data)
        pos = 0
        length = len(text)
        
        if text[:2].isdigit():
            charset = self.code128c
            codes = [charset['StartC']]
            codes_key = ["StartC"]
        elif text[0].isupper() or text[0] in self.code128a:
            charset = self.code128a
            codes = [charset['StartA']]
            codes_key = ["StartA"]
        else:
            charset = self.code128b
            codes = [charset['StartB']]
            codes_key = ["StartB"]

        while pos < length:
            if charset is self.code128c:
                if text[pos:pos+2].isdigit() and length - pos > 1:
                    codes.append(int(text[pos:pos+2]))
                    codes_key.append(text[pos:pos+2])
                    pos += 2
                else:
                    codes.append(charset['CodeB'])
                    codes_key.append('CodeB')
                    charset = self.code128b
            elif charset is self.code128b:
                if text[pos:pos+4].isdigit() and length - pos >= 4:
                    codes.append(charset['CodeC'])
                    codes_key.append('CodeC')
                    charset = self.code128c
                elif text[pos].isupper() or text[pos] in self.code128a:
                    codes.append(charset['CodeA'])
                    codes_key.append('CodeA')
                    charset = self.code128a
                else:
                    codes.append(charset[text[pos]])
                    codes_key.append(text[pos])
                    pos += 1
            else:  # Code A
                if text[pos:pos+4].isdigit() and length - pos >= 4:
                    codes.append(charset['CodeC'])
                    codes_key.append('CodeC')
                    charset = self.code128c
                elif not (text[pos].isupper() or text[pos] in self.code128a):
                    codes.append(charset['CodeB'])
                    codes_key.append('CodeB')
                    charset = self.code128b
                else:
                    codes.append(charset[text[pos]])
                    codes_key.append(text[pos])
                    pos += 1

       # print(codes_key)

        checksum_code = self._calculate_checksum(codes)
        codes.append(checksum_code)
        codes.append(charset['Stop'])

        return codes


    def generate(self, height=100, thickness=3, quiet_zone=True):
        # Générer le code-barres
        data_codes = self._encode_data_with_dynamic_charset()
        weight_sequence = self._get_weight_sequence(data_codes)
        
        # Initialiser l'image
        total_width = sum(int(weight) * thickness for weight in weight_sequence) + (20 * thickness if quiet_zone else 0)
        img = Image.new('1', (total_width, height), 1)  # Fond blanc
        draw = ImageDraw.Draw(img)

        # Dessiner le code-barres
        x = 10 * thickness if quiet_zone else 0
        draw_bar = True  # Commencer par dessiner une barre
        for weight in weight_sequence:
            width = int(weight) * thickness
            if draw_bar:
                draw.rectangle(((x, 0), (x + width - 1, height)), fill=0)  # Dessiner une barre noire
            # Pas besoin de dessiner explicitement les espaces blancs
            draw_bar = not draw_bar  # Alterner entre barre et espace
            x += width

        self.image = img
        return img

    def show(self):
        if self.image:
            self.image.show()
        else:
            print("Aucun code-barres généré.")

    def save(self, filepath):
        if self.image:
            self.image.save(filepath)
        else:
            print("Aucun code-barres généré.")
