from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats
import pandas as pd
import time
import json
import matplotlib.pyplot as plt
import numpy as np
import mplcursors


# On initialise avec les Celtics pour tester le code
all_teams = teams.get_teams()
celtics_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=1610612738)  
df = celtics_stats.get_data_frames()[0]


# Création du dictionnaire avec toutes les années
years = {}      
for index, row in df.iterrows():
    year_f = int(row['YEAR'].split('-')[0])
    year = year_f + 1
    if year not in years:
        years[year] = {}

# On remplit le dictionnaire avec les données de chaque équipe
for team in all_teams:
    team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team['id'])
    df = team_stats.get_data_frames()[0]
    for index, row in df.iterrows():
        year_s = int(row['YEAR'].split('-')[0])
        year = year_s + 1
        team_name = str(row['TEAM_NAME'])

        # lecture sécurisée des colonnes FG3A et nombre de matches (G / GP / GAMES_PLAYED)
        fg3a = pd.to_numeric(row.get('FG3A'), errors='coerce')
        games = None
        for col in ('G', 'GP', 'GAMES_PLAYED', 'GAMES'):
            val = row.get(col)
            if pd.notna(val):
                games = pd.to_numeric(val, errors='coerce')
                break

        # calcule FG3A par match si possible
        if pd.notna(fg3a) and games and games > 0:
            fg3a_per_game = fg3a / games
        else:
            fg3a_per_game = np.nan

        years[year][team_name] = fg3a_per_game
    time.sleep(1)

# Supprime les années sans données
for y in list(years.keys()):
    if years[y] == {}:
        print(f"Supprime année sans données: {y}")
        del years[y]    

# Calculer la moyenne FG3A par année (ignorer les valeurs NaN) et
moyenne_fg3a_per_year = {}
for y, teams_data in years.items():
    vals = [v for v in teams_data.values() if pd.notna(v)]
    if vals:
        moyenne_fg3a_per_year[y] = sum(vals) / len(vals)

# Années triées contenant des données (on filtre les années dont la moyenne vaut 0)
years_list = sorted([y for y, m in moyenne_fg3a_per_year.items() if m != 0 and not np.isnan(m)])
moyenne_values = [moyenne_fg3a_per_year[y] for y in years_list]


# Créer le graphique 1 : évolution de la moyenne des tentatives à 3 pts par année
plt.figure(figsize=(12, 6))
plt.plot(years_list, moyenne_values, marker='o')
plt.title('Évolution des tentatives à 3 points par match en NBA au fil des ans')
plt.xlabel('Année')
plt.ylabel('Moyenne des tentatives à 3 points par match')
plt.grid(True)
mplcursors.cursor()
plt.show()


















