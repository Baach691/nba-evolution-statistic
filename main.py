#!/usr/bin/env python3
"""Lance simultanément les deux scripts de génération de graphiques :
par défaut `3pts_evolution.py` et `pace_evolution.py`.

Chaque script est lancé dans son propre processus Python afin que
les deux fenêtres graphiques puissent s'afficher en parallèle.
"""
import subprocess
import sys
import time
from pathlib import Path


def launch(script_name):
    path = Path(script_name)
    if not path.exists():
        print(f"Fichier '{script_name}' introuvable.")
        return None
    print(f"Lancement de {script_name}...")
    try:
        p = subprocess.Popen([sys.executable, script_name])
        print(f"Processus lancé (pid={p.pid})")
        return p
    except Exception as e:
        print(f"Erreur lors du lancement de {script_name}: {e}")
        return None


def main():
    # noms par défaut
    script1 = '3pts_evolution.py'
    script2 = 'pace_evolution.py'

    # possibilité de passer des noms via la ligne de commande :
    # python main.py other1.py other2.py
    if len(sys.argv) > 1:
        script1 = sys.argv[1]
    if len(sys.argv) > 2:
        script2 = sys.argv[2]

    t0 = time.time()
    p1 = launch(script1)
    p2 = launch(script2)

    # Si on a lancé des processes, on attend leur fin (les fenêtres matplotlib
    # resteront ouvertes tant que l'utilisateur ne les a pas fermées).
    if p1:
        p1.wait()
    if p2:
        p2.wait()

    dt = time.time() - t0
    print(f"Tous les scripts terminés — temps écoulé : {dt:.1f}s")


if __name__ == '__main__':
    main()
