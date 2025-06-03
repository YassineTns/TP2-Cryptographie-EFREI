# 🔐 Fonctions pour le chiffrement et déchiffrement de Vigenère

def vigenere_chiffrement(message, cle):
    """
    Chiffre le message en utilisant le chiffrement de Vigenère avec la clé donnée.
    """
    resultat = ""
    cle = cle.upper()
    message = message.upper()
    i = 0

    for char in message:
        if char.isalpha():
            decalage = ord(cle[i % len(cle)]) - ord('A')
            nouveau = chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
            resultat += nouveau
            i += 1
        else:
            resultat += char
    return resultat


def vigenere_dechiffrement(message, cle):
    """
    Déchiffre un message chiffré avec Vigenère.
    """
    resultat = ""
    cle = cle.upper()
    message = message.upper()
    i = 0

    for char in message:
        if char.isalpha():
            decalage = ord(cle[i % len(cle)]) - ord('A')
            original = chr((ord(char) - ord('A') - decalage) % 26 + ord('A'))
            resultat += original
            i += 1
        else:
            resultat += char
    return resultat


# 💬 Mode interactif si tu exécutes directement le fichier
if __name__ == "__main__":
    print("=== Chiffrement de Vigenère ===")
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        message = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé : ")
        crypte = vigenere_chiffrement(message, cle)
        print("\n🔐 Message chiffré :", crypte)

    elif choix == 'D':
        message = input("Entrez le message à déchiffrer : ")
        cle = input("Entrez la clé utilisée : ")
        decrypte = vigenere_dechiffrement(message, cle)
        print("\n🔓 Message déchiffré :", decrypte)

    else:
        print("❌ Choix invalide. Tapez 'C' pour chiffrer ou 'D' pour déchiffrer.")
