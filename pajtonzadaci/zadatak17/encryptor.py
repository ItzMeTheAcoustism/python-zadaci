class ShiftCipher:
    def __init__(self, ceasar_shift):
        self.ceasar_shift = ceasar_shift
    def encrypt(self, plaintext):
        self.plaintext = plaintext
        encrypted_text = ""
        for character in plaintext:
            match_found = False
            for key, value in self.ceasar_shift.items():
                if character == key[0] or character == key[1]:
                    if character.isupper():
                        encrypted_text += value[0]
                    else:
                        encrypted_text += value[1]
                        match_found = True
                        break
            if not match_found:
                encrypted_text += character
        return
