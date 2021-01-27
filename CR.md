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
- ~~IDH de wikipédia : 2014 - 2019~~ IDH de undp : via API : 2010-2019
- Taux de chômage : ? - 2019

### Code

http://dbpedia.org/snorql/ ; http://dbpedia.org/page/Human_Development_Index ; 

```SPARQL
PREFIX dbo: <http://dbpedia.org/ontology/> 
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?p_name ?country ?idh ?year
WHERE {
 ?p dbpedia2:hdi ?idh .
 ?p dbpedia2:commonName ?country .
 ?p foaf:name ?p_name .
 ?p dbpedia2:hdiYear ?year .
 FILTER(langMatches(lang(?p_name), "en"))
 FILTER( ?idh < 1 )
}
ORDER BY ?idh
```

http://hdr.undp.org/en/content/human-development-report-office-statistical-data-api

## Répartition des tâches

Stitch : lire l’article (MiningRank ≠ CorrelatedSetsofNumericalAttributes)

Odd : continuer la requête SPARQL [x]

Mopa : ressourcer les données, script python

# 24 janvier

Récupération des données depuis le site undp.org

## Récupération du cookie de connexion

Sur la page de login http://ec2-54-174-131-205.compute-1.amazonaws.com/API/Login.php il s’agit d’un formulaire avec post :

- action => `/API/Login.php`

- user/login => `EmailLogin` == `odd.heurtel@mail.fr`
- mdp => `Password` == `MKZbzHNE9sQqgic`

commande wget : `wget --save-cookies cookie.txt --keep-session-cookies --post-data 'EmailLogin=odd.heurtel@mail.fr&Password=MKZbzHNE9sQqgic' --delete-after http://ec2-54-174-131-205.compute-1.amazonaws.com/API/Login.php`.

**Résultat échec**

## Tentative avec curl

Valeur du cookie = `q79r1h6hif37jrpjubp6npsbg4`

````
curl "http://ec2-54-174-131-205.compute-1.amazonaws.com/API/HDRO_API.php" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Prefer: safe" -H "Referer: http://ec2-54-174-131-205.compute-1.amazonaws.com/API/Information.php" -H "DNT: 1" -H "Connection: keep-alive" -H "Cookie: PHPSESSID=q79r1h6hif37jrpjubp6npsbg4" -H "Upgrade-Insecure-Requests: 1" -H "Cache-Control: max-age=0"
````

Sauvegarde dans un fichier texte, json.

**Résultat échec**

## Plusieurs curl

Création d’un premier script pour récupérer les données et exécution de la commande.

**Résultat OK**

# 27 janvier

