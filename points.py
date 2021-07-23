
import numpy as np
import cv2

def p_detect():
    font = cv2.FONT_HERSHEY_COMPLEX
    img2 = cv2.imread('abc.png', cv2.IMREAD_COLOR)
    img3= cv2.imread('abc.png', cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img3, 110, 255, cv2.THRESH_BINARY) 
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE) 
    art=[]
    for cnt in contours :

        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        n = approx.ravel()
        i = 0
        for j in n : 
            if(i % 2 == 0):
                x = n[i] 
                y = n[i + 1] 
                #string = str(x) + " " + str(y)
                art.append([x,y])
                #cv2.putText(img2, string, (x, y),  font, 0.5, (225,240,0))
            i = i + 1
    #cv2.imshow('image2', img2)
    #if cv2.waitKey(0) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
    hgt=[]
    w=[]
    for i in range(0,len(art)):
        hgt.append(art[i][1])
    y_max=max(hgt)
    for i in range(0,len(hgt),6):
        w.append(abs(hgt[i]-y_max))
    #print(w)
    return w






