# -*- coding: utf-8 -*-
"""TPNOTEOumouZoéAlexandra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jjX542hVQ6GGAi6YgE6WI-KTLN_8DgEW

# TP Analyse de survie
Auteurs:
        DEMBELE Oumou, MARTINEZ Zoé et MARTIN Alexandra

Nous avons realisé ce TP grâce aux diapositives sur l'analyse de survie et aux fonctionnalités de la librairie « lifelines » qui permettent de faire de l’analyse de survie.
"""

#installation de lifelines
!pip install lifelines

"""###importation des librairies"""

import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
import seaborn as sns

import numpy as np

"""###lecture du fichier

Lecture du fichier de données (leaders.xlsx). Pour des raisons pratiques, nous avons mit le fichier sous format excel.
"""

df = pd.read_excel("/content/leaders.xlsx")
df

"""###Calcul des statistiques descriptives sur la variable duration"""

print(df["duration"].describe())

"""Les statistiques descriptives sur la variable duration nous permettent notamment de nous rendre compte que les durées des régimes varient considérablement. En effet l'écart type d'environ 6.21 nous indique une grosse dispersion autour de la moyenne."""

# Distribution de la variable "duration" entre les démocratie et non-démocratie
plt.figure(figsize=(10, 6))
sns.boxplot(x='democracy', y='duration', data=df)
plt.title('Comparaison de la distribution de la durée entre les groupes de régime')
plt.xlabel('Type')
plt.ylabel('Durée')
plt.grid(True)
plt.show()

"""Grâce aux boites à moustaches, nous remarquons une nette différence entre les pays en démocratie et ceux qui ne le sont pas. Le type de politique à donc un impact sur la durée des régimes."""

# De façon plus précise, distribution de la variable "duration" entre les régimes
plt.figure(figsize=(10, 6))
sns.boxplot(x='regime', y='duration', data=df)
plt.title('Comparaison de la distribution de la durée entre les groupes de régime')
plt.xlabel('Type de régime')
plt.ylabel('Durée')
plt.grid(True)
plt.show()

"""L'analyse de la durée des événements révèle des variations significatives entre les différents types de régimes politiques. La monarchie a tendance à être la plus longue, suivis des dictatures civiles et militaires. Les démocraties parlementaires et présidentielles présentent des durées d'événements plus courtes, tandis que les démocraties sont nettement moins longues. Ces différences montrent des aspects différents de chaque politiques."""

# Distribution de la variable "duration" entre continent
plt.figure(figsize=(10, 6))
sns.boxplot(x='un_continent_name', y='duration', data=df)
plt.title('Comparaison de la distribution de la durée entre continent')
plt.xlabel('Continent')
plt.ylabel('Durée')
plt.grid(True)
plt.show()

"""Encore une fois grâce à nos boites à moustaches, nous visualisons les différences de durée de régimes entre continents. C'est l'Afrique qui à la plus grande durée de régime. Ce continent s'oppose à l'Europe qui à la plus faible.

###Affichage de l'histogramme de la durée (variable « duration ») pour l’ensemble de la population ou par type de régime.
"""

#pour l'ensemble de la population
plt.figure(figsize=(10, 6))
plt.hist(df["duration"], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Durée")
plt.ylabel("Fréquence")
plt.title("Histogramme de la durée de régime pour l'ensemble de la population")
plt.show()

#Par type de régime
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='duration', hue='regime', bins=20, kde=False)
plt.title('Histogramme de la durée de régime par type de régime')
plt.xlabel('Durée')
plt.ylabel('Fréquence')
plt.grid(True)
plt.legend(title='Type de régime')
plt.show()

"""Grâce aux histogrammes, nous prenons conscience que la durée de la majorité de régimes restent tout de même comprient entre 2 et 8 ans. seulement une très faible quantité va au dela.

###Estimation de la probabilité de survie et l’intervalle de confiance en utilisant la fonction Kaplan-Meyer. Affichage du tableau des proportions de survivants à l’instant t (t=0,…., n)
"""

#fonction

kmf = KaplanMeierFitter()
kmf.fit(df['duration'], event_observed=df['observed'])

#tableau

print(kmf.survival_function_)

"""Ci dessus nous avons le tableau des proportions de survivants à l'instant t, basé sur l'estimation de Kaplan-Meier, ce dernier offre un aperçu de la probabilité de survie des individus au cours du temps. Initialement, la probabilité de survie est de 100% à l'instant 0. Au fil du temps, on observe une diminution progressive de cette probabilité, illustrant la proportion de sujets qui continuent à survivre à chaque intervalle spécifié.

Vers le temps t=1, la probabilité de survie a diminué à environ 72%, indiquant une perte relativement importante de survivants au cours de cette première période. Cette tendance se poursuit au fil du temps, avec des proportions décroissantes à chaque intervalle successif. À t=10, la probabilité de survie a diminué à environ 18%, soulignant une diminution significative par rapport à la période initiale.

###Représentation graphique de la courbe de survie avec l’intervalle de confiance
"""

#graphique

plt.figure(figsize=(10, 6))
kmf.plot()
plt.title('Courbe de survie avec l’intervalle de confiance')
plt.xlabel('Durée')
plt.ylabel('Probabilité de survie')
plt.show()

"""Ce graphique met en avant ce que nous avons démontré juste avant. Au fil du temps la probabilité de survie devient de plus en plus faible. La courbe de survie descend rapidement ce qui indique une faible probabilité de survie.

###Représentation de la courbe de Kaplan-Meier pour chacun des deux groupes (dictateurs et démocrates).
"""

#représentation des deux groupes avec Kaplan-Meier


plt.figure(figsize=(10, 6))
for democracy in df['democracy'].unique():
    kmf.fit(df[df['democracy'] == democracy]['duration'], event_observed=df[df['democracy'] == democracy]['observed'], label=democracy)

    kmf.plot()
plt.title('Courbe de Kaplan-Meier pour chacun des deux groupes')
plt.xlabel('Durée')
plt.ylabel('Probabilité de survie')
plt.legend(title='democracy')
plt.show()

"""La coubre de Kaplan-Meier met en avant la différent de probabilité de survie entre les deux types de régimes. Les régimes en non démocraties semblent plus stables dans le temps (pente douce) et ont donc une probabilité de survie plus elevée. A contrario, les démocraties ont une faible durée dans le temps. La courbe descend rapidement.

##Partie facultatif

Pour exécuter un script avec Streamlit, sauvegardez-le sous le nom, par exemple, app.py, et exécutez-le avec la commande streamlit run app.py dans votre terminal. Cela lancera un serveur local et ouvrira automatiquement votre navigateur avec l'interface utilisateur générée par Streamlit.

Facilitons l'affichage sur page Web
"""

# les imports
import plotly.express as px
!pip install streamlit
import streamlit as st
import builtins
import plotly.graph_objects as go

@st.cache
def load_data():
    return pd.read_excel("/content/leaders.xlsx")

def hash_func(func):
    return None if func.__name__ == 'load_data' else func


@st.cache(hash_funcs={type(load_data): hash_func})
def load_data():
    return pd.read_excel("/content/leaders.xlsx")


data = load_data()


st.write(data)

# Création de l'objet
kmf = KaplanMeierFitter()
kmf.fit(data['duration'], event_observed=data['observed'])

# données de survie et intervalles de confiance
print(kmf.survival_function_)
print(kmf.confidence_interval_)

#une liste déroulante
regime_types = data['regime'].unique()
selected_regime = st.selectbox("Sélectionner le type de régime :", regime_types)

#filtre sur le régime
filtered_data = data[data['regime'] == selected_regime]

#Ploltly
fig = go.Figure()

# courbe de survie
fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.survival_function_.values.flatten(),
                         mode='lines',
                         name='Courbe de survie'))

fig.update_layout(title='Courbe de survie avec intervalle de confiance',
                  xaxis_title='Durée',
                  yaxis_title='Probabilité de survie')



# intervalle de confiance
fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.confidence_interval_['KM_estimate_upper_0.95'].values,
                         mode='lines',
                         line=dict(color='rgba(0,176,246,0.2)'),
                         name='Intervalle de confiance supérieur'))

fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.confidence_interval_['KM_estimate_lower_0.95'].values,
                         mode='lines',
                         fill='tonexty',
                         fillcolor='rgba(0,176,246,0.2)',
                         line=dict(color='rgba(0,176,246,0.2)'),
                         name='Intervalle de confiance inférieur'))

# Afficher
st.plotly_chart(fig)