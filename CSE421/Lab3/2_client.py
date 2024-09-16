import socket

DATA_SIZE = 16
DISCONNECT_MSG = "DISCONNECT"

# server information (not client)
port = 5050
hostname = socket.gethostname()
host_ip_address = socket.gethostbyname(hostname)
server_socket_addr = (host_ip_address, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)

def msg_to_send(msg):
    message = msg.encode('utf-8')
    msg_len = len(message)
    send_len = str(msg_len).encode('utf-8')
    send_len += b' ' * (DATA_SIZE - len(send_len))

    client.send(send_len)
    client.send(message)

    print(client.recv(2048).decode('utf-8'))


while True:
    msg = input("Enter a message: ")
    
    if msg == 'end':
        msg_to_send(DISCONNECT_MSG)
        break
    else:
        msg_to_send(msg)