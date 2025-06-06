def fatorial(n):
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Exemplo de uso:
if __name__ == "__main__":
    numero = int(input("Digite um número inteiro não negativo: "))
    print(f"Fatorial de {numero} é {fatorial(numero)}")
    # Caio Figueira Machado