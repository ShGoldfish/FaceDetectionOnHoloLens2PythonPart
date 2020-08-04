import socket
import cv2
import numpy as np
import os
import io
import PIL.Image as Image

########## Replace the value with your own HOloLens 2 IP Address
host = "192.168.1.18"

#########################################read img from byte file 

def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

def saveImgFromByteFile(fileNum):
	if not(os.path.isfile('Data/jpgframe'+str(fileNum))):
		return False
	byteImg = readimage('Data/jpgframe'+str(fileNum))
	stream = io.BytesIO(byteImg)
	try:
		img = Image.open(stream)
		img.save('frame.jpg')
	except OSError:
		print("Cannot save jpgframe{}".format(str(fileNum)))
	stream.close()
	return True

##############################################Face Detection#######################
def detectFaces():
	conf = 0.6
	net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
	image = cv2.imread("frame.jpg")
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))

	net.setInput(blob)
	detections = net.forward()
	num_faces = 0
	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		
		if confidence > conf:
			num_faces +=1
	data = str(num_faces)
	return data

##############################################Socket connection#######################
bitPerG = 1024
size = 8100*bitPerG

# HoloLens ip and port [9005 is the only working port !!]
port = 9005   
fileNum = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

while True:
	try:
		byteImg = bytearray(sock.recv(size))
		stream = io.BytesIO(byteImg)
		try:
			img = Image.open(stream)
			img.save('frame.jpg')
		except OSError:
			print("Cannot save frame")
		stream.close()
		data = detectFaces()
		# Send Face Detection Result to HL
		sock.sendall(data.encode())
	finally:
		pass

