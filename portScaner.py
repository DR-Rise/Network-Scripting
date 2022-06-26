import socket
import threading
from queue import Queue

import time
start_time = time.time()

target = "192.168.1.1"
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            open_ports.append(port)

port_list = range(1,1024)
fill_queue(port_list)

thread_list = []

for t in range(600):
    thread = threading.Thread(target= worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("\nOpen ports are : ",open_ports)


print("\n--- %s seconds ---" % (time.time() - start_time))
