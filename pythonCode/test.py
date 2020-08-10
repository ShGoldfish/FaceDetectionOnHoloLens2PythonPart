import numpy as np
import cv2

def detectFaces():
	conf = 0.6
	net = cv2.dnn.readNetFromCaffe("../pythonCode/deploy.prototxt.txt", "../pythonCode/res10_300x300_ssd_iter_140000.caffemodel")
	image = cv2.imread("frame.jpg")
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

		# draw the bounding box of the face along with the associated
		# probability
		# if i==0:
		faces_box = np.append(faces_box,np.around(box, decimals=3))

	#faces_box = faces_box.reshape((num_faces+1,4))
	#faces_box = np.delete(faces_box,0, 0);
	if faces_box.size < 4 || faces_box.size % 4 != 0 :
		return " "
	data = np.array2string(faces_box, separator=',')
	return data[1:-1]

print(detectFaces())