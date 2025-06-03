# TP2 de Cryptographie - EFREI
# Auteur : Yassine Gouja
# Sujet : Chiffrement de César, Vigenère et confusion (Shannon)

def cesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def cesar_decrypt(ciphertext, shift):
    return cesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    message = "Bonjour EFREI"
    shift = 3

    encrypted = cesar_encrypt(message, shift)
    print("🔐 Chiffrement de César :", encrypted)

    decrypted = cesar_decrypt(encrypted, shift)
    print("🔓 Déchiffrement :", decrypted)

