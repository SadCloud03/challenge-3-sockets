import threading

lock = threading.Lock()



def hacer_broadcast(cliente_socket, mensaje, clientes):
    with lock:
        for cliente in clientes:
            if cliente != cliente_socket:
                try:
                    cliente.send(mensaje)
                except:
                    clientes.remove(cliente)



def manejo_de_clientes(cliente_socket, direccion, clientes):
    print(f"[nuevo cliente] : [{direccion}]")
    while True:
        try:
            mensaje = cliente_socket.recv(1024)
            print(mensaje.decode())
            
            if not mensaje:
                break

            hacer_broadcast(cliente_socket, mensaje, clientes)
        except:
            break
    
    with lock:
        clientes.remove(cliente_socket)

    print(f"[desconexion] : {direccion}")
    cliente_socket.close()