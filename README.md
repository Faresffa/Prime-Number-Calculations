# Prime-Number-Calculations

Ce repository contient quatre algorithmes différents pour calculer les nombres premiers :

Méthode simple (Brute force) : Cette méthode vérifie chaque nombre pour déterminer s'il est premier en testant la divisibilité par tous les nombres inférieurs à lui. Elle est facile à comprendre mais peu efficace pour de grands nombres.

Test jusqu'à la racine carrée : Cette méthode améliore la méthode simple en ne testant la divisibilité que jusqu'à la racine carrée du nombre. Cela permet de réduire le nombre de vérifications nécessaires, rendant l'algorithme plus rapide que la méthode brute.

Méthode des Buffers (ou approche des tampons) : Cette méthode utilise des tampons pour optimiser le processus de vérification des nombres premiers. Elle est plus rapide que la méthode simple et l'optimisation de l'utilisation des tampons permet d'améliorer la performance.

Crible d'Ératosthène : L'algorithme du crible d'Ératosthène est une méthode efficace pour trouver tous les nombres premiers jusqu'à un certain nombre. Il élimine les non-premiers en marquant les multiples de chaque nombre premier à partir de 2.

Chaque méthode est implémentée dans un fichier séparé, et vous pouvez comparer leurs performances sur différents ensembles de données.
