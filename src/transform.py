import pandas as pd


#lire le fichier CSV et garde les codes en text pour ne pas perdre les zero
df = pd.read_csv(
    "data/raw/carburants.csv",
    sep=";",
    dtype={"id": str, "cp": str, "code_departement": str, "code_region": str},
)


#rajouter zero devant jusqu'a ce quil atteint le 8 chiffres qui sont attendu
df["id"] = df["id"].str.zfill(8)


#je divise par 100000 par ce que c est impossible d avoir une latitude et un longitude pareil sur cette terre
df["latitude"] = df["latitude"] / 100000
df["longitude"] = df["longitude"] / 100000


# garder seulement les 10 colonnes utiles pour la table stations
stations = df[[
    "id", "adresse", "ville", "cp", "departement",
    "code_departement", "region", "latitude", "longitude", "pop",
]]

#ici c est pour modifier le nom d une colonne par une autre
stations = stations.rename(columns={"pop" : "type_route"})

print("Table stations :", stations.shape)
print(stations.head())

# passer d'une colonne par carburant à une ligne par carburant (format long)
colonnes_prix = [
    "gazole_prix", "sp95_prix", "sp98_prix",
    "e10_prix", "e85_prix", "gplc_prix",
]

prix = df[["id"] + colonnes_prix ].melt(
    id_vars=["id"],
    var_name="carburant",
    value_name="prix",
)  

print("Avant suppression des cases vides :", prix.shape)

# supprimer les lignes sans prix (carburants que la station ne vend pas)
prix = prix.dropna(subset=["prix"])

print("Après suppression des cases vides :", prix.shape)
print(prix.head(10))

# traduire les anciens noms de colonnes en noms de carburants lisibles
noms_carburants = {
    "gazole_prix": "Gazole",
    "sp95_prix": "SP95",
    "sp98_prix": "SP98",
    "e10_prix": "E10",
    "e85_prix": "E85",
    "gplc_prix": "GPLc",
}

prix["carburant"] = prix ["carburant"].map(noms_carburants)

# renomer "id" en "station_id" pour correspondre a la table SQL
prix  = prix.rename(columns={"id" : "station_id"})

print(prix.head(10))
print(prix["carburant"].value_counts())

# même travail pour les dates de mise à jour : une ligne par carburant
colonnes_maj = [
    "gazole_maj", "sp95_maj", "sp98_maj",
    "e10_maj", "e85_maj", "gplc_maj",
]

dates = df[["id"] + colonnes_maj ].melt(
    id_vars=["id"],
    var_name="carburant",
    value_name="date-maj",
)

# traduire les noms de colonnes de dates en noms de carburants
noms_dates = {
    "gazole_maj": "Gazole",
    "sp95_maj": "SP95",
    "sp98_maj": "SP98",
    "e10_maj": "E10",
    "e85_maj": "E85",
    "gplc_maj": "GPLc",
}
dates["carburant"] = dates["carburant"].map(noms_dates)
dates = dates.rename(columns={"id": "station_id"})

# relier chaque prix à sa date (même station + même carburant)
prix = prix.merge(dates, on=["station_id", "carburant"], how= "left")

print("table prix final :" , prix.shape)
print(prix.head(10))

