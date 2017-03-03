# COEN498 PP (Cloud Computing) Assignment 1
## Assignment 1: Guessing animal game

### Running the application
Use python 3.x and call either the server.py or the client.py from command line. Or similar execute one of the precompiled binaries in the "dist" from command line
A remote instance of the program is hosted at fajardo.io (Digital Ocean - New York) and timmy.noip.me (Self hosted - Montreal). It will be accessible until March 31st
This program uses Python 3 and protobuf, please ensure they are installed before running.

- Running the client
To run from source directly, call "python3 client.py <host> <serialization method>"
Builds from Windows and Ubuntu are available in the "dist" folder as "guessing_animal_client" & "guessing_animal_client_ubuntu"

- Running the server
The server is more independent and just requires "python3 server.py" to be called. Precompiled binaries are available
Builds from Windows and Ubuntu are available in the "dist" folder as "guessing_animal_server" & "guessing_animal_server_ubuntu"
