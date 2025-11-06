# Jeu de Billes 

## 🎮 Description

Ce projet est un **jeu de billes pour deux joueurs** développé en **Python** avec la bibliothèque **Pygame**.
Chaque joueur commence avec un nombre fixe de billes (par défaut 10). À tour de rôle, les joueurs misent des billes dans un carré central puis lancent leurs billes sur celles de l’adversaire.

* Si la bille lancée **reste dans le carré**, elle devient une nouvelle mise.
* Si elle **sort du carré** en poussant d’autres billes, le joueur **collecte toutes les billes sorties**.
* Le joueur qui **n’a plus de billes à miser perd** la partie.

Ce jeu simule les règles classiques du jeu de billes traditionnel avec une interface graphique simple et intuitive.

---

## 🧱 Fonctionnalités

* Gestion de **2 joueurs** avec tour par tour.
* Affichage du **nombre de billes de chaque joueur**.
* Possibilité de **lancer les billes avec la souris**.
* Détection des **collisions entre billes** et avec les murs du carré.
* Collecte automatique des billes sorties du carré.
* **Victoire** lorsqu’un joueur n’a plus de billes.

---

## ⚙️ Installation

1. Cloner le projet :

```bash
git clone <URL_DU_PROJET>
cd jeu_billes
```

2. Créer un environnement virtuel (optionnel mais recommandé) :

```bash
python -m venv venv
```

3. Activer l’environnement :

* **Windows :** `venv\Scripts\activate`
* **macOS/Linux :** `source venv/bin/activate`

4. Installer les dépendances :

```bash
pip install pygame
```

---

## 🚀 Utilisation

Pour lancer le jeu :

```bash
python src/main.py
```

Le jeu démarre avec :

* Le carré central affiché.
* Les billes de chaque joueur à disposition.
* Le score de chaque joueur affiché en haut.

---

## 📁 Arborescence du projet

```
jeu_billes/
│
├─ main.py
├─ README.md
├─ src/
│  ├─ settings.py
│  ├─ game_manager.py
│  ├─ physics.py
│  ├─ ui.py
│  ├─ input_handler.py
│  ├─ entities/
│  │   ├─ bille.py
│  │   └─ player.py
│  └─ scenes/
│      ├─ menu.py
│      ├─ play_scene.py
│      └─ game_over.py
├─ assets/
│  ├─ images/
│  ├─ sounds/
│  └─ fonts/
├─ data/
│  └─ scores.json
└─ tests/
    └─ test_collisions.py
```

---

## 📝 Configuration

Toutes les **constantes du jeu** (taille fenêtre, couleurs, taille du carré, rayon des billes…) sont définies dans `src/settings.py`.
Tu peux modifier ces valeurs pour personnaliser le jeu facilement.




