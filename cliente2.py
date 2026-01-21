import threading
from funciones.funciones_cliente import escuchar_mensajes, conectar

# ------ informacion del servidor a conectarse ------
PORT = 5000
HOST = "127.0.0.1"

def main():
    # ----- iniciar la conexion ------

    cliente_socket = conectar(PORT, HOST)

    nombre = input("ingrese su nombre: ")

    try:
        cliente_socket.send(f"[conectado] : {nombre}".encode())
    except (Exception, KeyboardInterrupt) as e:
        print(f"[error] : {e}")

    print("[for exit] : './exit'\n[for reconecting] : './reconnect' ")

    # ----- manejo de recepcion de mensajes -----

    hilo = threading.Thread(
        target=escuchar_mensajes,
        args=(cliente_socket,),
        daemon=True
    )

    hilo.start()

    # ----- bucle de envio de mensajes -----
    while True:

        try:
            mensaje = input("")

            if mensaje == "./exit":
                print("[exiting]")
                break

            elif mensaje == "./reconnect":
                cliente_socket = conectar(PORT, HOST)

                hilo = threading.Thread(
                    target=escuchar_mensajes,
                    args=(cliente_socket,),
                    daemon=True
                )
                hilo.start()

            cliente_socket.send(f"[{nombre}] : {mensaje}".encode())

        # error mas sencillo 
        except (Exception, KeyboardInterrupt) as e:
            print(f"[error] : {e}")

    if cliente_socket:
        cliente_socket.close()

    print("[closed client]")

if __name__ == "__main__":
    main()