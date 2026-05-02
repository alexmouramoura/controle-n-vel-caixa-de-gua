from colorama import Fore, Style, init
import time

# Inicializa o colorama
init(autoreset=True)

# Sistema contínuo
while True:
    try:
        nivel = float(input("\nDigite o nível do reservatório (em metros): "))

        # Faixas contínuas (sem buracos)
        if 2.5 <= nivel <= 5.0:
            print(Fore.RED + "Nível muito baixo (CRÍTICO)")

        elif 5.5 < nivel <= 10.0:
            print(Fore.YELLOW + "Nível baixo")

        elif 11.0 < nivel <= 14.0:
            print(Fore.GREEN + "Nível médio")

        elif 15.0 < nivel <= 20.0:
            print(Fore.CYAN + "Nível alto")

        elif 25.0 < nivel <= 30.0:
            print(Fore.BLUE + "Nível muito alto (ALERTA)")

        else:
            print(Fore.WHITE + "Valor fora da faixa do reservatório!")

        # Pequena pausa (opcional)
        time.sleep(1)

    except ValueError:
        print(Fore.WHITE + "Entrada inválida! Digite um número válido.")

    except KeyboardInterrupt:
        print(Fore.WHITE + "\nSistema encerrado.")
        break