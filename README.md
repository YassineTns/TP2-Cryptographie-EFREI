# 🔐 TP2 Cryptographie — EFREI

## Partie 1 — Chiffrement de César + Encodage Base64

Ce script Python permet de chiffrer ou déchiffrer un message en combinant :

- le **chiffrement de César**, où le décalage est basé sur la longueur d'une clé,
- l'**encodage Base64**, qui rend le texte encore plus difficile à lire.

---

### 📄 Fichier principal :
`code/cesar.py`

---

### 🧠 Principe

- **Chiffrement** :
  - Le texte est d'abord chiffré avec le chiffrement de César (décalage = longueur de la clé).
  - Ensuite, le résultat est encodé en Base64.

- **Déchiffrement** :
  - Le texte est d'abord décodé depuis Base64.
  - Ensuite, il est déchiffré avec la même clé (décalage inversé).

---

### ⚙️ Utilisation

```bash
python code/cesar.py
