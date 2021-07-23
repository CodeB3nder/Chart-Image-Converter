import numpy as np
import cv2
import xlsxwriter as xw
from tkinter import simpledialog, messagebox
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cart=[]
        cart.append(x)
        cart.append(y)
        string=str(x)+","+str(y)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,string,(x,y),font,.3,(255,0,0),1,cv2.LINE_AA)
        cv2.imshow('image',img)
        ans.append(cart)
def interpolation():
    line_scale_Y=(ans[0][1]-ans[1][1])/(Y_max-Y_min)
    line_scale_X=(ans[2][0]-ans[0][0])/(X_max-X_min)
    for i in range(3,len(ans)):
        points.append([abs(ans[i][0]-ans[0][0])/line_scale_X,abs(ans[0][1]-ans[i][1])/line_scale_Y])
def original(file_name):
    global img, ans, points, cap
    cap = cv2.imread(file_name, 1)
    img = cv2.resize(cap,(1000,700))
    ans = []
    points = []
    cv2.imshow('image',img)
    messagebox.showinfo("Info", "First select origin then select max in Y axis, then X max and then all the rest local maxima")
    cv2.setMouseCallback('image',click)
    cv2.waitKey()
    global Y_max, Y_min, X_max, X_min
    Y_max = simpledialog.askinteger("MAX IN Y AXIS", "Please enter Y_max")
    Y_min = simpledialog.askinteger("MIN IN Y AXIS", "Please enter Y_min")
    X_max = simpledialog.askinteger("MAX IN X AXIS", "Please enter X_max")
    X_min = simpledialog.askinteger("MIN IN X AXIS", "Please enter X_min")
    interpolation()
    export_plot_To_Excel()
    

def export_plot_To_Excel():
    workbook = xw.Workbook("out_scatter.xlsx")
    worksheet = workbook.add_worksheet()
    headings = ['X', 'Y'] 
    worksheet.write_row('A1', headings)
    for item in range(len(points)):
        worksheet.write(item + 1, 0, points[item][0])
        worksheet.write(item + 1, 1, points[item][1])
    chart1 = workbook.add_chart({'type': 'scatter'}) 
    chart1.add_series({  
    'name':       ['Sheet1', 0, 1],  
    'categories': ['Sheet1', 1, 0, len(points), 0],  
    'values':     ['Sheet1', 1, 1, len(points), 1],  
    })
    chart1.set_title ({'name': 'Resultant Graph made using extracted data'})
    chart1.set_x_axis({'name': 'X'})  
    chart1.set_y_axis({'name': 'Y'})
    chart1.set_style(11)  
    worksheet.insert_chart('E2', chart1)
    workbook.close()








