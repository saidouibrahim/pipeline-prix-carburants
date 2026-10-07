# ⛽ Pipeline des prix des carburants en France

Projet personnel de **data engineering** : un pipeline ETL qui récupère les prix
des carburants publiés en open data par l'État, les nettoie et les stocke dans
une base de données pour les analyser.

## 🎯 Objectif

Construire un pipeline de données complet, de la source brute jusqu'à une base
de données exploitable, afin de répondre à des questions comme :

- Où trouver le carburant le moins cher dans un département ?
- Comment les prix évoluent-ils dans le temps ?
- Quel carburant est le plus disponible en France ?

## 📊 Source des données

[Prix des carburants en France – Flux instantané](https://data.economie.gouv.fr/explore/dataset/prix-des-carburants-en-france-flux-instantane-v2/)
(data.economie.gouv.fr) : environ 10 000 stations-service, mises à jour en continu.

## 🏗️ Architecture du pipeline

1. **Extract** (`src/extract.py`) : téléchargement automatique du CSV, enregistré avec la date du jour
2. **Transform** (`src/transform.py`) : nettoyage des données avec pandas
3. **Load** : chargement dans une base SQLite *(en cours)*

## 🧹 Nettoyage des données

- Identifiants et codes postaux conservés en texte, avec restauration des zéros perdus
- Coordonnées GPS corrigées (valeurs stockées × 100 000 dans la source)
- Prix passés d'un format « large » (une colonne par carburant) à un format « long » (une ligne par carburant)

## 🗄️ Modèle de données

Deux tables normalisées (voir `sql/schema.sql`) :

- **stations** : une ligne par station (adresse, ville, département, coordonnées…)
- **prix** : une ligne par station, carburant et date, reliée à `stations` par une clé étrangère

## 🛠️ Technologies

Python · pandas · requests · SQL · SQLite · Git

## 📦 Librairies principales

- **pandas** : manipulation et nettoyage des données
- **requests** : téléchargement des données depuis l'API

## 🚀 Lancer le projet

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sqlite3 data/carburants.db < sql/schema.sql
python src/extract.py
python src/transform.py
pip install pandas
```

## 📌 Statut

🚧 En cours de construction

- [x] Extraction des données
- [x] Modélisation de la base
- [ ] Transformation (en cours)
- [ ] Chargement en base
- [ ] Analyses SQL
- [ ] Automatisation quotidienne