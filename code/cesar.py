# === TP2 de Cryptographie - EFREI ===
# Auteur : Yassine Gouja
# Sujet : Chiffrement de César + Encodage Base64 avec déchiffrement

import base64

# Fonction de chiffrement ou déchiffrement de César
def cesar(message, cle, mode='chiffrement'):
    resultat = ""  # Chaîne résultat à retourner
    decalage = len(cle)  # Le décalage est déterminé par la longueur de la clé

    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            base = ord('A') if char.isupper() else ord('a')  # Majuscule ou minuscule

            if mode == 'chiffrement':
                code = (ord(char) - base + decalage) % 26 + base  # Application du décalage
            elif mode == 'dechiffrement':
                code = (ord(char) - base - decalage) % 26 + base  # Décalage inverse
            else:
                raise ValueError("Mode inconnu. Utilise 'chiffrement' ou 'dechiffrement'.")

            resultat += chr(code)  # Ajoute le caractère transformé au résultat
        else:
            resultat += char  # Garde les caractères non alphabétiques inchangés

    return resultat  # Retourne le message transformé

# Fonction principale
def main():
    print("=== Chiffrement César + Base64 ===")

    # Demande à l'utilisateur s'il souhaite chiffrer ou déchiffrer
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        # CHIFFREMENT
        message = input("Entrez le message à chiffrer : ")  # Message brut
        cle = input("Entrez la clé (ex: ABC) : ")  # Clé utilisée pour décaler

        chiffre = cesar(message, cle, mode='chiffrement')  # Chiffrement César
        encodage = base64.b64encode(chiffre.encode()).decode()  # Encodage en base64

        print("\n🔐 Message chiffré + encodé :", encodage)

    elif choix == 'D':
        # DÉCHIFFREMENT
        message = input("Entrez le message encodé à décoder : ")
        cle = input("Entrez la clé : ")

        try:
            decode = base64.b64decode(message).decode()  # Décodage base64
        except Exception as e:
            print("❌ Erreur de décodage base64 :", e)
            return

        dechiffre = cesar(decode, cle, mode='dechiffrement')  # Déchiffrement César
        print("\n📂 Message décodé + déchiffré :", dechiffre)

    else:
        print("Choix invalide. Tapez 'C' ou 'D'.")

# Exécution du programme si ce fichier est exécuté directement
if __name__ == "__main__":
    main()
