import time
import threading
import queue
import sys

def countdown(t, queue):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    # Quando o countdown termina, coloca um sinalizador na fila
    queue.put("countdown_terminou")
    

def resposta(queue):
    while True:
        n = input("Digite 'p' para continuar: ")
        if n.lower() == "p":
            print("good")
            break
        else:
            print('vamo')
            break
        # Coloca um sinalizador na fila indicando que a resposta foi dada
        queue.put("resposta_dada")

# Crie uma fila para comunicação entre as threads
fila = queue.Queue()

# Crie as threads
thread_countdown = threading.Thread(target=countdown, args=(10, fila))
thread_resposta = threading.Thread(target=resposta, args=(fila,))

# Inicie as threads
thread_countdown.start()
thread_resposta.start()

# Aguarde até que a thread de resposta termine
thread_resposta.join()

# Se a thread de resposta terminou, espera pela thread de countdown terminar
thread_countdown.join()

print("Fim do programa.")
