# AI Sales Prediction Dashboard

## Description
Ce projet utilise **Prophet** pour générer des prévisions de ventes et **Streamlit** pour créer un tableau de bord interactif. L'objectif est de permettre à l'utilisateur de visualiser les ventes historiques et de prévoir les ventes futures en fonction de différentes périodes.

## Fonctionnalités
- Nettoyage des données de vente
- Agrégation et transformation des données
- Prévisions dynamiques avec **Prophet**
- Interface interactive avec **Streamlit**
- Choix de l'horizon des prévisions via un slider (de 7 à 365 jours)

## Technologies
- **Python** : Langage de programmation principal
- **Streamlit** : Framework pour le développement de l'interface utilisateur
- **Prophet** : Outil de prévision de séries temporelles développé par Facebook
- **Pandas** : Manipulation des données
- **Plotly** : Visualisation interactive

## Structure du projet
Voici la structure du projet :


## Installation
1. **Clonez le dépôt GitHub** :
    ```bash
    git clone https://github.com/votre-utilisateur/AI_SALE_PREDICTION.git
    cd AI_SALE_PREDICTION
    ```
2. **Créez un environnement virtuel** :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows : env\Scripts\activate
    ```
3. **Installez les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Préparation des données
1. **Téléchargez les données** : Placez vos données brutes de ventes dans le dossier `data/raw/`.  
   Les données doivent être sous forme de fichier CSV avec des colonnes telles que `Order ID`, `Product`, `Quantity Ordered`, `Price Each`, et `Sales`.
2. **Nettoyez et préparez les données** :
    ```bash
    python src/preprocess.py
    ```
    Les résultats seront stockés dans `data/processed/cleaned_sales_data.csv`.

### Génération des prévisions avec Prophet
Le script `modeling.py` utilise les données nettoyées pour entraîner un modèle **Prophet**. Ce modèle génère ensuite des prévisions sur une période définie.

### Lancer l'application Streamlit
1. Lancez l'application Streamlit :
    ```bash
    streamlit run src/dashboard.py
    ```
2. Utilisez l'interface pour :
    - Visualiser les ventes historiques.
    - Ajuster l'horizon des prévisions (7 à 365 jours) à l'aide du slider.
    - Consulter les prévisions générées.

## Machine Learning (ML) dans le projet

### Utilisation de **Prophet**
Le modèle **Prophet** est utilisé pour prévoir les ventes futures sur la base des données historiques.  
**Étapes clés** :
1. Les données sont préparées et nettoyées dans `preprocess.py`.
2. Dans `dashboard.py`, un modèle **Prophet** est entraîné sur ces données.
3. Le modèle génère des prévisions sur une période spécifiée via l'interface Streamlit.

## Déploiement

### Déploiement via **Streamlit Cloud**
1. **Préparez le dépôt pour le déploiement** :
    - Assurez-vous que votre dépôt GitHub contient tous les fichiers nécessaires (`requirements.txt`, `src/dashboard.py`, etc.).
2. **Déployez sur Streamlit Cloud** :
   
3. **Partagez l'application** : Une URL sera générée pour permettre à d'autres utilisateurs d'accéder à votre tableau de bord.

## Exemple d'utilisation
1. Téléchargez vos données de ventes dans `data/raw/`.
2. Nettoyez et préparez les données avec :
    ```bash
    python src/preprocess.py
    ```
3. Lancez l'application avec :
    ```bash
    streamlit run src/dashboard.py
    ```
4. Ajustez l'horizon de prévision dans l'interface Streamlit.

## Auteur
**Fikri El mehdi**  


## Licence
Ce projet est sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.
