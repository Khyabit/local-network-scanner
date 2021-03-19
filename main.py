import socket

ip_addr = socket.gethostbyname(socket.gethostname())
incomplete_ip_addr = ''

indices = ip_addr.split('.')
for i in range(3):
    incomplete_ip_addr += f'{indices[i]}.'

for i in range(255):
    ip = f'{incomplete_ip_addr}{i}'
    try:
        print(f'{ip}: {socket.gethostbyaddr(ip)[0]}')
    except:
        pass
