import socket
import threading
from funciones.funciones_servidor import manejo_de_clientes

def main():
    # ----- no quiero que haya conflicto en la lista de clientes -----
    lock = threading.Lock()

    # ------ cosas que va a necesitar mi servidor -----
    PORT = 5000
    HOST = "127.0.0.1"

    # ----- almacen de clientes -----
    clientes = []

    # ----- hacer el servidor en si ------
    # su socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # su puerto y el host
    servidor_socket.bind((HOST, PORT))
    # que empiece a escuchar
    servidor_socket.listen()

    print(f"servidor escuchando en {HOST} : {PORT}")

    # ------ bucle para aceptar clientes -----
    while True:
        cliente_socket, direccion = servidor_socket.accept()
        cliente_socket.send("[connexion success]".encode())
        with lock:
            clientes.append(cliente_socket)

        # manejo de multiples clientes
        hilo = threading.Thread(
            target=manejo_de_clientes,
            args=(cliente_socket, direccion, clientes),
            daemon=True
        )

        hilo.start()

if __name__ == "__main__":
    main()


