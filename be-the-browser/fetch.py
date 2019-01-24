import sys
import socket

if len(sys.argv) != 4:
    print('Usage: ' + sys.argv[0] + ' <host> <port> <resource>')
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
resource = sys.argv[3]

print('Fetching: http://{host}:{port}{resource}'.format(host=host, port=port, resource=resource))

message_bytes = """GET {resource} HTTP/1.1
Host: {host}

""".format(resource=resource, host=host).encode()

s = socket.socket()
s.connect((host, port))
s.send(message_bytes)

data = s.recv(8192)
while len(data) > 0:
    print(data.decode(), end='')
    data = s.recv(8192)
