from functools import lru_cache

@lru_cache(maxsize=None)
def vence(n):
    if n <= 0:
        return False
    if not vence(n - 1):
        return True
    if not vence(n - 2):
        return True
    if not vence(n - 3):
        return True
    return False

def jogada_computador(n):
    for move in (1, 2, 3):
        if n - move >= 0 and not vence(n - move):
            return move
    return 1  

def jogar(n):
    print(f"\nJogo das Pedras iniciado com {n} pedras!")
    jogador = True  # True = humano, False = computador 

    while n > 0:
        print(f"\nRestam {n} pedras.")
        if jogador:  # Usuário
            jogada = int(input("Sua vez! Retire 1, 2 ou 3 pedras: "))
            if jogada not in (1, 2, 3) or jogada > n:
                print("Jogada inválida, tente novamente.")
                continue
            
        else:       # Computador
            jogada = jogada_computador(n)
            print(f"Computador retira {jogada} pedras.")
        n -= jogada
        jogador = not jogador

    if not jogador:
        print("\nVocê venceu!")
    else:
        print("\nO computador venceu!")

    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta == 's':
            jogar(15)
            break
        elif resposta == 'n':
            print("Obrigado por jogar!")
            break
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    jogar(15)