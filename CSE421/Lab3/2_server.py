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
                count = 0

                for c in msg:
                    if c in 'aeiouAEIOU':
                        count += 1
                
                reply_msg = ""
                if count == 0:
                    reply_msg = "Not enough vowels"
                elif count <= 2:
                    reply_msg = "Enough vowels I guess"
                else:
                    reply_msg = "Too many vowels"
                
                conn.send(reply_msg.encode('utf-8'))
    
    conn.close()