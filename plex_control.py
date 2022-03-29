# Socket server in python using select function
 
import socket, select, plexapi

from plexapi.server import PlexServer
baseurl = '<SERVER_IP>'
token = '<TOKEN>'
plex = PlexServer(baseurl, token)

def main():
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
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
                    control = data[2:-1]
                    match control:
                      case "Up":
                        plex.clients()[0].moveUp(); 
                      case "Left":
                        plex.clients()[0].moveLeft();
                      case "Right":
                        plex.clients()[0].moveRight();
                      case "Down":
                        plex.clients()[0].moveDown();
                      case "Enter":
                        plex.clients()[0].select();
                      case "Back":
                        plex.clients()[0].goBack();
                      case "Home":
                        plex.clients()[0].goToHome();
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