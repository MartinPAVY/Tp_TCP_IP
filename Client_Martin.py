import socket

surname = "Martin"

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration de l'adresse et du port du serveur
server_address = ('localhost', 1675)

# Connexion au serveur
client_socket.connect(server_address)

# Envoi un message au serveur
requete = f"Houston, we've got a {surname} trying to connect, are you awake ?"
client_socket.sendall(requete.encode())

# Réception de la reply
reponse = client_socket.recv(1024).decode()
print(f"Server responded : {reponse}")

# Les informations utilisées seront les suivantes
# Martin Scorsese
# https://fr.web.img6.acsta.net/c_310_420/pictures/19/09/09/12/00/5874736.jpg (image de Martin Scorsese récupérée sur allocine)

while True:
    # Lecture de l'entrée utilisateur
    message = input("Enter a message (or 'quit' to quit) : ")

    # Gestion de l'input 'quit' pour quitter
    if message.lower() == "quit":
        print("Connexion ended... Goodbye")
        break

    # Transmission de la requête au serveur
    requete = f"{message} {surname}"
    client_socket.sendall(requete.encode())

    # Reception de la réponse du serveur (Avec 1024 comme taille maximale des données à recevoir en octets )
    reponse = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {reponse}")

# Connexion fermée
client_socket.close()