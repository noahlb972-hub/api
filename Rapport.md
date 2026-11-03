1. Description du projet
.Objectif
Le projet consiste à développer la partie back-end d'une application en ligne permettant de gérer une liste d'étudiants. Le back-end est une API REST écrite en Python avec le micro-framework Flask.
Elle expose des routes HTTP, interroge une base de données MySQL (base ciel2027, table etudiant) grâce à la bibliothèque mysql.connector, et renvoie les résultats au format JSON.

Diagramme de cas d'utilisation
Utilisateur identifié
Consulter tous les étudiants ; consulter un étudiant ; ajouter un étudiant ; modifier un étudiant ; supprimer un étudiant

Utilisateur non identifié
S'authentifier (POST /login/)

Administrateur
Créer l'utilisateur extern_user et gérer ses privilèges ; sauvegarder la base

<img width="4064" height="3470" alt="image" src="https://github.com/user-attachments/assets/22f08d93-29b5-4455-a82b-141a9ecce809" />
diagramme fait a partir de mermaid

 Description de l'API
 Récupérer tous les étudiants
 Méthode / route : GET /v1/etudiants/Fonction : getEtudiants()
 Paramètres : aucun
 Réponses : 200 tableau JSON des étudiants ; 400 requête invalide ; 401 accès non autorisé ; 500 échec de connexion à la base.
 
Récupérer un étudiant
Méthode / route : GET /v1/etudiants/{id}
Fonction : getEtudiant(id)
Paramètres : id (entier, dans la route)
Réponses : 200 détails de l'étudiant ; 400 requête invalide ; 401 accès non autorisé ; 404 id invalide ; 500 échec de connexion.

Ajouter un étudiant
 Méthode / route : POST /v1/etudiants/
 Fonction : addEtudiant()
Corps (JSON) : { "nom": "...", "prenom": "...", "email": "...", "telephone": "..." }
 Réponses : 201 ajout OK ; 401 accès non autorisé ; 500 échec de connexion.
 
Modifier un étudiant
Méthode / route : PUT /v1/etudiants/{id}
 Fonction : updateEtudiant(id)
 Paramètres : id dans la route ; détails de l'étudiant en JSON dans le corps
 Réponses : 200 modification OK ; 401 accès non autorisé ; 404 id invalide ; 500 échec de connexion.
 
 Supprimer un étudiant
 Méthode / route : DELETE /v1/etudiants/{id}
 Fonction : deleteEtudiant(id)
 Paramètres : id dans la route
 Réponses : 200 suppression OK ; 401 accès non autorisé ; 404 id invalide ; 500 échec de connexion.
 
 S'authentifier (version 3)
 Méthode / route : POST /login/
 Fonction : login()
 Corps (JSON) : { "username": "...", "password": "..." }
 Principe : l'API recherche le mot de passe de l'utilisateur dans la table user et compare le résultat à celui reçu.
 Réponses : 200 authentification réussie ; 401 identifiants incorrects ; 500 échec de connexion à la base.

Récapitulatif des 3 versions de l'API
 v1
api_v1.py
Tous les cas d'utilisation du CRUD ; versioning dans les routes (/v1/...) ; codes HTTP et messages de retour appropriés ; requêtes SQL construites avec des f-strings

v2
api_v2.py
Gestion des erreurs avec try / except (ex. : id inexistant renvoyant 404 et {"erreur": "id invalide"} au lieu d'une TypeError non gérée) ; gestion des privilèges avec l'utilisateur extern_user (SELECT, INSERT, UPDATE, DELETE) ; test depuis un autre poste du réseau local ; début des sauvegardes avec GitHub

v3
api_v3.py + db.py
Table user ; route POST /login/ ; authentification par username / password ; programmation modulaire et orientée objet : toutes les fonctions de requêtage sont déplacées dans la classe Database
diagramme de classe 
<img width="1104" height="1700" alt="image" src="https://github.com/user-attachments/assets/89e66122-50f8-4c93-8901-ead41ecb8701" />

Fiche des tests de l'API 
celui qui ma teste c'est Mathys et j'ai teste sur Mathys aussi

