import time
t = 0
while t < 3:
    time1 = time.time()
    n = input() 
    time2 = time.time()
    print(time2-time1)
    if (time2-time1) > 10:
            
        break
         
    t += 1