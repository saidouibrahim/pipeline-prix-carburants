import pandas as pd

df = pd.read_csv(
    "data/raw/carburants.csv",
    sep=";",
    dtype={"id": str, "cp": str, "code_departement": str, "code_region": str},
)

df["id"] = df["id"].str.zfill(8)

df["latitude"] = df["latitude"] / 100000
df["longitude"] = df["longitude"] / 100000

stations = df[[
    "id", "adresse", "ville", "cp", "departement",
    "code_departement", "region", "latitude", "longitude", "pop",
]]

stations = stations.rename(columns={"pop" : "type_route"})

print("Table stations :", stations.shape)
print(stations.head())


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

prix = prix.dropna(subset=["prix"])

print("Après suppression des cases vides :", prix.shape)
print(prix.head(10))