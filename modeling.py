import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


def prepare_data(filepath):
    """
    Prépare les données pour Prophet.
    Args:
        filepath (str): Chemin du fichier nettoyé.
    Returns:
        pd.DataFrame: Données formatées pour Prophet.
    """
    data = pd.read_csv(filepath, parse_dates=["date"])
    data = data.rename(columns={"date": "ds", "total_sales": "y"})
    return data


def train_prophet_model(data):
    """
    Entraîne un modèle Prophet.
    Args:
        data (pd.DataFrame): Données avec colonnes "ds" (dates) et "y" (valeurs).
    Returns:
        Prophet: Modèle entraîné.
    """
    model = Prophet()
    model.fit(data)
    return model


def make_forecast(model, periods=30):
    """
    Génère des prévisions avec Prophet.
    Args:
        model (Prophet): Modèle Prophet entraîné.
        periods (int): Nombre de jours à prédire.
    Returns:
        pd.DataFrame: Prévisions générées.
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


def plot_forecast(model, forecast):
    """
    Trace les prévisions générées par Prophet.
    Args:
        model (Prophet): Modèle Prophet.
        forecast (pd.DataFrame): Prévisions générées.
    """
    model.plot(forecast)
    plt.title("Prévisions des ventes")
    plt.xlabel("Date")
    plt.ylabel("Ventes")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Chemin vers les données nettoyées
    file_path = "../data/processed/cleaned_sales_data.csv"

    # Préparation des données
    data = prepare_data(file_path)

    # Entraînement du modèle
    model = train_prophet_model(data)

    # Génération de prévisions (30 jours par défaut)
    forecast = make_forecast(model, periods=30)

    # Afficher les prévisions
    plot_forecast(model, forecast)
