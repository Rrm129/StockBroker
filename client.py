import socket
import time


def main():

    SERVER = "127.0.0.1"
    PORT = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print('Connected')
    program = True
    y = True
    
    while program == True:

        print('1) Show info\n2) Broker\n3) Close')
        x = input('input:')
        print()
        

        if x == '1':
            print('Name: Elon Musk\nDOB: 12/12/1997\n500,000 TSLA\n100,000 Space X\n') 
        
        if x == '2':
            
            while  y == True:
                stock = input('Ticker: ')
                if stock == 'break':
                    break

                client.sendall(bytes(stock, 'UTF-8'))
                msg = client.recv(4096)
                stockprice = msg.decode()
               
                if stockprice == 'Invalid':
                    print('Invalid')
                    continue
                
                print(stock.upper(), ": $", stockprice,'\n')

            # client.close()

        if x == '3':
            print('Logging out')
            time.sleep(2)
            # client.close()
            break

    
if __name__ == "__main__":
    main()
