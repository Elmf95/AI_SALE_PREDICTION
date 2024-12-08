import pandas as pd


def clean_sales_data(data):
    """
    Nettoie et prépare les données de ventes pour l'analyse et les prévisions.
    Args:
        data (pd.DataFrame): Données brutes.
    Returns:
        pd.DataFrame: Données nettoyées.
    """
    # Supprimer les colonnes inutiles
    data = data.drop(
        columns=["Unnamed: 0", "Purchase Address", "Hour"], errors="ignore"
    )

    # Renommer les colonnes pour simplifier leur usage
    data.columns = data.columns.str.strip().str.replace(" ", "_").str.lower()

    # Vérifier les valeurs manquantes et les supprimer si nécessaire
    data = data.dropna(subset=["order_date", "quantity_ordered", "price_each"])

    # Convertir les colonnes en types appropriés
    data["quantity_ordered"] = pd.to_numeric(data["quantity_ordered"], errors="coerce")
    data["price_each"] = pd.to_numeric(data["price_each"], errors="coerce")
    data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")

    # Retirer les lignes avec des valeurs invalides
    data = data.dropna()

    # Calculer des colonnes supplémentaires
    data["year"] = data["order_date"].dt.year
    data["month"] = data["order_date"].dt.month

    # Agréger les ventes par jour
    daily_sales = data.groupby(data["order_date"].dt.date)["sales"].sum().reset_index()
    daily_sales.columns = ["date", "total_sales"]

    print(
        f"Données nettoyées : {daily_sales.shape[0]} lignes, {daily_sales.shape[1]} colonnes"
    )
    return daily_sales


if __name__ == "__main__":
    # Charger les données brutes
    file_path = "../data/raw/Sales Data.csv"
    data = pd.read_csv(file_path, parse_dates=["Order Date"])

    # Nettoyer les données
    cleaned_data = clean_sales_data(data)

    # Sauvegarder les données nettoyées
    cleaned_data.to_csv("../data/processed/cleaned_sales_data.csv", index=False)
    print("Données nettoyées sauvegardées.")
