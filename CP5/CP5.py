from random import choice, randint

def reconstruir_solucao(M, moedas, dp):
    solucao = []
    while M > 0:
        for moeda in moedas:
            if M - moeda >= 0 and dp[M] == dp[M - moeda] + 1:
                solucao.append(moeda)
                M -= moeda
                break
    return solucao


def qtdeMoedasPD(M, moedas):
    dp = [float('inf')] * (M + 1)
    dp[0] = 0
    for i in range(1, M + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    if dp[M] == float('inf'):
        return -1, []
    solucao = reconstruir_solucao(M, moedas, dp)
    return dp[M], solucao


def jogo_moedas():
    print("\n🎮 BEM-VINDO AO DESAFIO DAS MOEDAS! 🎯")
    print("-" * 50)

    pontos = 0

    moedas_opcoes = [
        [1, 3, 4],
        [1, 5, 7, 10],
        [2, 4, 6],
        [1, 2, 5, 10]
    ]

    while True:
        moedas = choice(moedas_opcoes)
        M = randint(8, 30)

        melhor_qtd, melhor_solucao = qtdeMoedasPD(M, moedas)

        if melhor_qtd == -1:
            continue

        print(f"\nMonte o valor: {M}")
        print(f"Moedas disponíveis: {moedas}")

        tentativa = input("\n➡ Quantas moedas você acha que precisa? ")

        if not tentativa.isdigit():
            print("❌ Digite apenas números.\n")
            continue

        tentativa = int(tentativa)

        print("\n🤖 IA calculando a melhor solução…")

        print(f"\n💡 Melhor solução da IA: {melhor_solucao}  --> total: {melhor_qtd} moedas")

        # Sistema de pontuação
        if tentativa == melhor_qtd:
            print("✅ Você acertou exatamente!")
            pontos += 2
        elif tentativa < melhor_qtd:
            print("🤯 UAU! Você sugeriu menos moedas que a IA!")
            pontos += 3
        else:
            print("❌ Você usou mais moedas que o ideal.")
            pontos -= 1

        print(f"📊 Pontuação atual: {pontos}\n")

        jogar = input("Quer jogar novamente? (s/n): ")
        if jogar.lower() != "s":
            print(f"\n🏁 Jogo encerrado! Pontuação final: {pontos}")
            print("👋 Até a próxima!")
            break


if __name__ == "__main__":
    jogo_moedas()
