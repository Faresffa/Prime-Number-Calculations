# def crible_erathostene(limite):
#     # Initialiser une liste où True signifie que le nombre est premier
#     nombres = [True] * (limite + 1)
#     nombres[0] = nombres[1] = False  # 0 et 1 ne sont pas premiers
    
#     for i in range(2, int(limite**0.5) + 1):  # Parcourir jusqu'à la racine carrée de 'limite'
#         if nombres[i]:  # Si 'i' est encore marqué comme premier
#             for j in range(i * i, limite + 1, i):  # Marquer tous les multiples de 'i' comme non premiers
#                 nombres[j] = False

#     # Retourner les nombres qui sont encore marqués comme premiers
#     return [i for i, premier in enumerate(nombres) if premier]

import math

def est_premier_eratosthene(n):
    if n <= 1:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 et 1 ne sont pas premiers
    
    for prime in range(2, int(math.sqrt(n)) + 1):
        if sieve[prime]:
            for not_prime in range(prime * prime, n + 1, prime):
                sieve[not_prime] = False
    
    else :
        return sieve[n]

# TEst
n = int(input("Enter a number: "))
if est_premier_eratosthene(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")






# Exemple d'utilisation
#primes = crible_erathostene(30)
#print(primes)  
