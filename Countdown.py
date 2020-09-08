from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from countdown import countdown
import threading,time
from threading import Thread


running=False


class Countdown:
    def __init__(self,root):
        self.root=root
        self.root.title("countdown")
        self.root.geometry("400x200")
        self.root.resizable(0,0)
        self.root.iconbitmap("counticon.ico")

        hourss=StringVar()
        minuitess=IntVar()
        secondss=IntVar()
        txt_var=StringVar()
        txt_var.set("00:00")
        

        #=======================hower_on_button
        def on_enter1(e):
            But_start['background']="black"
            But_start['foreground']="cyan"
  
        def on_leave1(e):
            But_start['background']="SystemButtonFace"
            But_start['foreground']="SystemButtonText"

        def on_enter2(e):
            But_pause['background']="black"
            But_pause['foreground']="cyan"
  
        def on_leave2(e):
            But_pause['background']="SystemButtonFace"
            But_pause['foreground']="SystemButtonText"


        def on_enter3(e):
            But_resume['background']="black"
            But_resume['foreground']="cyan"
  
        def on_leave3(e):
            But_resume['background']="SystemButtonFace"
            But_resume['foreground']="SystemButtonText"

        def on_enter4(e):
            But_clear['background']="black"
            But_clear['foreground']="cyan"
  
        def on_leave4(e):
            But_clear['background']="SystemButtonFace"
            But_clear['foreground']="SystemButtonText"
        
        #=============================================================

        






        


        

        def run():
            
            
            cout_time=countdown(mins=minuitess.get(),secs=secondss.get())
            #txt_var.set(str(cout_time))
            
        def cnt():
            global running
            mins=minuitess.get()
            secs=secondss.get()
            t = (mins*60) + secs
            while t:
                mins, secs =divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                lab_count=Label(Frame_top,font=("times new roman",30,"bold"),fg="red",bg="black",text=str(timer))
                lab_count.place(x=140,y=10)
                time.sleep(1)
                t -= 1


        def starts():
            timer=threading.Timer(1.0,cnt)
            timer.start()
        starts()
                
       
        


        
            

        

                
                
        
        

            

            

        def pause():
            if running:
                return starts()
            But_start.config(state="disable")
            But_pause.config(state="disable")
            But_resume.config(state="normal")
            
            
            

        def resume():
            But_start.config(state="disable")
            But_pause.config(state="normal")
            But_resume.config(state="disable")

        def clear():
            But_start.config(state="normal")
            But_pause.config(state="normal")
            lab_count.config(text="00:00")
            
            Minutes_combo.set("Minutes")
            Seconds_combo.set("Seconds")
            
        
        #Frame==============================
        Main_Frame=Frame(self.root,width=400,height=200,relief=RIDGE,bd=3)
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(Main_Frame,width=395,height=80,relief=RIDGE,bg="black",bd=3)
        Frame_top.place(x=0,y=0)

        Frame_middle=Frame(Main_Frame,width=395,height=45,relief=RIDGE,bd=3,bg="#9e8ab0")
        Frame_middle.place(x=0,y=80)

        Frame_bottom=Frame(Main_Frame,width=395,height=69,relief=RIDGE,bd=3,bg="#7672cf")
        Frame_bottom.place(x=0,y=125)

        #==============================Frame_top====================================
        lab_count=Label(Frame_top,font=("times new roman",30,"bold"),fg="red",bg="black",text="00:00")
        lab_count.place(x=140,y=10)
        
        


        #===========================Frmae_bottom===============================
        But_start=Button(Frame_bottom,text="Start",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=starts)
        But_start.place(x=10,y=15)
        But_start.bind("<Enter>",on_enter1)
        But_start.bind("<Leave>",on_leave1)

        But_pause=Button(Frame_bottom,text="Pause",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=pause)
        But_pause.place(x=100,y=15)
        But_pause.bind("<Enter>",on_enter2)
        But_pause.bind("<Leave>",on_leave2)

        But_resume=Button(Frame_bottom,text="Resume",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=resume)
        But_resume.place(x=210,y=15)
        But_resume.bind("<Enter>",on_enter3)
        But_resume.bind("<Leave>",on_leave3)

        But_clear=Button(Frame_bottom,text="Clear",width=8,font=('times new roman',11,'bold'),cursor="hand2",command=clear)
        But_clear.place(x=300,y=15)
        But_clear.bind("<Enter>",on_enter4)
        But_clear.bind("<Leave>",on_leave4)

        #=====================Frame_middle+++++++++++++++++++++++++++++++++++
        #Hours_list=list(range(1,25))
        #Hours_combo=Combobox(Frame_middle,values=Hours_list,font=('arial',10),width=10,state="readonly",textvariable=hourss)
        #Hours_combo.set("Hours")
        #Hours_combo.place(x=40,y=10)

        Minutes_list=list(range(1,61))
        Minutes_combo=Combobox(Frame_middle,values=Minutes_list,font=('arial',10),width=14,state="readonly",textvariable=minuitess)
        Minutes_combo.set(0)
        Minutes_combo.place(x=25,y=10)

        Seconds_list=list(range(1,61))
        Seconds_combo=Combobox(Frame_middle,values=Seconds_list,font=('arial',10),width=14,state="readonly",textvariable=secondss)
        Seconds_combo.set(0)
        Seconds_combo.place(x=240,y=10)

        




        

if __name__ == "__main__":
    root=Tk()
    app=Countdown(root)
    root.mainloop()


##from tkinter import *
##from tkinter.ttk import *
##  
### creating tkinter window 
##root = Tk() 
##  
### Progress bar widget 
##progress = Progressbar(root, orient = HORIZONTAL, 
##              length = 100, mode = 'determinate') 
##  
### Function responsible for the updation 
### of the progress bar value 
##def bar(): 
##    import time 
##    progress['value'] = 20
##    root.update_idletasks() 
##    time.sleep(1) 
##  
##    progress['value'] = 40
##    root.update_idletasks() 
##    time.sleep(1) 
##  
##    progress['value'] = 50
##    root.update_idletasks() 
##    time.sleep(1) 
##  
##    progress['value'] = 60
##    root.update_idletasks() 
##    time.sleep(1) 
##  
##    progress['value'] = 80
##    root.update_idletasks() 
##    time.sleep(1) 
##    progress['value'] = 100
##  
##progress.pack(pady = 10) 
##  
### This button will initialize 
### the progress bar 
##Button(root, text = 'Start', command = bar).pack(pady = 10) 
##  
### infinite loop 
##mainloop() 
