letra = input("Digite uma letra: ").strip().lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra do alfabeto.")
elif letra in 'aeiou':
    print("Vogal")
else:
    print("Consoante")
    # Caio Figueira Machado