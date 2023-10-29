import socket, sys
from threading import Thread
from queue import Queue

host = sys.argv[1]
port_a = int(sys.argv[2])
port_b = int(sys.argv[3])

data_queue = Queue

print(sys.argv)

def producer_worker():

def consumer_worker(...): ...

if (__name__ == '__main__'):
    producer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    producer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    producer_socket.bind((host, port_a))
    producer_socket.listen(5)    

    producer_socket_, producer_addr = producer_socket.accept()

    producer_thread = Thread(target = producer_worker) 
    producer_thread.start()

    consumer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    consumer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    consumer_socket.bind((host, port_b))
    consumer_socket.listen(5)

    consumer_group = []
    consumer_count = 0
    while True: 
        conn

        worker_thread = Thread(target = consumer_worker, args=(,))
        worker_thread.start()