import os
import pandas as pd


def find_file_in_directory(directory, filename):
    """
    Recherche un fichier spécifique dans un répertoire donné.
    Args:
        directory (str): Chemin du répertoire à explorer.
        filename (str): Nom du fichier à rechercher.
    Returns:
        str: Chemin complet vers le fichier s'il est trouvé, sinon None.
    """
    for root, _, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


def load_sales_data(directory, filename="Sales Data.csv"):
    """
    Charge un dataset de ventes à partir d'un fichier CSV situé dynamiquement.
    Args:
        directory (str): Répertoire où chercher le fichier.
        filename (str): Nom du fichier à charger.
    Returns:
        pd.DataFrame: Données sous forme de DataFrame.
    """
    filepath = find_file_in_directory(directory, filename)
    if filepath:
        data = pd.read_csv(filepath, parse_dates=["Order Date"])
        print(f"Données chargées depuis : {filepath}")
        print(
            f"Nombre de lignes : {len(data)}, Nombre de colonnes : {len(data.columns)}"
        )
        return data
    else:
        raise FileNotFoundError(
            f"Le fichier '{filename}' n'a pas été trouvé dans le répertoire '{directory}'."
        )


if __name__ == "__main__":
    # Exemple d'utilisation
    directory = "../data/raw/"
    sales_data = load_sales_data(directory)
    print(sales_data.head())
