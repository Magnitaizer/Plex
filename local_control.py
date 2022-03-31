# Socket server in python using select function
 
import socket, select, pynput

def main():
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    from pynput.keyboard import Key, Controller
    keyboard = Controller()
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print("Chat server started on port " + str(PORT))
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
             
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)
                 
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = str(sock.recv(RECV_BUFFER))
                    print(data)
                    control = data[2:-1]  #Get rid of extra symbols if your client is sending any
                    print(control)
                    match control:
                      case "Up":
                        keyboard.press(Key.up)
                        keyboard.release(Key.up) 
                      case "Left":
                        keyboard.press(Key.left)
                        keyboard.release(Key.left) 
                      case "Right":
                        keyboard.press(Key.right)
                        keyboard.release(Key.right) 
                      case "Down":
                        keyboard.press(Key.down)
                        keyboard.release(Key.down) 
                      case "Select":
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter) 
                      case "Back":
                        keyboard.press('b')
                        keyboard.release('b') 
                      case "Home":
                        keyboard.press('h')
                        keyboard.release('h') 
                      case "Menu":
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                      case "Info":
                        keyboard.press('i')
                        keyboard.release('i')
                      case "Play":
                        keyboard.press('p')
                        keyboard.release('p') 
                      case "Pause":
                        keyboard.press('p')
                        keyboard.release('p') 
                      case "Stop":
                        keyboard.press('x')
                        keyboard.release('x') 
                      case "Next":
                        keyboard.press(Key.up)
                        keyboard.release(Key.up) 
                      case "Prev":
                        keyboard.press(Key.down)
                        keyboard.release(Key.down) 
                      case "NextSub":
                        keyboard.press('l')
                        keyboard.release('l') 
                      case "NextAudio":
                        keyboard.press('a')
                        keyboard.release('a') 
                      case _:
                        print("Err 404 Not Found!")
                       
                # client disconnected, so remove from socket list
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
         
    server_socket.close()
    
if __name__ == "__main__":
    main()