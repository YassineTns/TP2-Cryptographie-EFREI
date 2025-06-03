# 🔐 TP2 Cryptographie — EFREI

## ✅ Partie 1 — Chiffrement de César + Encodage Base64

### 📄 Fichier :
`code/cesar.py`

### 🧠 Principe

Le chiffrement de César dans ce script est couplé à un encodage en Base64 pour renforcer la dissimulation du message.

- **Chiffrement :**
  1. Le message est chiffré avec la méthode de César.
  2. Le message chiffré est ensuite encodé en Base64.

- **Déchiffrement :**
  1. Le message est d'abord décodé de Base64.
  2. Le message est ensuite déchiffré via la méthode de César.

Le **décalage** utilisé pour César est automatiquement défini comme la **longueur de la clé** fournie par l’utilisateur.

### ⚙️ Exécution

```bash
python code/cesar.py
```

Une fois lancé, le script vous demandera :

- de choisir entre chiffrement (C) ou déchiffrement (D),
- d’entrer un message,
- de saisir une clé.

### 🧪 Exemple de chiffrement

```
Message : Bonjour EFREI
Clé     : CLE
=> Chiffré + Base64 : HFWQMRWJKIU=
```

---

## ✅ Partie 2 — Chiffrement de Vigenère

### 📄 Fichier :
`code/vigenere.py`

### 🧠 Principe

Le chiffrement de **Vigenère** repose sur l’utilisation répétée d’une **clé** pour chiffrer chaque lettre du message avec un décalage variable.

- Chaque lettre du message est décalée selon la position de la lettre correspondante de la clé.
- La clé est **répétée en boucle** pour couvrir tout le message.

### 🔁 Fonctionnalités

- Les lettres sont automatiquement transformées en majuscules.
- Les caractères spéciaux, chiffres et espaces ne sont **pas modifiés**.
- Mode interactif via le terminal.

### ⚙️ Exécution

```bash
python code/vigenere.py
```

Le script vous demande :

- si vous voulez chiffrer (C) ou déchiffrer (D),
- le message,
- la clé.

### 🧪 Exemple

```
Message : Bonjour tout le monde
Clé     : CLE
=> Message chiffré : DXOHSSV VSCV NI QSRHFI
```
