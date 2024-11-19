# Manga2i



site de vente de manga

## Table des matières

1. [À propos](#à-propos)
2. [Fonctionnalités](#fonctionnalités)
3. [Prérequis](#prérequis)
4. [Installation](#installation)

---

## À propos

projet fil rouge dans le cadre d'une formation pour devenir devOps, le but est de créer un site de ecommerce et d'y integrer un maximum de compétences acquise lors de la formation afin de proposer le plus de fonctionnalité possible.

## Fonctionnalités

1. Gestion du Catalogue de Mangas
- Fiche produit détaillée : Inclut la couverture, le résumé, le genre, l’auteur, et le prix. :hourglass_flowing_sand:
- Filtres et recherche avancée : Recherche par titre, auteur, genre, avec des options de tri (popularité, prix, nouveautés). :hourglass_flowing_sand:
- Suggestions de mangas similaires : Recommandations basées sur le genre ou l’auteur pour encourager la découverte. :hourglass_flowing_sand:

2. Compte Utilisateur et Historique d'Achat
- Inscription et connexion : Création de comptes. :white_check_mark:
- Sauvegarder le panier, les commandes, et les favoris. :hourglass_flowing_sand:
- Historique des commandes : Visualisation des commandes passées et suivi de chaque achat. :hourglass_flowing_sand:
- Liste de souhaits : Possibilité de sauvegarder des mangas pour les acheter plus tard. :hourglass_flowing_sand:

3. Système de Panier et de Paiement
- Panier dynamique : Affichage en temps réel des articles, des quantités, et du total. :hourglass_flowing_sand:
- Options de paiement sécurisé : Support des cartes bancaires et des services de paiement en ligne (ex. PayPal). :hourglass_flowing_sand:
- Confirmation et suivi de commande : Confirmation instantanée et email avec suivi de livraison. :hourglass_flowing_sand:

4. Avis et Notations des Mangas
- Commentaires et notes par les utilisateurs : Chaque utilisateur peut donner son avis et noter un manga. :hourglass_flowing_sand:
- Système d’évaluation par étoiles : Note moyenne affichée sur la fiche produit. :hourglass_flowing_sand:
- Modération des avis : Option de validation des avis pour assurer la qualité des commentaires. :hourglass_flowing_sand:

5. Promotions et Fidélisation
- Codes de réduction et offres spéciales : Système de coupons pour des promotions sur certains mangas. :hourglass_flowing_sand:
- Programme de fidélité : Points gagnés à chaque achat, échangeables contre des réductions. :hourglass_flowing_sand:
- Notifications de promotions : Alertes pour les offres et nouvelles sorties basées sur les préférences utilisateur. :hourglass_flowing_sand:

## Prérequis

Spécifie les dépendances nécessaires avant l'installation :

- **Python 3.10.5**
- **Django 5.0.1**
- **virtualenv 20.27.1**

## Installation

Explique comment installer le projet en local :

1. Clonez le dépôt :

   ```bash
   git clone git@github.com:yheguy/Manga2i.git
   cd Manga2i/manga2i
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Créez un environnement virtuel et activez-le :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Créez la base de données :

   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur :

   ```bash
   python manage.py createsuperuser
   ```

6. Lancer le serveur de développement :

   ```bash
   python manage.py runserver
   ```
