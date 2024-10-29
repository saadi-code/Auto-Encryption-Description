class Rotor:
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring
        self.notch = ord(notch) - ord('A')
        self.position = position

    def rotate(self):
        return False  # Pas de rotation

    def encrypt_forward(self, char):
        # Convertir le caractère en un index, appliquer le décalage de position
        index = (ord(char) - ord('A') + self.position) % 26
        # Transformer le caractère en utilisant le câblage du rotor
        encrypted_char = self.wiring[index]
        # Reconvertir en prenant en compte le décalage de position inverse
        result = chr((ord(encrypted_char) - ord('A') - self.position) % 26 + ord('A'))
        print(f"encrypt_forward - {char} -> {result}")
        return result

    def encrypt_backward(self, char):
        # Inverser le câblage du rotor
        index = (self.wiring.index(char) - self.position + 26) % 26
        # Transformer en prenant en compte le décalage de position inverse
        result = chr((index + ord('A') + self.position) % 26 + ord('A'))
        print(f"encrypt_backward - {char} -> {result}")
        return result

# Test minimal pour vérifier la symétrie
rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    encrypted_char = rotor.encrypt_forward(char)
    decrypted_char = rotor.encrypt_backward(encrypted_char)
    assert char == decrypted_char, f"Erreur avec le caractère {char}"

print("Symétrie correcte pour chaque lettre.")