# Gestion des utilisateurs à partir de supabase

## Pré-requis et installations
1. Posséder un environnement de travail linux (une VM Ubuntu sur ton ordinateur, ou autre)
2. Installer les requirements du projet :
    * git
    * docker (<a href="https://www.docker.com/">docker.io</a> sous ubuntu)
    * docker-compose
    * un editeur de texte (visual studio code, Atom, sublime Text, ou autre)


## Structure
**docker** : pour démarrer un environnement supabase en local via docker/docker-compose selon la documentation docker
  * Variables d'environnement : les générer à partir du <a href="https://supabase.com/docs/guides/self-hosting#api-keys">générateur JWT (Json Web Token)</a>
  ```
  export API_URL="my-url-to-my-awesome-supabase-instance"
  export API_KEY="my-supa-anon-api-key"
  export SUPABASE_KEY="my-supa-service-role"
  ```
  * Dans le fichier `docker/.env` remplacer les valeurs de `ANON_KEY`, `SERVICE_ROLE_KEY` et `JWT_SECRET`
  * Dans le fichier `docker/volumes/api/kong.yml` remplacer les valeurs de `anon` et `service_role`
  * Lancer le docker.
  ```bash
  cd docker
  docker compose up
  ```
  Ouvrir depuis le navigateur de votre choix la page <a href="http://localhost:3000">http://localhost:3000</a>.

**utils/supabaseAdmin.py** : librairie contenant les fonctions admin suivantes :
   * Création d'un nouvel utilisateur et de son profil
   * Enrichissement d'un profil (prénom, nom, date de naissance, addresse, ville)
   * SUppression d'un utilisateur et de son profil
   * Detail d'un prolile d'utilisateur
   * Création des amis
   * Liste des amis de l'utilisateur connecté

**utils/supabaseClient.py** : librairie contenant la fonction user suivante :
   * Liste des profils des users amis de l'utilisateur connecté

**test** : contient les tests unitaires des différentes fonctions de la librairie
Pour lancer les tests :
```
make test
```
  * Creation de 5 utilisateurs et de leurs profils
  * Générer quelques relations d’amitié
  * Vérifier que le `SELECT *` retourne bien les amis seulement.


## Documentation
* https://supabase.com/docs/guides/self-hosting/docker
* https://supabase.com/docs/guides/auth/managing-user-data
* https://supabase.com/docs/reference/python/introduction
* https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts
* https://github.com/supabase-community/supabase-py
