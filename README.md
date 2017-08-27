# Cached DNS Server Implementation

### General description
This is implementation of Cached DNS Server written in Python3.

### Requirements
- Python 3.*
- IPy

### Usage
To run server use next command:
```sh
$ python3 dns.py [-h] [-p P] [-f F]
```

List of arguments:
  - h, --help  show this help message and exit
  - p P        Port for running server
  - f F        Address of forwader

After you run server you can make queries to it by typing next (get A records for google.com):
```sh
dig +notcp @127.0.0.1 -p 9090 google.com A
```

### Example of using
```sh
$ python3 dns.py -p 9090 -f 8.8.8.8
[+] Server is configurated
[+] Server is running on 9090 port

2017-05-09 20:14:50 -- [*] 127.0.0.1 A google.com. forwader

2017-05-09 20:14:51 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:52 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:52 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:52 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:53 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:53 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:14:54 -- [*] 127.0.0.1 A google.com. cache

2017-05-09 20:15:02 -- [*] 127.0.0.1 A ya.ru. forwader

2017-05-09 20:15:03 -- [*] 127.0.0.1 A ya.ru. cache

2017-05-09 20:15:05 -- [*] 127.0.0.1 NS ya.ru. forwader

2017-05-09 20:15:06 -- [*] 127.0.0.1 NS ya.ru. cache
```