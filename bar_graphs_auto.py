from tkinter import messagebox, simpledialog

import numpy as np
import cv2
import edge
import points
import xlsxwriter as xw
from tkinter import *

poi = []
ans = []

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cart=[]
        cart.append(x)
        cart.append(y)
        cv2.imshow('image',img)
        ans.append(cart)

def interpolation():
    line_scale = ((ans[0][1] - ans[1][1]) / (Y_max - Y_min) )
    for i in li:
        poi.append(round(abs(i/line_scale)))

def export_plot_To_Excel():
    workbook = xw.Workbook("out_bar_auto.xlsx")
    worksheet = workbook.add_worksheet()
    headings = ['X', 'Y'] 
    worksheet.write_row('A1', headings) 
    i = 1
    for item in range(len(poi)):
        worksheet.write(item + 1, 0, i)
        worksheet.write(item + 1, 1, poi[item])
        i = i+1 
    chart1 = workbook.add_chart({'type': 'column'}) 
    chart1.add_series({  
    'name':       ['Sheet1', 0, 1],  
    'categories': ['Sheet1', 1, 0, len(poi), 0],  
    'values':     ['Sheet1', 1, 1, len(poi), 1],  
    })
    chart1.set_title ({'name': 'Resultant Graph made using extracted data'})
    chart1.set_x_axis({'name': 'X'})  
    chart1.set_y_axis({'name': 'Y'})
    chart1.set_style(11)  
    worksheet.insert_chart('E2', chart1)
    workbook.close()

def original(file_name):
    global cap, img1, img, Y_max, Y_min, cropped, x, y, Y_max_cor, X_max_cor, li
    cap = cv2.imread(file_name,1)
    img1=cv2.resize(cap,(1000,700))
    cv2.imwrite('resized.png',img1)
    img=cv2.imread('resized.png',1)
    cv2.imshow('image',img)
    # print("First select origin then select max in Y axis, then X max")
    # cv2.setMouseCallback('image',click)
    # cv2.waitKey()
    # Y_max=int(input("Enter Max value of Y-axis:"))
    # Y_min=int(input("Enter Min value of Y-axis:"))
    messagebox.showinfo("Info", "First select origin then select max in Y axis, then X max")
    cv2.setMouseCallback('image', click)
    cv2.waitKey()
    Y_max = simpledialog.askinteger("MAX IN Y AXIS", "Please enter Y_max")
    Y_min = simpledialog.askinteger("MIN IN Y AXIS", "Please enter Y_min")
    line_scale = (ans[0][1] - ans[1][1]) / (Y_max - Y_min)
    x = ans[0][0]
    y = ans[0][1]
    Y_max_cor= ans[1][1]
    X_max_cor = ans[2][0]
    cropped = img[Y_max_cor-4:y-4, x+4:X_max_cor+4]
    cv2.imwrite("cropped.png", cropped)
    li = edge.scan()
    interpolation()
    export_plot_To_Excel()





