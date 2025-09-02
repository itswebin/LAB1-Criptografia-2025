from scapy.all import IP, ICMP, send
import time

def enviar_mensaje(mensaje, destino="8.8.8.8"):
    for char in mensaje:
        # cada carácter va en el campo "data" del ICMP
        paquete = IP(dst=destino)/ICMP()/char.encode()
        print(f"Enviando carácter: {char}")
        send(paquete, verbose=0)
        time.sleep(0.5)  # para parecer tráfico normal

if __name__ == "__main__":
    mensaje = input("Ingrese el mensaje cifrado: ")
    ip_destino = input("Ingrese la IP destino (ej: 8.8.8.8): ")
    enviar_mensaje(mensaje, ip_destino)
