import requests
from datetime import date
from pathlib import Path

URL = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/exports/csv"



def telecharger_csv() : 
    print ("telechargerment en cour...")
    reponse = requests.get(URL, timeout=120)
    reponse.raise_for_status()


    aujourdhui = date.today().isoformat()
    chemin = Path(f"data/raw/carburants_{aujourdhui}.csv")
    chemin.write_bytes(reponse.content)
    print("Fichier enregistrer : ", chemin)
    return chemin

# si on lance ce fichier directement, exécute telecharger_csv()
if  __name__ == "__main__" : 
    telecharger_csv()
