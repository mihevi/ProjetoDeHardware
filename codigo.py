import RPi.GPIO as GPIO
import random
import time

# Definindo os pinos para os LEDs e Botões
pinosLeds = [2, 17, 10, 5]
pinosBotoes = [3, 27, 9, 6]

# Configuração inicial do GPIO
GPIO.setmode(GPIO.BCM)
for pin in pinosLeds:
    GPIO.setup(pin, GPIO.OUT)
for pin in pinosBotoes:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Inicializando variáveis
sequencia = []
rodada_atual = 0
botao_pressionado = -1
perdeu_o_jogo = False

# Função para iniciar a próxima rodada
def proximaRodada():
    global rodada_atual
    numero_sorteado = random.randint(0, 3)
    sequencia.append(numero_sorteado)
    rodada_atual += 1

# Função para reproduzir a sequência (sem som)
def reproduzirSequencia():
    for numero in sequencia:
        GPIO.output(pinosLeds[numero], GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pinosLeds[numero], GPIO.LOW)
        time.sleep(0.1)

# Função para aguardar o jogador
def aguardarJogador():
    global perdeu_o_jogo, botao_pressionado
    passo_atual_na_sequencia = 0

    while passo_atual_na_sequencia < rodada_atual and not perdeu_o_jogo:
        botao_pressionado = aguardarJogada()
        if sequencia[passo_atual_na_sequencia] != botao_pressionado:
            gameOver()
            break
        passo_atual_na_sequencia += 1

# Função para aguardar uma jogada
def aguardarJogada():
    jogada_efetuada = False
    botao_pressionado = -1
    while not jogada_efetuada:
        for i in range(4):
            if GPIO.input(pinosBotoes[i]) == GPIO.LOW:
                botao_pressionado = i
                jogada_efetuada = True
                GPIO.output(pinosLeds[i], GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(pinosLeds[i], GPIO.LOW)
                break
        time.sleep(0.1)
    return botao_pressionado

# Função para o fim do jogo
def gameOver():
    global perdeu_o_jogo
    for _ in range(4):
        for pin in pinosLeds:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
        for pin in pinosLeds:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)
    perdeu_o_jogo = True

# Loop principal
try:
    random.seed()
    while True:
        if perdeu_o_jogo:
            sequencia = []
            rodada_atual = 0
            perdeu_o_jogo = False
            time.sleep(1)  # Pausa antes de reiniciar

        proximaRodada()
        reproduzirSequencia()
        aguardarJogador()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()