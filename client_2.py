import socket, cv2,pickle,struct
import pyshine as ps
import imutils

camera =True
if camera == True:
    vid = cv2.VideoCapture('test2.mp4')
else:
    vid = cv2.VideoCapture('test1.mp4')

client_socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
host_ip = 'fe80::f10e:9e0d:4b02:402c%15'
port = 12121
client_socket.connect((host_ip,port))

if client_socket:
    while (vid.isOpened()):
        try:
            img,frame = vid.read()
            frame = imutils.resize(frame,width = 380,height = 380)
            a= pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            #cv2.imshow(f"TO: {host_ip}",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                client_socket.close()
        except:
            print('video finish !')
            break
