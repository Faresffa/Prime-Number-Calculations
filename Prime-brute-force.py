def est_premier(nombre):
    if nombre <= 1:
        return False
    for candidate in range(2, nombre):  # Tester tous les nombres de 2 à nombre - 1
        if nombre % candidate == 0:
            return False
    return True

# test
n = int(input("Entrez un nombre : "))
if est_premier(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")
