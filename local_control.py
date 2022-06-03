import socket, pynput, time

while True:
    try:
        from pynput.keyboard import Key, Controller
        keyboard = Controller()  

        PCName = socket.gethostname()
        addr = socket.gethostbyname(PCName)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', 5000))
        server.listen()

        print('work')
        print(addr)

        serverWorking = True
        clientOnline = False

        while serverWorking:
            clientSocket, address = server.accept()
            clientOnline = True
            while clientOnline:
                data = clientSocket.recv(512).decode()
                print(data)
                match data:
                      case 'End':
                        serverWorking = False
                        clientSocket.close()
                        clientOnline = False
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
                        clientSocket.close()
                        clientOnline = False
    except:
        clientSocket.close()
        print('error')
    else:
        break
    time.sleep(5)
