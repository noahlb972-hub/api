Conclusion et améliorations possibles en cybersécurité
Ce projet a permis de construire progressivement une API REST fonctionnelle : implémentation du CRUD (v1), fiabilisation par la gestion des erreurs et des privilèges (v2), puis authentification et architecture orientée objet (v3). L'API reste cependant un prototype pédagogique ; plusieurs améliorations sont indispensables avant une mise en production.
6.1 Injections SQL
Les requêtes construites avec des f-strings (WHERE idetudiant = {id}) sont vulnérables si la valeur n'est pas maîtrisée. Il faut utiliser des requêtes paramétrées :
cursor.execute("SELECT * FROM etudiant WHERE idetudiant = %s", (id,))
On peut aussi valider le type et le format de toutes les entrées reçues dans le corps JSON.
6.2 Injections XSS
Les champs saisis (nom, prénom, e-mail) peuvent contenir du code HTML ou JavaScript renvoyé tel quel au front-end. Il faut valider et assainir les entrées côté API, échapper les données à l'affichage côté client et envoyer des en-têtes de sécurité (Content-Type: application/json, Content-Security-Policy).
6.3 Authentification et mots de passe
• Ne jamais stocker les mots de passe en clair : utiliser un hachage salé (bcrypt, argon2).
• Remplacer les identifiants de test simples par des mots de passe robustes.
• Utiliser des jetons (JWT) avec expiration pour sécuriser chaque requête, au lieu de ne vérifier que la route /login/.
• Limiter les tentatives de connexion (protection contre la force brute) avec un rate limiting.
6.4 Chiffrement des échanges
Les échanges sont actuellement en HTTP clair. Il faut passer en HTTPS (certificat TLS, reverse proxy type Nginx).
6.5 Base de données et secrets
• Ne pas écrire les identifiants MySQL dans le code ni les publier sur GitHub : utiliser des variables d'environnement ou un fichier .env exclu du dépôt.
• Restreindre l'utilisateur extern_user à l'adresse IP du serveur API plutôt qu'à tout hôte (%), et filtrer le port 3306 par pare-feu.
• Appliquer le principe du moindre privilège et sauvegarder régulièrement la base.
6.6 Mise en production
• Désactiver debug=True (il expose la console et les traces d'erreurs) et utiliser un serveur WSGI (Gunicorn).
• Limiter les ouverture réseau : l'entrée NAT de la box doit être temporaire et restreinte, ou remplacée par un VPN.
• Configurer CORS, journaliser les accès et les erreurs, et surveiller les journaux.
6.7 Qualité et tests
Automatiser les tests Postman (collections et runner) afin de détecter les régressions à chaque nouvelle version.
Bilan : l'API répond aux exigences fonctionnelles du cahier des charges ; la sécurisation (requêtes paramétrées, hachage des mots de passe, HTTPS, jetons) constitue la priorité de la prochaine version (v4).
