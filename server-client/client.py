import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65433))
    message = "Hola, servidor!"
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print(f"Respuesta del servidor: {response.decode('utf-8')}")
    client_socket.close()

if __name__ == "__main__":
    start_client()