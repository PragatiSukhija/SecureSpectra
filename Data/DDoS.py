import socket

target_host = '192.168.0.228'
target_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Your UDP data', (target_host, target_port))
sock.close()
