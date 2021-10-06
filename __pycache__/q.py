import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Arbejder på {item}')
        print(f'Færdiggjorde {item}')
        q.task_done()

#Start tråd
threading.Thread(target=worker, daemon=True).start()

#Send 5 requests til worker
for item in range(10000):
    q.put(item)
print('All requests sent\n', end='')

q.join()
print('Færdig')
