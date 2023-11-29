import RPi.GPIO as GPIO
import random
import time
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
    print("Botão pressionado:", botao_pressionado)  # Adicione esta linha para debug
    return botao_pressionado
