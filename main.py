import time 

def cronometro(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos

    for t in range(total_segundos, -1, -1):
        horas, resto = divmod(t, 3600)
        minutos, segundos = divmod(resto, 60)
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    print("Tempo esgotado")

print("Bem-vindo ao cronometro mais legal de todos!!")
print("Digite um tempo para o seu cronometro:")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

cronometro(horas, minutos, segundos)
