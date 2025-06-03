import base64

def cesar(message, cle, mode='chiffrement'):
    decalage = len(cle)
    resultat = ""

    for char in message:
        if char.islower():
            base = ord('a')
        elif char.isupper():
            base = ord('A')
        else:
            resultat += char
            continue

        if mode == 'chiffrement':
            code = (ord(char) - base + decalage) % 26 + base
        elif mode == 'dechiffrement':
            code = (ord(char) - base - decalage) % 26 + base
        else:
            raise ValueError("Mode inconnu. Utilise 'chiffrement' ou 'dechiffrement'.")

        resultat += chr(code)

    return resultat


def encoder_base64(texte):
    return base64.b64encode(texte.encode()).decode()


def decoder_base64(texte_b64):
    return base64.b64decode(texte_b64.encode()).decode()


def main():
    print("=== Chiffrement César + Base64 ===")
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        message = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé : ")
        chiffré = cesar(message, cle, mode='chiffrement')
        encodé = encoder_base64(chiffré)
        print("\n🔐 Message chiffré + encodé :", encodé)

    elif choix == 'D':
        message_encodé = input("Entrez le message encodé à décoder : ")
        cle = input("Entrez la clé : ")
        try:
            décodé = decoder_base64(message_encodé)
        except Exception as e:
            print("Erreur de décodage base64 :", e)
            return
        déchiffré = cesar(décodé, cle, mode='dechiffrement')
        print("\n🔓 Message décodé + déchiffré :", déchiffré)

    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()
