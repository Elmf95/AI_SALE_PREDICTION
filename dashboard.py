import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.express as px


# Charger les données nettoyées
@st.cache_data
def load_data(filepath):
    """
    Charge les données nettoyées.
    """
    data = pd.read_csv(filepath, parse_dates=["date"])
    return data


# Générer des prévisions
@st.cache_data
def generate_forecast(data, periods):
    """
    Génère des prévisions en utilisant Prophet.
    Args:
        data (pd.DataFrame): Données historiques (colonnes 'ds', 'y').
        periods (int): Nombre de jours de prévision.
    Returns:
        Prophet, pd.DataFrame: Modèle Prophet et ses prévisions.
    """
    prophet_data = data.rename(columns={"date": "ds", "total_sales": "y"})
    model = Prophet()
    model.fit(prophet_data)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return model, forecast


# Charger les données
data_file = "../data/processed/cleaned_sales_data.csv"
data = load_data(data_file)

# Configuration du tableau de bord
st.title("Tableau de bord : Prévisions des ventes")
st.sidebar.header("Paramètres")

# Affichage des données historiques
st.subheader("Données historiques des ventes")
st.write(f"Nombre total de jours : {data.shape[0]}")
st.dataframe(data)

# Visualisation des ventes quotidiennes
st.subheader("Graphique des ventes quotidiennes")
fig = px.line(data, x="date", y="total_sales", title="Ventes quotidiennes")
st.plotly_chart(fig)

# Prévisions
st.subheader("Prévisions avec Prophet")
horizon = st.sidebar.slider(
    "Choisir l'horizon de prévision (en jours)",
    min_value=7,
    max_value=365,
    value=30,
    step=7,
)

# Générer les prévisions dynamiquement
model, forecast = generate_forecast(data, horizon)

# Afficher les prévisions
st.write(f"Prévisions pour les {horizon} prochains jours")
forecast_fig = plot_plotly(model, forecast)
st.plotly_chart(forecast_fig)

# Comparaison des ventes réelles et prévues
st.subheader("Comparaison des ventes réelles et prévues")
merged_data = pd.merge(
    data, forecast[["ds", "yhat"]], left_on="date", right_on="ds", how="left"
)
st.dataframe(merged_data[["date", "total_sales", "yhat"]].tail(10))
