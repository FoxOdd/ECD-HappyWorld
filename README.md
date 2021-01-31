# ECD-HappyWorld
Exploration de données sur les données du bonheur dans le monde ainsi que des données complémentaires.

# Acquisition des données

Voici notre démarche pour l'acquisition et le formatage des données.
## Données du bonheur

Les tables du bonheur sont disponible en téléchargement sur https://www.kaggle.com/unsdsn/world-happiness .

Chaque table *2015.csv* , *2016.csv* , *2017.csv* , *2018.csv* , *2019.csv* est téléchargeable. 
Le téléchargement requiert une inscription.

Ranger les données dans un dossier **data/happy/.**

## Données sur la liberté de la presse

...

Ranger les données dans un dossier **data/RSF**

## Donnée du Rapport de développement humain

...

Ranger les données dans un dossier **data/Human_Development_Report/**

# Formatage des données

## Correspondance ISO noms pays 
Dans le dossier data, lancer la commande
```
cd data
cut -d, -f1,3,4 RSF/Index2015.csv > ISO3166.csv
```
## Trier les colonnes des fichiers du bonheur
Trier et supprimer manuellement les colones des fichiers **data/happy/201?** afin que les colonnes s'organisent de la façon suivante:
 - 1ère colonne Country ou Country or region
 - 2ème colonne Happiness Rank  ou Overall rank
 - 3ème colonne Happiness Score ou Score 
 - 4ème colonne Economy (GDP per Capita) ou GDP per capita
 - 5ème colonne Family ou Social support
 - 6ème colonne Health (Life Expectancy) ou Healthy life expectancy
 - 7ème colonne Freedom ou Freedom to make life choices 
 - 8ème colonne Trust (Government Corruption) ou Perceptions of corruption
 - 9ème colonne Generosity

## Imposer le séparateur décimal en point et non en virgule

Les fichiers du RSF ont leurs nombres écrits "à la française", avec une virgule et non un point comme séparateur.

Manuellement sur Excel pour tous les fichiers du RFS, imposer la langue en anglais puis sélectionner les colonnes *Score 201?* à mettre en format numeric number.

## Modifier les noms des fichiers du dossier Human_Development_Report

Les noms des fichiers contiènent des espaces et sont assez compliqué , un renommage des fichiers est donc a effectuer:
 - *Carbon dioxide emissions, per unit of GDP (kg per 2010 US$ of GDP).json* en *Carbon_dioxide_emissions.json*
 - *Education index.json* en *Education_index.json*
 - *Forest area (% of total land area).json* en *Forest_area.json* 
 - *HIV prevalence, adult (% ages 15-49).json* en *HIV_prevalence.json*
 - *Homicide rate (per 100,000 people).json* en *Homicide_rate.json* 
 - *Human Development Index (HDI).json* en *Homicide_rate.json*
 - *Internet users, total (% of population).json* en *Internet_users.json*
 - *Mean years of schooling (years).json* en *Mean_years_of_schooling.json*
 - *Mean years of schooling, female (years).json* en *Mean_years_of_schooling_female.json*
 - *Mean years of schooling, male (years).json* en *Mean_years_of_schooling_male.json*
 - *Mortality rate, infant (per 1,000 live births).json* en *Mortality_rate_infant.json*
 - *Unemployment, total (% of labour force).json* en *Unemployment.json*   
 - *Urban population (%).json* en *Urban_population.json* 

## Écritures de tableau récapitulatif des données

Les données sont mises en commun par année dans un fichier csv paramètre en fonction des pays. Ces fichiers récapitulatifs sont stockés dans **data/total** 

Pour les obtenir lancer une première fois la commande 
```
cd data
mkdir total
./script/formatage_data.py

```

Le script ne va pas renvoyer d'erreur cepandant il renvoie des années et des noms de pays.
Ce sont les pays du fichier *data/happy201?* de l'année considéré (ligne au dessus du nom du pays ) qui n'a pas pu être ajouter au car il n'y avait pas de correspondance ISO.

Pour rajouter ces pays il faut manuelement dans les fichiers *data/happy/201?* renomer le pays avec la bonne correspondance anglaise du fichier *data/ISO3166.csv* 

Relancer 
```
./script/formatage_data.py

```

# Calculer la corrélation entre le classement du bonheur et le classement des paramètres avec le tau de kendall

Ouvrir le script /script/kendalltau.R et à la ligne 6 indiquer le chemin absolu jusqu'aux data, enregistrer puis lancer le script 
```
./script/kendalltau.R
```

# Calcul de l'ACP et réalisation du clustering via les k-means
Ouvrir et lancer le Notebook Jupyter *Clustering.ipynb*.
