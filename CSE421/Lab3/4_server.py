import socket

DATA_SIZE = 16
DISCONNECT_MSG = "DISCONNECT"

# server information
port = 5050
hostname = socket.gethostname()
host_ip_address = socket.gethostbyname(hostname)
server_socket_addr = (host_ip_address, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)

server.listen()
print("Server is listening now...")

while True:
    conn, addr = server.accept()
    print('Connected to', addr)
    connected = True

    while connected:
        initial_msg = conn.recv(DATA_SIZE).decode('utf-8')
        print("Length of the message", initial_msg)

        if initial_msg:
            msg_len = int(initial_msg)
            msg = conn.recv(msg_len).decode('utf-8')

            if msg == DISCONNECT_MSG:
                conn.send("Goodbye. Nice to meet you!".encode('utf-8'))
                print("Terminating the connection with", addr)
                connected = False
            else:
                hours = int(msg)
                
                salary = 0

                if hours <= 40:
                    salary = hours * 200
                else:
                    salary = 8000 + (hours - 40) * 300
                
                conn.send(str(salary).encode('utf-8'))
    
    conn.close()