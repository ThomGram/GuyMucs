
# GuyMucs

**GuyMucs** est une application graphique qui utilise **Demucs** pour isoler et séparer les instruments d’un fichier audio. L’utilisateur peut choisir un instrument spécifique (voix, batterie, basse, ou autres) pour extraire ses pistes, et l’application génère deux fichiers de sortie : l’instrument isolé et l’accompagnement restant.

## Fonctionnalités

- Sélection d’un ou plusieurs fichiers audio en entrée.
- Choix de l’instrument à isoler (voix, batterie, basse, autres).
- Production de deux fichiers de sortie : l’instrument isolé et le reste de la musique.
- Interface graphique simple et intuitive avec barre de progression.

## Prérequis

- **Python 3.8+**
- **ffmpeg** pour la gestion audio (installez-le via `conda` ou directement selon votre système).
- Modules Python nécessaires (voir `requirements.txt`).

## Installation

1. **Clonez le dépôt GitHub** :
   ```bash
   git clone <URL_DU_DEPOT>
   cd GuyMucs
   ```

2. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurez ffmpeg** :
   - Sur Ubuntu (si non installé via Conda) :
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - Sur macOS :
     ```bash
     brew install ffmpeg
     ```

## Utilisation

1. **Lancez l’application** :
   ```bash
   python -m guymucs.main
   ```

2. **Instructions dans l’interface** :
   - Sélectionnez un ou plusieurs fichiers audio.
   - Choisissez un dossier de sortie.
   - Sélectionnez l’instrument à isoler et lancez la séparation.
   - Une barre de progression indiquera l’avancement du traitement.

## Génération d'un exécutable (optionnel)

Pour distribuer **GuyMucs** sans nécessiter Python, vous pouvez créer un exécutable unique avec **PyInstaller** :

```bash
pyinstaller --onefile --name GuyMucs guymucs/main.py
```

L’exécutable sera disponible dans le dossier `dist`.

## Contribuer

1. **Forkez le projet** et clonez-le.
2. **Créez une branche** pour vos modifications :
   ```bash
   git checkout -b ma-branche
   ```
3. **Faites un commit** de vos modifications :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. **Poussez vos modifications** vers GitHub :
   ```bash
   git push origin ma-branche
   ```
5. **Ouvrez une pull request** pour discuter de vos changements.

