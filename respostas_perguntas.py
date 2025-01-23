print("Jogo de perguntas e respostas")

pergunta = "Qual o maior animal terrestre? "
resposta = "Elefante africano"

respostaDoJogador = str(input(pergunta))

if respostaDoJogador == resposta:
    print("Você acertou")
else:
    print("Você errou")
