import subprocess
import threading
import configparser
import multiprocessing

import os
import sys
import signal

import socket
import time

def is_tcp_open(host="127.0.0.1", port=25000, timeout=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        err = s.connect_ex((host, port))
        return err == 0
    finally:
        s.close()


def main():

    port = 25000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    while True:

        print("%d %s" % (port, "OK" if is_tcp_open(port=port) else "REFUSED"))
        time.sleep(2)
