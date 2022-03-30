import socket, plexapi, pyautogui, time
from plexapi.server import PlexServer

while True:
    try:
        plex = PlexServer('http://<IP_ADDRESS>:32400', '<TOKEN>')
        client = plex.client('<CLIENT_NAME>')

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('<IP_ADDRESS>', 5000))
        server.listen()

        print('work')

        serverWorking = True
        clientOnline = False

        while serverWorking:
            clientSocket, address = server.accept()
            clientOnline = True
            while clientOnline:
                data = clientSocket.recv(512).decode()
                #print(data)
                match data:
                    case 'End':
                        serverWorking = False
                        clientSocket.close()
                        clientOnline = False
                    case 'Up':
                        client.moveUp();
                    case 'Left':
                        client.moveLeft()
                    case 'Right':
                        client.moveRight()
                    case 'Down':
                        client.moveDown()
                    case 'Select':
                        client.select()
                    case 'Back':
                        client.goBack()
                    case 'Home':
                        client.goToHome()
                    case 'Menu':
                        client.toggleOSD()
                    case 'Play':
                        client.play()
                    case 'Pause':
                        client.pause()
                    case 'Stop':
                        client.stop()
                    case 'Next':
                        client.stepForward()
                    case 'Prev':
                        client.stepBack()
                    case 'Info':
                        pyautogui.press('i')
                    case 'Sub':
                        pyautogui.press('s')
                    case 'Audio':
                        pyautogui.press('a')
                    case 'Aspect':
                        pyautogui.press('z')
                    case 'i':
                        pass
                    case 's':
                        pass
                    case 'a':
                        pass
                    case 'z':
                        pass
                    case _:
                        clientSocket.close()
                        clientOnline = False
    except:
        clientSocket.close()
        print('error')
    else:
        break
    time.sleep(15)
