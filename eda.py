import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_cleaned_data(filepath):
    """
    Charge les données nettoyées à partir d'un fichier CSV.
    Args:
        filepath (str): Chemin du fichier nettoyé.
    Returns:
        pd.DataFrame: Données nettoyées.
    """
    return pd.read_csv(filepath, parse_dates=["date"])


def plot_daily_sales(data):
    """
    Trace les ventes quotidiennes.
    Args:
        data (pd.DataFrame): Données avec colonnes "date" et "total_sales".
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["date"], data["total_sales"], label="Ventes quotidiennes")
    plt.title("Tendance des ventes quotidiennes")
    plt.xlabel("Date")
    plt.ylabel("Total des ventes")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_monthly_sales(data):
    """
    Trace les ventes agrégées par mois.
    Args:
        data (pd.DataFrame): Données avec colonnes "date" et "total_sales".
    """
    data["month"] = data["date"].dt.to_period("M")
    monthly_sales = data.groupby("month")["total_sales"].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(x="month", y="total_sales", data=monthly_sales)
    plt.title("Ventes totales par mois")
    plt.xlabel("Mois")
    plt.ylabel("Total des ventes")
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    # Chemin vers le fichier nettoyé
    file_path = "../data/processed/cleaned_sales_data.csv"

    # Charger les données
    cleaned_data = load_cleaned_data(file_path)

    # Tracer les ventes quotidiennes
    plot_daily_sales(cleaned_data)

    # Tracer les ventes mensuelles
    plot_monthly_sales(cleaned_data)
