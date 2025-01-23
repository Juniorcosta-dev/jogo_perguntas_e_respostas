print("Jogo de perguntas e respostas")

perguntaRespostas = {
    "Qual o maior animal terrestre?": "elefante africano",
    "Qual é o país mais populoso do mundo?": "china",
    "Quantos planetas existem no sistema solar?": "Oito"
}

pontuacao = 0

for pergunta, respostaCerta in perguntaRespostas.items():
    respostaDoJogador = input(pergunta + " ").lower()

    if respostaDoJogador == respostaCerta.lower():
        print("Você acertou!\n")
        pontuacao += 1
    else:
        print(f"Você errou! A resposta correta é: {respostaCerta}\n")

print(f"Fim do jogo! Sua pontuação {pontuacao} de {len(perguntaRespostas)} perguntas.")
