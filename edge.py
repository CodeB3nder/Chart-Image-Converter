
import cv2
import numpy as np
import points
def scan():
	n = cv2.imread('cropped.png',1)
	#rgb_img=cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
	cap=cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
	#cap=cv2.resize(rgb_img,(1000,700))
	#cap=cv2.resize(rgb_img,(1000,700))
	hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
	lower_red = np.array([30,150,50])
	upper_red = np.array([255,255,180])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(cap,cap, mask= mask)
	#cv2.imshow('Original',cap)
	edges = cv2.Canny(cap,100,200)
	cv2.imwrite('abc.png',edges)
	#cap.release()
	l = points.p_detect()
	#cv2.destroyAllWindows()
	return l
	
