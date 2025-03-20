import time

def cronometro(horas, minutos, segundos):
    # Convertendo horas, minutos e segundos para total de segundos
    total_segundos = horas * 3600 + minutos * 60 + segundos

    # Contagem regressiva
    for t in range(total_segundos, -1, -1):
        horas, resto = divmod(t, 3600)
        minutos, segundos = divmod(resto, 60)
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    print("Tempo esgotado!")

# Solicitar entrada do usuário
print("Digite o tempo para o cronômetro (máximo 24 horas):")
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Executar o cronômetro
cronometro(horas, minutos, segundos)
