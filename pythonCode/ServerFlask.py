from flask import Flask, jsonify, request, send_file
import PIL.Image as Image
import numpy as np
import threading
import logging
import time
import json
import cv2
import os
import io

##############################################Face Detection#######################
app = Flask(__name__)
return_data = "Null"


@app.route('/')
def hello_world():
	print("hello, world!")
	return "hello, world!"

@app.route('/receive-image', methods=['POST'])
def receive_image():
	global return_data
	data = request.files.get('myImage')
	b = bytes(data.read())
	# b = bytearray(data)
	buf = io.BytesIO(b)
	try:
		img = Image.open(buf)
		img.save('frame.jpg')
	except OSError:
		return_data = " "
		print("Cannot save frame")
	buf.close()
	image = cv2.imread("frame.jpg")
	conf = 0.6
	net = cv2.dnn.readNetFromCaffe("../pythonCode/deploy.prototxt.txt", "../pythonCode/res10_300x300_ssd_iter_140000.caffemodel")
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()

	num_faces = 0
	faces_box = np.array([])
	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		#print(confidence)
		if confidence < conf:
			continue
		num_faces += 1
		# compute the (x, y)-coordinates of the bounding box for the object
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		faces_box = np.append(faces_box,box.astype("int"))#np.around(box, decimals=3))
	n = faces_box.size
	if n < 4 :
		return_data = " "
		return return_data
	if n % 4 != 0:
		faces_box = faces_box[:-n]
	
	return_data = np.array2string(faces_box, separator=',')
	return return_data[1:-1]

@app.route('/detect-faces', methods=['GET'])
def detect_faces():
	global return_data
	return return_data[1:-1]

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 9005, debug=True )
