import time

print("Bem vindo ao seu cronômetro preferido!!!")

def cronometro(segundos):
    for t in range(segundos, -1, -1):
        minutos, segundos = divmod(t, 60)
        print(f"{minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    print("Tempo esgotado!")

tempo = int(input("Digite o tempo em segundos: "))
cronometro(tempo)
    