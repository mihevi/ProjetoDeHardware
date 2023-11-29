import time
tempo_inicio = time.time()
n = int(input())
tempo_final = time.time()
tempo = tempo_final - tempo_inicio
print(tempo)
if tempo >= 10:
    print("You loser")
    
elif n != 2:
    print("your lose")
else: 
    print("Good man!")
