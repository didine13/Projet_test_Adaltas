# Gestion des utilisateurs à partir de supabase

## Pré-requis et installations
1. Posséder un environnement de travail linux (une VM Ubuntu sur ton ordinateur, ou autre)
2. Installer les requirements du projet : git, docker (docker.io sous ubuntu), docker-compose, un editeur de texte (visual studio code, Atom, sublime Text, ou autre)
3. Démarrer un environnement supabase via docker/docker-compose selon la documentation docker


## Structure
* project/lib.py : librairie contenant les fonctions suivantes :
 * Création d'un nouvel utilisateur et de son profil
 * Création des amis
 * Liste des profils des users amis de l'utilisateur connecté

test : contient les tests unitaires des différentes fonctions de la librairie
* Creation de 5 utilisateurs et de leurs profils
* Générer quelques relations d’amitié
* Vérifier que le SELECT * retourne bien les amis seulement.


## Documentation
* https://supabase.com/docs/guides/self-hosting/docker
* https://supabase.com/docs/guides/auth/managing-user-data
* https://supabase.com/docs/reference/python/introduction
* https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts
