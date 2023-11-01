import socket, sys, signal
from threading import Thread
from queue import Queue

host = sys.argv[1]
port_a = int(sys.argv[2])
port_b = int(sys.argv[3])

events_queue = Queue()

def producer_worker():
    global producer_conn
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

def consumer_worker(conn, num):
    global consumer_count
    conn.send(str(num).encode())
    while True:
        events = conn.recv(1000).decode()
        if not events:
            conn.close()
            print("[Consumer %d disconnected]" % num)
            consumer_count-=1
            print(f"[{consumer_count} consumers online]")
            break
        if (events_queue.empty()):
            conn.send("No event in queue".encode())
        else:
            conn.send(events_queue.get().encode())
            print("[Remain events: %d]" % events_queue.qsize())

def handleInt(signum, frame):
    print("\nexit")
    producer_socket.close()
    sys.exit()

signal.signal(signal.SIGINT, handleInt)

if (__name__ == '__main__'):
    producer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    producer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    producer_socket.bind((host, port_a))
    producer_socket.listen(5)    

    producer_conn, producer_addr = producer_socket.accept()
    print("[Producer connected]")
    
    producer_thread = Thread(target = producer_worker) 
    producer_thread.start()

    consumer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    consumer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    consumer_socket.bind((host, port_b))
    consumer_socket.listen(5)
    consumer_group = []
    consumer_count = 0
    consumer_cumul_count = 0

    while True: 
        consumer_conn, consumer_addr = consumer_socket.accept()
        consumer_count+=1
        consumer_cumul_count+=1
        print(f"[Consumer {consumer_cumul_count} connected]")
        print(f"[{consumer_count} consumers online]")


        consumer_group.append(consumer_conn)

        worker_thread = Thread(target = consumer_worker, args=(consumer_conn, consumer_cumul_count))
        worker_thread.start()