import pickle
import socket

#########SVM
filename = '../../main/clasificadorid2.sav'
svm = pickle.load(open(filename, 'rb'))
# cv2.imshow('img',imagen)
# cv2.waitKey(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.11', 10000)
sock.bind(server_address)
sock.listen(1)  # Acepta hasta 1 conexiones entrantes.
print('esperando conexion')
con, dir_cliente = sock.accept()
print('conexion aceptada de' + str(dir_cliente))
msg_received = con.recv(16)
msg_received_decoded = msg_received.decode('utf-8')
print('se recibio:' + msg_received_decoded)
if msg_received_decoded == 'test_fr_tkinter_tcpip':
    msgen = 'pruebaacep'
    msgend = bytes(msgen, 'utf-8')
    con.sendall(msgend)
    print('se envio:' + msgen)
    con.close()
