TCP Server with MD5 Response Script
Overview

This project consists of a standalone Python script that functions as a TCP server. The server is designed to accept connections on port 5555 from TCP clients operating within the same local IP range. Upon receiving a message, the server generates an MD5 hash of the message and responds to the client with the generated MD5 digest. The server continues to operate until manually terminated by the user.
