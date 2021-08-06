import socket
import threading
from yahoo_fin import stock_info as si


class ClientThread(threading.Thread):

    def __init__(self, clientSocket, clientAdress):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        self.cAdress = clientAdress
        print('Connected with: ', clientAdress)

    def run(self):

        while True:
            print("Waiting for client msg ")
            try:
                msg = self.csocket.recv(4096)
            except ConnectionAbortedError:
                print('Connection to: ', self.cAdress, ' lost')
                break

            stockticker = msg.decode()

            try:
                stockprice = si.get_live_price(stockticker)
            except:            
                self.csocket.sendall(bytes('Invalid', 'UTF-8'))
                continue

            self.csocket.sendall(bytes(str(round(stockprice,2)), 'UTF-8'))
            

def main():

    LOCALHOST = "127.0.0.1"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client request..")

    while True:
        server.listen(1)
        clientSocket, clientAdress = server.accept()
        newClient = ClientThread(clientSocket, clientAdress)
        newClient.start()
        print('active connections: ', threading.activeCount()-1)

if __name__ == "__main__":
    main()
