import socket


def main():

    SERVER = "127.0.0.1"
    PORT = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print('Connected')

    while True:
        stock = input('Ticker: ')
        client.sendall(bytes(stock, 'UTF-8'))
        msg = client.recv(4096)
        stockprice = msg.decode()
        print(stock, ": $", stockprice)


if __name__ == "__main__":
    main()
