import socket
import datetime

pole = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

class Client:
    def __init__(self):
        self.sock = socket.socket()
        
    def connect(self, host, port):
        print(str(datetime.datetime.now()) + "\nConnecting to {}:{}".format(host, str(port)))
        self.sock.connect((host, port))
        print(str(datetime.datetime.now()) + "\nConnected")

    def send_data(self, value):
        self.sock.send(bytes(value, "utf-8"))
        
    def send_input(self):
        now_turn = 1
        while True:
            if pole == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
                for row in pole:
                    print(row)
                print('Новый раунд! Правила такие - введите номер строки, а затем номер ячейки.')
                print('Начнём?')
            if now_turn == 1:
                print('Ходит игрок 1 - крестик')
            if now_turn == 2:
                print('Ходит игрок 2 - нолик')

            s = input()
            if s == "break":
                break
            self.send_data(s)
            print(str(datetime.datetime.now()) + ':   ' + s)
            cursor = s.split()

            if pole[int(cursor[0])][int(cursor[1])] == 0:
                pole[int(cursor[0])][int(cursor[1])] = now_turn
                if now_turn == 1:
                    now_turn = 2
                else:
                    now_turn = 1

            print(cursor[0], cursor[1])


            for row in pole:
                print(row)

        
class Server:
    def __init__(self, host, port):
        self.serv_sock = socket.socket()
        self.serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv_sock.bind((host, port))
        self.serv_sock.listen()
        self.client_socket = None

    def accept_client(self):
        print(str(datetime.datetime.now()) + "\nAccepting clients")
        incoming_connect = self.serv_sock.accept()
        print(str(datetime.datetime.now()) + "\nAccepted {} - {}".format(str(incoming_connect[0]), str(incoming_connect[1])))
        self.client_socket = incoming_connect[0]

    def recieve_data(self):
        data = self.client_socket.recv(1024)
        print(str(datetime.datetime.now()) + ': ' + str(data))

    def recieve_input(self):
        while True:
            s = self.recieve_data()
            if s == None:
                continue
            if s != None:
                if s == 'break':
                    break
                print(str(datetime.datetime.now()) + ':   ' + s.decode("utf-8"))

        

        
        
        
        

        
        