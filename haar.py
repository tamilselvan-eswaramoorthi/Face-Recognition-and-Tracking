import numpy as np
import cv2
import serial
import urllib

arduino = serial.Serial('/dev/ttyACM0', 9600)
face_cascade = cv2.CascadeClassifier('face.xml')
url='http://192.168.43.1:8080/shot.jpg'
while True:
	b_imgResp = urllib.urlopen(url)
	b_imgNp = np.array(bytearray(b_imgResp.read()),dtype=np.uint8)
	b_img = cv2.imdecode(b_imgNp,-1)
	b_img = cv2.flip(b_img, 1)
	img = cv2.resize(b_img, (640, 500)) 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    if x<200:
	        arduino.write('A')
	    elif x>300:
	        arduino.write('C')
	    else:
	        arduino.write('B') 
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('img',img)

	k = cv2.waitKey(1)
	if k == 27:
	    cv2.destroyAllWindows()