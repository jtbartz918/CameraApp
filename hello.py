import numpy as np
import cv2
import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Danfoss Camera App")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=10, height=10)
imageFrame.grid(row=0, column=0, padx=0, pady=0)
e = tk.Entry(window)

#Capture video frames
path = ""
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
# ret0, img0 = cap0.read()
# img1 = cv2.resize(img0,(800,800))
# ret1, img1 = cap1.read()
# img2 = cv2.resize(img1,(800,800))
# ret2, img2 = cap2.read()
# img3 = cv2.resize(img2,(800,800))
def show_frame():
    _, frame0 = cap0.read()
    _, frame1 = cap1.read()
    _, frame2 = cap2.read()
    # frame0 = cv2.flip(frame0, 1)
    #frame1 = cv2.flip(frame1, 2)
    # frame2 = cv2.flip(frame2, 3)
    cv2image0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGBA)
    cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
    cv2image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
    img0 = Image.fromarray(cv2image0)
    img1 = Image.fromarray(cv2image1)
    img2 = Image.fromarray(cv2image2)
    imgtk0 = ImageTk.PhotoImage(image=img0)
    imgtk1 = ImageTk.PhotoImage(image=img1)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    display1.imgtk = imgtk0 #Shows frame for display 1
    display1.configure(image=imgtk0)
    display2.imgtk = imgtk1 #Shows frame for display 2
    display2.configure(image=imgtk1)
    #display3.imgtk = imgtk2 #Shows frame for display 2
    #display3.configure(image=imgtk2)
    window.after(10, show_frame)

def saveImg():
    global path
    _, frame0 = cap1.read()
    _, frame1 = cap2.read()
    _, frame2 = cap3.read()
    _, frame3 = cap4.read()
    _, frame4 = cap5.read()
    #print("Writing pictures to " + path)
    try:
        cv2.imwrite(path+"/ftest0.png",frame0)
        cv2.imwrite(path+"/ftest1.png",frame1)
        cv2.imwrite(path+"/ftest2.png",frame2)
        cv2.imwrite(path+"/ftest1.png",frame3)
        cv2.imwrite(path+"/ftest2.png",frame4)
        print("images taken succesfully, please scan next barcode")
    except:
        print("error saving pictures, please contact IT")
    
        
        
    scan()




#button1 = tk.Button(compount=bottom, text ="Hello", command = saveImg)

display1 = tk.Label(imageFrame)
display1.grid(row=0, column=0)  #Display 1
display2 = tk.Label(imageFrame)
display2.grid(row=0, column=1) #Display 2
#display3 = tk.Label(imageFrame)
#display3.grid(row=0, column=2) #Display 3

def scan():
    global path
    print("Scan barcode")
    scanned = input()
    path = "C:/Users/u333271/Desktop/" + scanned
    try:
        os.mkdir(path)

    except Exception as e:
        print ("Creation of the directory %s failed" % path)

    else:
        print ("Successfully created the directory %s " % path)
#Slider window (slider controls stage position)
button1 = tk.Button(imageFrame, text="Take Pictures", fg="red", command=saveImg, height = 20, width = 30)
button1.grid(row=1, column=0)
e.grid(row=2, column=0)

s = e.get()
def scan2():
    global path
    print("Scan barcode")
    scanned = input()
    path = "C:/Users/u333271/Desktop/" + scanned
    try:
        os.mkdir(path)

    except Exception as e:
        print ("Creation of the directory %s failed" % path)

    else:
        print ("Successfully created the directory %s " % path)



try:
    show_frame() #Display
    scan2()
except:
    print("An error occured please contact IT")
window.mainloop()  #Starts GUI
