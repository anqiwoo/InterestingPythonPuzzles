import socket

# Test
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('127.0.0.1', 9999))
print(s2.recv(1024).decode('utf-8'))
for name in [b'Vicky', b'Lisa', b'Alice']:
    s2.send(name)
    print(s2.recv(1024).decode('utf-8'))
s2.send(b'exit')
s2.close()
