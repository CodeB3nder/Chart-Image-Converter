from tkinter import simpledialog

import numpy as np
from collections import Counter
import cv2
import extcolors
import PIL
import math
import collections
import xlsxwriter as xw
def original(file_name):
    global majors
    cap = cv2.imread(file_name,1)
    img = cv2.resize(cap,(1000,700))
    output=img.copy()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,1500,param1=200,param2=30,minRadius=0,maxRadius=0)
    fig=np.uint16(np.around(circles))
    ans=[]
    for (x,y,r) in fig[0,:]:
        for angle in range(0,360,1):
            cgn=math.radians(angle)
            X=int(x+((r-int(r/2))*math.cos(cgn)))
            Y=int(y+((r-int(r/2))*math.sin(cgn)))
            ans.append([X,Y])

    a=[]
    for i in range(len(ans)):
        a.append(list(img[ans[i][1]][ans[i][0]]))
    b=[]
    for i in range(0,360,1):
        b.append(int(a[i][0])+int(a[i][1])+int(a[i][2]))
    res = Counter(b)
    percentage = {}
    for key in dict(res):
        percentage[key] = res[key]/360 * 100
    non_majors=[]
    majors=[]
    rgbs=[]
    t = simpledialog.askinteger("LABELS", "Enter no of labels:")
    for key,value in percentage.items():
        rgbs.append([key,value])
    rgbs.sort(key= lambda x: x[1],reverse=True)
    k=len(rgbs)
    for i in range(k):
        if i<t:
            majors.append([rgbs[i][0],rgbs[i][1]])
        else:
            non_majors.append([rgbs[i][0],rgbs[i][1]])
    majors.sort(key= lambda x: x[0])
    non_majors.sort(key= lambda x: x[0])
    for i in range(len(non_majors)):
        min=abs(majors[0][0]-non_majors[i][0])
        for j in range(1,len(majors)):
            c=abs(majors[j][0]-non_majors[i][0])
            if(c>min):
                majors[j-1][1]=majors[j-1][1]+non_majors[i][1]
                break
            elif(c<min and j==len(majors)-1):
                majors[j][1]=majors[j][1]+non_majors[i][1]
                min=c
            else:
                min=c
    export_plot_To_Excel()
#print(majors)
def export_plot_To_Excel():
    workbook = xw.Workbook("out_pie_auto.xlsx")
    worksheet = workbook.add_worksheet()
    headings = ['Item','Percentage']
    worksheet.write_row('A1', headings) 
    i = 1
    for item in range(len(majors)):
        worksheet.write(item + 1, 0, i)
        worksheet.write(item + 1, 1, majors[item][1])
        i = i+1
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
    'name':       'Percentage',
    'categories': ['Sheet1', 1, 0, len(majors), 0],
    'values':     ['Sheet1', 1, 1, len(majors), 1],
    })
    chart1.set_title({'name': 'Resultant Pie chart'})
    chart1.set_style(10)
    worksheet.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})
    workbook.close()
