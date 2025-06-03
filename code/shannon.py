import hashlib

def xor(message, cle):
    """Effectue un XOR entre chaque caractère du message et de la clé (en boucle)."""
    resultat = ""
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(cle[i % len(cle)])  # boucle sur la clé
        r = m ^ k  # opération XOR
        resultat += format(r, '02x')  # on ajoute en hexadécimal (2 chiffres)
    return resultat

def main():
    print("=== 🔐 Confusion (Shannon) avec XOR + SHA-256 ===")
    message = input("Entrez un message : ")
    cle = input("Entrez une clé : ")

    # Étape 1 : XOR
    xor_result = xor(message, cle)
    print("\nRésultat du XOR (hexadécimal) :", xor_result)

    # Étape 2 : SHA-256
    hash_result = hashlib.sha256(xor_result.encode()).hexdigest()
    print("🔐 SHA-256 du résultat XOR :", hash_result)

if __name__ == "__main__":
    main()
