import socket
import sys

def log_message_and_response(message, response):
    with open("client_log.txt", "a") as log_file:
        log_message = f"Message: '{message}', Response: {response}\n"
        log_file.write(log_message)
    print(log_message, end='')

def main():
    print("Client Application")
    print("Establishing a connection to a server")
    print("Available on the same host using PORT 5555")

    PORT = 5555  # Port number of server
    messages = ["Hello, server!", "How are you?", "This is message three", "Testing message four",
                "Python networking is cool", "Black Hat Python", "Message seven", "Another message",
                "Penultimate message", "Final message"]

    try:
        clientSocket = socket.socket()
        localHost = socket.gethostname()
        print("\nAttempting Connection to: ", localHost, PORT)
        clientSocket.connect((localHost, PORT))
        print("Socket Connected ...")

        for msg in messages:
            print(f"Sending: {msg}")
            messageBytes = msg.encode("utf-8")
            clientSocket.sendall(messageBytes)
            
            # Wait for response
            buffer = clientSocket.recv(2048)
            response = buffer.decode("utf-8")
            print(f"Response: {response}")
            
            # Log the message and response
            log_message_and_response(msg, response)

            if msg == "Final message":  # Exit after sending the last message
                print("All messages sent. Closing connection.")
                break

        clientSocket.close()

    except Exception as err:
        print("An error occurred:", str(err))
        sys.exit()

if __name__ == "__main__":
    main()
