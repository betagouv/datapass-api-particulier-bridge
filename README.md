# 🌉 Data Pass <> API Particulier Bridge

Application de bridge appelée par Data Pass lorsqu'une demande concernant API Particulier est validée.

Le bridge effectue alors les actions suivantes :

- Authentification de l'appel Data Pass,
- Création de l'application Gravitee :
  - Génération d'une nouvelle API Key
  - Définition du `client_id` de l'application par calcul du `sha512` de l'API Key
- Création de la souscription de l'application Gravitee aux APIs Gravitee qui concernent API Particulier :
  - API DGFIP
  - API CNAF
  - API Introspect
- Création d'un compte technique pour le contact technique renseigné dans la demande
- Mise à jour du dictionnaire Gravitee des noms d'applications `application-names`
- Mise à jour du dictionnaire Gravitee des scopes des applications `api-particulier-scopes`
- Envoi d'un message sur le portail, au contact technique, pour lui donner la clé d'API

# Installation

- `cp .env.dist .env`
- `pipenv install`

# Développement local

- `pipenv run flask run`

# Tests

- `pipenv run test`

# Déploiement

Le bridge est déployé sur l'instance [Dokku](https://github.com/dokku/dokku) d'Etalab.
