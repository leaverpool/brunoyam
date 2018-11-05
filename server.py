from networking import Server

server = Server('localhost', 9234)     # создали объект сервера
server.accept_client()
server.recieve_input()

