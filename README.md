## NBA Evolution Statistic

Un petit projet Python pour analyser l'évolution de certaines statistiques NBA (trois points, rythme de jeu, etc.) au fil des saisons. Ce dépôt contient des scripts d'analyse et des visualisations simples pour explorer les tendances historiques.

### Contenu du dépôt
- main.py — point d'entrée principal (script d'orchestration / exemple d'utilisation).
- 3pts_evolution.py — script d'analyse et visualisation de l'évolution des tirs à 3 points.
- pace_evolution.py — script d'analyse et visualisation de l'évolution du "pace" (rythme de jeu).
- requirements.txt — dépendances Python nécessaires.
- README.md — (ce fichier) description et instructions.

### Description
Ce projet vise à fournir des outils légers pour examiner comment certaines statistiques collectives de la NBA (par ex. pourcentage et volume de tirs à 3 points, pace) ont évolué dans le temps. Les scripts lisent des jeux de données (CSV ou API), calculent des métriques par saison et produisent des graphiques ou des fichiers de sortie analytiques.

### Fonctionnalités
- Calculs saisonniers de métriques choisies (ex. nombre/moyenne de 3pts, pace).
- Visualisations simples (courbes temporelles).
- Scripts modulaires faciles à réutiliser pour d'autres métriques ou jeux de données.

### Prérequis
- Python 3.8+ recommandé.
- Virtualenv (optionnel mais recommandé).
- Les dépendances listées dans requirements.txt.

### Installation rapide
1. Cloner le dépôt (ou récupérer les fichiers).
2. Créer un environnement virtuel et installer les dépendances :
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Exemples d'utilisation
- Lancer le script principal (si main.py est configuré comme orchestrateur) :
```bash
python main.py
```
- Exécuter directement un script d'analyse :
```bash
python 3pts_evolution.py
python pace_evolution.py
```
Chaque script peut accepter des arguments (fichiers d'entrée, options de sortie). Consultez l'entête du script ou ajoutez `--help` si l'option est implémentée.

### Structure des fichiers et entrée attendue
Les scripts attendent généralement des données tabulaires (CSV) contenant des colonnes telles que : saison, équipe, possession, tentatives_de_3pts, réussite_de_3pts, etc. Si les jeux de données utilisés proviennent d'une API ou d'un format différent, adaptez la partie lecture dans le script (fonctions d'import).

Exemple minimal de colonnes acceptées :
- season: année ou identifiant de saison (ex. "2017-18")
- team / player: identifiant d'équipe ou de joueur
- possessions: nombre de possessions (pour calculer le pace)
- 3pt_att: tentatives à trois points
- 3pt_made: paniers marqués à trois points

### Données et sources
Ce projet n'inclut pas forcément les données brutes. Sources possibles :
- Base de données publique (ex. Basketball-Reference, stats.nba.com via API)
- Jeux de données CSV exportés manuellement
Précisez la source des données dans le README final si vous publiez le projet.

### Suggestions d'améliorations (next steps)
- Ajouter un script de téléchargement / pré-traitement des données.
- Documenter les arguments CLI de chaque script (`argparse`).
- Ajouter des tests unitaires pour les fonctions de transformation des données.
- Fournir des notebooks Jupyter pour l'exploration interactive.

### Contribution
Contributions bienvenues. Ouvrez une issue pour proposer une fonctionnalité ou un bug, puis envoyez une pull request avec une description claire des modifications.

### Licence
Indiquez ici la licence choisie (MIT, BSD, GPL, etc.). Si vous n'avez pas encore choisi, ajoutez un fichier `LICENSE` plus tard.

### Contact
Pour questions ou retours : ajoutez votre adresse e-mail ou lien GitHub.
