import socket, time, sys, signal

host = sys.argv[1]
port = int(sys.argv[2])

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((host, port))
consumer_number = int(sc.recv(500).decode())
print("Connected, consumer %d" % consumer_number)

def handleInt(signum, frame):
    print("\nexit")
    sys.exit()

signal.signal(signal.SIGINT, handleInt)

while True:
    sc.send('give me message'.encode())
    msg = sc.recv(500).decode()

    if (len(msg)>1):
        print(msg)
    else:
        print(f"Event {msg} is processed in consumer {consumer_number}")
    time.sleep(1)