import socket, sys, signal

host = sys.argv[1]
port = int(sys.argv[2])

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sc.connect((host, port))

def handleInt(signum, frame):
    print("\nexit")
    sys.exit()

signal.signal(signal.SIGINT, handleInt)

while True:
    events = input()
    print("%d events are created" % len(events))

    sc.send(events.encode())