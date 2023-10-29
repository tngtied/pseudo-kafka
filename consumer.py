import socket, time, sys

host = sys.argv[1]
port = int(sys.argv[2])

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect((host, port))

print("[Producer connected]")

while True:
    sc.send('give me message'.encode())
    msg = sc.recv(100).decode()

    time.sleep(1)