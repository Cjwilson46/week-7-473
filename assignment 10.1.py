import socket
import sys
import hashlib
import datetime

def log_connection(client_address, message, md5_digest):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{timestamp}: Connection from {client_address}, Message: '{message}', MD5 Digest: {md5_digest}\n"
    with open("connection_log.txt", "a") as log_file:
        log_file.write(log_message)
    print(log_message, end='')

def create_md5_hash(message):
    hasher = hashlib.md5()
    hasher.update(message)
    return hasher.hexdigest()

print("Server Starting up\n")

try:
    serverSocket = socket.socket()
    localHost = socket.gethostname()
    localPort = 5555
    serverSocket.bind((localHost, localPort))
    serverSocket.listen(1)
    print('\nWaiting for Connection Request')

    conn, client = serverSocket.accept()
    print("Connection Received from Client: ", client)

    while True:
        buffer = conn.recv(2048)
        if not buffer:
            break  # Exit the loop if no data is received
        message = buffer.decode('utf-8')
        print(message)
        md5_digest = create_md5_hash(buffer)
        log_connection(client, message, md5_digest)
        if 'exit' in message.lower():
            print("Server Terminated by User")
            break

except Exception as err:
    print(str(err))
    sys.exit()

finally:
    conn.close()  # Make sure to close the connection
    serverSocket.close()  # And also close the server socket
