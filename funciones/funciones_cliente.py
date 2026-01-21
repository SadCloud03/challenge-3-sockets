import threading
import socket
import time

lock = threading.Lock()



def conectar(PORT, HOST, num_reintentos = 3, tiempo_sleep = 1):
    for intento in range(num_reintentos):
        time.sleep(tiempo_sleep)
        try:
            socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cliente.connect((HOST, PORT))

            return socket_cliente
        except Exception as e:
            print(f"[error] : [{e}] ; [reintento] : [{intento}]")



def escuchar_mensajes(socket_cliente):
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode()

            if not mensaje:
                break

            print("\n" + mensaje)
        except:
            print("[error] : [No conexion to server]")
            break

