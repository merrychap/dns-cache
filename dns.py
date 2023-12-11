import argparse
import socket
import sys

from IPy import IP
from resolver import DNS

from server import get_local_ip


MIN_PORT = 0
MAX_PORT = 65536


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='Port for listening connections')
    parser.add_argument('-f', help='IP:Port of a forwader. For example, 8.8.8.8:53')

    args = parser.parse_args()

    port, forwader = args.p, args.f

    if port is None and forwader is None:
        print ('No parameters specified. Please, read help')
        sys.exit(0)

    if ':' in forwader:
        forwader = tuple(forwader.split(':'))
    else:
        forwader = (forwader, 53)
    forwader = (socket.gethostbyname(forwader[0]), int(forwader[1]))
    try:
        IP(forwader[0])
    except ValueError:
        print('[-] Invalid forwader\'s IP')
        sys.exit()

    try:
        port = int(port)
        if port < MIN_PORT or port > MAX_PORT:
            print('[-] Invalid port')
            sys.exit()
    except ValueError:
        print('[-] Invalid port\nTry harder next time c:')
        sys.exit()
    
    dns_server = DNS(port, forwader)
    dns_server.run()


if __name__ == '__main__':
    try:
        main()
    except PermissionError:
        print('Please, use sudo')
        sys.exit(0)
