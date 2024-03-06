Bienvenue à toi jeune étranger

##Pour créer la première séquence plusieurs actions sont à mener:

wsk action create randompy random.py
wsk action create double double.js
wsk action create display display.php

##Pour créer la première séquence tu devra lancer la commande suivante :

wsk action create sequencedouble --sequence randompy,double,display 

##Afin de pouvoir exécuter la première séquence taper la commande suivante tu devras

wsk action invoke sequencedouble  --result

##Pour ta deuxième quête qui est la création de la séquence exposée qur le web tu devras mener ces actions à bien :

wsk action create webrandom webrandom.js
wsk action create webdouble webdouble.php
wsk action create webdisplay webdisplay.py

Pour créer la séquence exposée sur les internet tu devra taper la commande suivante :

wsk action create websequence --sequence webrandom,webdouble,webdisplay 

##Concernant la seconde séquance qui elle est exposée sur le web tu devras lancer la commande ci-dessous

curl https://ow.services.eemi.tech/api/v1/web/guillem.borzi%40eemi.com/default/websequence

##Si d'aventure ta curiosité t'emmène à regarder le résultat l'adresse suivante dans la barre de recherche tu devra rentrer :

https://ow.services.eemi.tech/api/v1/web/guillem.borzi%40eemi.com/default/websequence

##Bonne route à toi 
