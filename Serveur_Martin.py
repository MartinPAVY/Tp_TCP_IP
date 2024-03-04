import datetime
import socket

# Initialisation des informations
surname = "Martin"
age = 20

def find_port(age):
    """
    Permer de lier un port au socket en fonction de l'age
    """
    port = 1655 + age
    while True:
        try:
            # Essayez de lier le socket au port
            server_socket.bind(('localhost', port))
            break
        except OSError as e:
            # Incrémente le port de 100 si il y a une erreur (ex port déjà occupé)
            port += 100




# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Appelle la fonction findPort, et passage de paramètre age
find_port(age)

# Activation du mode écoute du socket
server_socket.listen(5)

# Les informations utilisées seront les suivantes
# Martin Scorsese
# https://fr.web.img6.acsta.net/c_310_420/pictures/19/09/09/12/00/5874736.jpg (image de Martin Scorsese récupérée sur allocine)

# Tentative de lancement du server
try:

    # Autorise les connexions entrantes
    client_socket, client_address = server_socket.accept()
    print(f"Successfully connected {client_address}")

    while True:

        # Réception du message du client
        message = client_socket.recv(1024).decode()
        print(f"Client message : {message}")

        # Vérification du message/Date
        if (message[0:4] == "date"):
            # Récupération de la currentDate
            currDate = datetime.datetime.now()
            # currentDate formatée avec les minutes/heures
            currDateFormated = currDate.strftime("%Y-%m-%d %H:%M:%S")
            # Ajout de la date dans le retour
            message = "Current date is : " + str(currDateFormated)

        # Ajout d'une réponse au message
        message += " \nI love martin scorsese !"

        # Réponse retournée
        client_socket.send(message.encode())
except ConnectionAbortedError: # Retourne un message d'erreur si la connexion est terminée par le client
    print("Correction ended")
    client_socket.close()