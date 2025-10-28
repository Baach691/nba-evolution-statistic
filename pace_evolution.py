from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.endpoints import boxscoreadvancedv3
from nba_api.stats.endpoints import teamestimatedmetrics
import pandas as pd
import time
import json
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# On initialise avec les Celtics car équipe la plus ancienne donc il ne manque pas de saison
all_teams = teams.get_teams()
celtics_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=1610612738)
dfc = celtics_stats.get_data_frames()[0]
seasons = []

# Crée une liste de toutes les saisons disponibles à partir des données des Celtics
for index, row in dfc.iterrows():
    season = row['YEAR']
    if season not in seasons:
        seasons.append(season)

# Crée le dictionnaire avec les données de Pace pour chaque équipe et chaque année
years = {}
for season in seasons:
    tem = teamestimatedmetrics.TeamEstimatedMetrics(season=season)
    df = tem.get_data_frames()[0]
    season_year = int(season.split('-')[0]) + 1
    years[season_year] = {}
    for index, row in df.iterrows():
        team_name = str(row['TEAM_NAME'])
        pace = float(row['E_PACE'])
        years[season_year][team_name] = pace
    time.sleep(1)
    if years[season_year] == {}:
        # supprime les années vides pour éviter les erreurs plus tard
        del years[season_year]

# Crée une liste des années triées et calcule la moyenne du Pace pour chaque année
years_list = sorted(years.keys())
total_pace_per_year = []
for year in years_list:
    total_pace = sum(pace for pace in years[year].values() if pace is not None)
    moyenne_pace = total_pace / len(years[year])
    total_pace_per_year.append(moyenne_pace)

# Crée le graphique avec matplotlib
plt.figure(figsize=(12, 6))
plt.plot(years_list, total_pace_per_year, marker='o')
plt.title("Évolution du rythme de jeu (Pace) en NBA au fil des ans")
plt.xlabel('Année')
plt.ylabel('Moyenne du rythme de jeu (Pace)')
plt.grid(True)
# Ajoute un curseur interactif pour afficher les valeurs des points
mplcursors.cursor()
plt.show()


