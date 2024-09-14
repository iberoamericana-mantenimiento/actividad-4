import socket
import threading
 
def handle_client(client_socket):
    welcome_message = "¡Hola! Ya estás conectado al servidor."
    client_socket.send(welcome_message.encode('utf-8'))
    request = client_socket.recv(1024)
    print(f"Recibido: {request.decode('utf-8')}")
    client_socket.close()
 
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65433))
    server_socket.listen()
    print("Servidor conectado al puerto 65433...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conectado a {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
 
if __name__ == "__main__":
    start_server()