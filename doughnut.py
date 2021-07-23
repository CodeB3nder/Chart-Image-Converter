import cv2
import math
import numpy as np
import xlsxwriter as xw
from tkinter import simpledialog, messagebox
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(255,0,0),cv2.FILLED)
        cv2.imshow('image',img)
        ans.append([x,y])
def vector(a,b):
    return [b[1]-a[1],b[0]-a[0]]
def length(a):
    return math.sqrt(math.pow(a[0],2)+math.pow(a[1],2))
def calculate_angle(ans):
    sum=0
    n=int((len(ans))/2)
    for i in range(n-1):
        pt1=ans[i]
        pt2=ans[n+i]
        pt3=ans[i+1]
        pt4=ans[n+i+1]
        m1=vector(pt1,pt2)
        m2=vector(pt3,pt4)
        length_m1=length(m1)
        length_m2=length(m2)
        a=m1[0]*m2[0]
        b=m2[1]*m1[1]
        c=length_m1*length_m2
        ang=(math.acos((a+b)/c))*57.3
        angles.append(ang)
        sum+=ang
    angles.append(360-sum)
def interpolation():
        for i in range(len(angles)):
            x=int(np.rint((angles[i]/360)*100))
            rst.append(x)
def original(file_name):
    global ans, angles, rst, img, cap
    cap = cv2.imread(file_name,1)
    img = cv2.resize(cap,(1000,700))
    ans=[]
    angles=[]
    rst=[]
    cv2.imshow('image',img)
    messagebox.showinfo("Info", "First select outer points on the circumference and then inner points in same order in clockkwise dirction")
    cv2.setMouseCallback('image',click)
    cv2.waitKey()
    cv2.destroyAllWindows()
    calculate_angle(ans)
    interpolation()
    export_plot_To_Excel()


def export_plot_To_Excel():
    workbook = xw.Workbook("out_donut.xlsx")
    worksheet = workbook.add_worksheet()
    headings = ['Item','Percentage']
    worksheet.write_row('A1', headings)
    i = 1
    for item in range(len(rst)):
        worksheet.write(item + 1, 0, i)
        worksheet.write(item + 1, 1, rst[item])
        i = i+1
    chart1 = workbook.add_chart({'type': 'doughnut'})
    chart1.add_series({
    'name':       'Percentage',
    'categories': ['Sheet1', 1, 0, len(rst), 0],
    'values':     ['Sheet1', 1, 1, len(rst), 1],
    })
    chart1.set_title({'name': 'Resultant Doughnut chart'})
    chart1.set_style(10)
    worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()




