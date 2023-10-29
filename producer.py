import socket, time, sys
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

sc.connect((host, port))

while True:
    events = input()
    sc.send(events.encode())