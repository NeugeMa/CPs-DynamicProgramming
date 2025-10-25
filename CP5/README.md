# Resolução - CP5 "O desafio das Moedas"

# 🕹️ Mini-Jogo “Desafio das Moedas” ✅🎮
Tivemos a criatividade de montar um jogo sobre este problema! Que contém as funções obrigatórias e explicações necessárias para seu desenvolvimento. Nosso jogo possui:
- Pontuação
- Faz o jogador competir contra o algoritmo
- Mostra quais moedas devem ser usadas


## 🧩 Soluções Implementadas
O grupo implementou quatro funções para resolver o problema:

| Função                | Estratégia            |  Corretude   |  Performance   |
| --------------------- | --------------------- | :--------:   | :-----------:  |
| `qtdeMoedas()`        | Gulosa                | ❌ Às vezes | ✅ Alta        |
| `qtdeMoedasRec()`     | Recursiva pura        |      ✅     | ❌ Muito lenta |
| `qtdeMoedasRecMemo()` | Top-Down Memoization  |      ✅     | ✅ Boa         |
| `qtdeMoedasPD()`      | Bottom-Up Programming |      ✅     | ✅ Excelente   |


## ⚠️ Quando o algoritmo guloso falha?
O algoritmo guloso tenta sempre pegar a maior moeda possível…
Mas isso nem sempre resulta no menor número de moedas!

| Montante | Moedas    | Guloso             | Ótimo (PD)             |
| -------- | --------- | ------------------ | ---------------------- |
| 6        | [1, 3, 4] | 3 + 3 = 2 moedas ❌ | 4 + 1 + 1 = 3 moedas ✅ |

Observações: O guloso parece ótimo, mas erra em alguns sistemas de moedas


### Integrantes
- Heloísa Real  | RM554535
- Mariana Neugebauer Dourado | RM550494

### Repositório Exercício
[Repositório Exercício](https://github.com/mmamorim/dynprog-2025-2/blob/main/CP05-Enunciado.md)
