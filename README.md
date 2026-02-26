# CommunicationProtocol

Ce projet propose une implémentation simple et extensible d’un protocole de communication entre un client et un serveur en Python. Il sert de base pour développer des systèmes réseau, des applications distribuées ou des modules d’échange de données.

Objectifs du projet

Fournir un client et un serveur minimalistes mais fiables.

Mettre en place une logique d’envoi/réception de messages.

Créer un protocole simple pouvant évoluer vers des fonctionnalités avancées (authentification, chiffrage, multiplexage, sérialisation, etc.).

## Architecture du dépôt
.
├── client.py     # Client TCP permettant d’envoyer des messages au serveur  
└── server.py     # Serveur TCP capable de recevoir et traiter des messages
## Fonctionnement général

Le serveur ouvre un socket et reste en attente de connexions entrantes.
Le client établit une connexion au serveur, envoie un message et attend une réponse éventuelle.

Les scripts utilisent le module Python socket et respectent une structure claire pour faciliter la maintenance et l’extension.

## Prérequis

Python 3.8 ou supérieur

Aucun package externe n’est requis

## Installation

Clonez le dépôt :
```bash
git clone https://github.com/<username>/CommunicationProtocol.git
cd CommunicationProtocol
```
## Utilisation
Lancer le serveur
```bash
python3 server.py
```
Lancer le client
Dans un autre terminal :

```bash
python3 client.py
```

Modifiez les paramètres (hôte, port, buffer size) directement dans les fichiers selon vos besoins.

## Améliorations possibles

- Ajout d’un protocole structuré (JSON, Protobuf, etc.)

- Mise en place d’un chiffrement TLS

- Gestion multi-clients

- Ajout de logs détaillés

- Tests automatisés

## Auteur

Projet créé et maintenu par Ashley-Adonya.
