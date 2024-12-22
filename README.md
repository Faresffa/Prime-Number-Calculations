# Prime-Number-Calculations

Ce repository contient quatre algorithmes différents pour calculer les nombres premiers :

1. Méthode naïve (Brute force)
Cette méthode vérifie si un nombre est divisible par tous les entiers strictement inférieurs à lui (à partir de 2). Bien qu'elle soit facile à comprendre, elle est inefficace pour des grands nombres à cause du grand nombre d'opérations.

2. Test jusqu'à la racine carrée
Cette version optimise la méthode brute en limitant les tests de divisibilité jusqu'à la racine carrée du nombre. Cela réduit considérablement le nombre de calculs nécessaires et rend l'algorithme bien plus rapide.

3. Crible d'Ératosthène
Un algorithme classique qui détermine tous les nombres premiers jusqu'à une limite donnée. Il fonctionne en marquant les multiples des nombres premiers et est idéal pour générer une liste de nombres premiers. Cependant, il est moins adapté pour vérifier un seul nombre.

Pourquoi le crible d'Ératosthène ?:
Le crible d'Ératosthène est une méthode ultra-efficace pour générer tous les nombres premiers jusqu'à une limite n, avec une complexité de 𝑂(𝑛 log log 𝑛). Plutôt que de tester chaque nombre individuellement, il élimine les multiples de manière systématique, garantissant une rapidité imbattable pour les grands ensembles

Structure du dépôt
Chaque méthode est implémentée dans un fichier Python distinct, et des exemples d’utilisation sont inclus. Cela vous permet de comparer facilement leurs performances et de choisir l’approche la plus adaptée à vos besoins.


