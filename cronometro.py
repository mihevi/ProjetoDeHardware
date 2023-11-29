import time
import threading
import sys

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    sys.exit()
        

def resposta():
    n = input()
    if n.lower == "p" and t != 1:
       print("good")
    elif n.lower != "p":
       print('vamo')
    else:
       print("you loser")
    
        
t = 10
putz = threading.Thread(target=countdown(t), args=(t))
tome = threading.Thread(target=resposta())

putz.start()

tome.start()

            