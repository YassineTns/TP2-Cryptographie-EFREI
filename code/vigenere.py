# === VIGENERE.PY ===
# Ce script permet de chiffrer et déchiffrer un message à l'aide du chiffrement de Vigenère.

# Fonction de chiffrement Vigenère
def vigenere_chiffrement(message, cle):
    """
    Chiffre un message en utilisant la méthode de Vigenère.
    Le message et la clé sont convertis en majuscules pour normaliser le traitement.

    :param message: str - texte à chiffrer
    :param cle: str - clé de chiffrement
    :return: str - message chiffré
    """
    resultat = ""
    cle = cle.upper()          # On met la clé en majuscules
    message = message.upper()  # On met aussi le message en majuscules
    i = 0  # Index pour parcourir les lettres de la clé

    for char in message:
        if char.isalpha():  # On chiffre uniquement les lettres alphabétiques
            decalage = ord(cle[i % len(cle)]) - ord('A')  # Calcule le décalage avec la lettre de la clé
            nouveau = chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))  # Applique le décalage
            resultat += nouveau
            i += 1  # On passe à la lettre suivante de la clé
        else:
            resultat += char  # Les caractères non alphabétiques ne sont pas modifiés
    return resultat


# Fonction de déchiffrement Vigenère
def vigenere_dechiffrement(message, cle):
    """
    Déchiffre un message chiffré avec Vigenère.

    :param message: str - texte à déchiffrer
    :param cle: str - clé utilisée pour le chiffrement
    :return: str - message déchiffré
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


# Fonction principale qui gère l'interaction utilisateur
def main():
    print("=== Chiffrement de Vigenère ===")
    choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer ? ").strip().upper()

    if choix == 'C':
        message = input("Entrez le message à chiffrer : ")
        cle = input("Entrez la clé : ")
        crypte = vigenere_chiffrement(message, cle)
        print("\nMessage chiffré :", crypte)

    elif choix == 'D':
        message = input("Entrez le message à déchiffrer : ")
        cle = input("Entrez la clé utilisée : ")
        decrypte = vigenere_dechiffrement(message, cle)
        print("\nMessage déchiffré :", decrypte)

    else:
        print("Choix invalide. Tapez 'C' pour chiffrer ou 'D' pour déchiffrer.")


# Lancement automatique de la fonction main si le fichier est exécuté directement
if __name__ == "__main__":
    main()
