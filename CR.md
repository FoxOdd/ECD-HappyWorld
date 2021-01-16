# 16 janvier 2021

- Le taux de Kendall
- [Rank-correlated set mining](http://adrem.uantwerpen.be/~goethals/software/) : [http://adrem.uantwerpen.be/bibrem/pubs/rankmining.pdf](http://adrem.uantwerpen.be/bibrem/pubs/rankmining.pdf)

On se concentre sur une année par exemple **2015** et essayer de remonter les années et concluant qu’il nous manque des données.

Pour tous les tableaux bien s’assurer d’avoir le code iso du pays et si besoin faire un dico de correspondance pour le code.

Vérifier les doublons

Définir un nombre de variables minimum pour garder le pays dans le jeu de données.

## Inventaire des données

- Hapiness : 2015 - 2019 (plusieurs variables)
- RSF : 2014 - 2020
- Espérance de vie : 2013 - 2016
- IDH de wikipédia : 2014 - 2019
- Taux de chômage : ? - 2019

### Code

http://dbpedia.org/snorql/ ; http://dbpedia.org/page/Human_Development_Index ; 

```SPARQL
PREFIX dbpedia2: <http://dbpedia.org/property/>
SELECT ?p ?h WHERE {
   ?p dbpedia2:hdi ?h .
   FILTER(?h < 1)
}
```

Attention il faut trier les pays par leur nom (label ?)

## Répartition des tâches

Stitch : lire l’article (MiningRank ≠ CorrelatedSetsofNumericalAttributes)

Odd : continuer la requête SPARQL

Mopa : ressourcer les données, script python

