import socket, sys
from threading import Thread
from queue import Queue

host = sys.argv[1]
port_a = int(sys.argv[2])
port_b = int(sys.argv[3])

events_queue = Queue()

def producer_worker():
    while True:
        events = producer_conn.recv(1000).decode()
        if not events:
            producer_conn.close()
            #comment out before submission
            print("[Producer disconnected]")
            break
        ##이거 괜찮은 거 맞나?
        print("[Events created]")
        for index in range(0, len(events)):
            events_queue.put(events[index])
    # ##producer 단위 확인용 iteration
    # print("in queue: ")
    # for event in iter(events_queue.get, None):
    #     print("  %c" % event)
        print("[Remain events: %d]" % events_queue.qsize())
        


# def consumer_worker(...): ...

if (__name__ == '__main__'):
    producer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    producer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    producer_socket.bind((host, port_a))
    producer_socket.listen(5)    

    producer_conn, producer_addr = producer_socket.accept()
    print("[Producer connected]")
    
    producer_thread = Thread(target = producer_worker) 
    producer_thread.start()

    # consumer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # consumer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # consumer_socket.bind((host, port_b))
    # consumer_socket.listen(5)

    # consumer_group = []
    # consumer_count = 0
    # while True: 
    #     conn

    #     worker_thread = Thread(target = consumer_worker, args=(,))
    #     worker_thread.start()