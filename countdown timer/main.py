import time #library with time stuff in python

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) #divmod() takes two numbes and retuns a pair of numbers, the quotient and remainder. So t seconds divided by 60 retuns x mins and y secs
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1) #the sleep(1) function makes the code wait for 1 second
        t -= 1
    
    print("Fim do temporizador!")

t = input("Insira o tempo em segundos: ")
countdown(int(t))