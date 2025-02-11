# Cosmics Arduino

Quelques fichiers pour tester l'Arduino et la Ultimate GPS breakout.

## Lecture carte Ultimate GPS breakout usb

- Brancher micro-usb sur la carte
- Récupérer le nom du port série en faisant `ls /dev`
- Ouvrir une session screen vers ce port série `screen /dev/tty.XXXX 9600`

## Pré-requis:

- [PlatformIO](https://docs.platformio.org/en/stable/core/installation/index.html)
- [VS Code plugin](https://platformio.org/install/ide?install=vscode)

## Instructions très basiques

- Cloner ce répository
- Ouvrir dans VSCode
- Faire "Build" puis "Upload"
- Ouvrir le "Serial Monitor" intégré

## Enregistrer la sortie série dans un fichier

- Install `pyserial` via `python3 -m pip install pyserial`
- Éditer le script log.py en changeant notamment le port série et le nom du fichier de sortie
- Exécuter `python3 log.py`