from tkinter import *
import tkinter.messagebox #ใช้ทำงานเรื่อง MS block



def _1():

    #สร้างหน้าต่าง
    root = Tk()
    root.title("Test gui")
    root.mainloop() #ลูปที่คอยระบค่าที่กด ไม่มีจะทำงานเร็วมากแล้วจบ


def _2():
    #กำหนดขนาดหน้าจอ

    root = Tk()
    root.title("Test gui")
    root.geometry("500x700+100+100") #กำนหดขนาด (ขนาด + หางจากขอบ x + ห่างบจากขอบ y(นับจากด้านบน))
    root.mainloop() #ลูปที่คอยระบค่าที่กด

def _3():
    #การแสดงผลข้อความ
    root = Tk()
    root.title("Test gui")

    MyLabel1 = Label(text="Hello World").pack() #ใส่ข้อความ 1 .pack อยู่ตรงกลาง
    MyLabel2 = Label(text="Hello World",fg="red",font=20,bg="yellow").pack() #ใส่ข้อความ 2 มีคุณสมบัติสี

    root.geometry("500x700+100+100")
    root.mainloop() 

def _4():
    #ตจัดทำแหน่งหน้าจอ
    root = Tk()
    root.title("Test gui")

    MyLabel1 = Label(text="Hello World").place(x=100,y = 100) #จัดข้อความด้วย place
    MyLabel2 = Label(text="Hello World",fg="red",font=20,bg="yellow").grid(row = 0, column= 0) #จัดด้วย Grid
    MyLabel3 = Label(text="Hello World").grid(row = 0, column = 1)

    root.geometry("500x700+100+100")
    root.mainloop() 

def _5():
    #ปุ่ม
    root = Tk()
    root.title("Test gui")

    btn1 = Button(root,text="save",fg="white",bg="green").pack()
    btn2 = Button(root,text="cancel",fg="white",bg="red").pack()
    
    root.geometry("500x700+100+100")
    root.mainloop()

def _6_1():
    root = Tk() #ถ้าอยากให้ขึ้นหน้าเดียวกันต้องไม่แยกฟังก์ชั่นแบบนี้
    Label(root,text="Hello",fg="red",font = 20,bg = "black").pack()


def _6():
    #คำสั่งในปุ่ม
    root = Tk()
    root.title("Test gui")

    btn1 = Button(root,text="Show Hello",fg="white",bg="green",command=_6_1).pack()
    
    root.geometry("500x700+100+100")
    root.mainloop()

def _7_1(txt):
    ms = txt.get()
    print(ms)

def _7():
    #กล่องข้อความ รับค่า
    root = Tk()
    root.title("Test gui")
    txt = StringVar() #เอาไว้ใช้เก็บข้อความจากกกล่องข้อความ
    My_block = Entry(root,textvariable=txt).pack() #กล่องข้อความ

    btn1 = Button(root,text="Show Hello",fg="white",bg="green",command=_7_1).pack()
    
    root.geometry("500x700+100+100")
    root.mainloop()
    #อันนี้จะทำได้ต่อเมื่อ 7 อยู่ใน main 7.1 เป็นฟังก์ชั้่น

def _8():
    #หลายหน้าจอ
    root = Tk()
    root.title("หน้าจอ 1")



    mywindow = Tk() #สามารถใส่ในฟังก์ชั่นแล้วเรียกด้วยปุ่มได้
    mywindow.title("หน้าจอ 2")


    MyLabel1 = Label(root,text="Hello World").pack()
    MyLabel2 = Label(mywindow,text="Hello World",fg="red",font=20,bg="yellow").pack()

    root.geometry("500x400")
    mywindow.geometry("500x400+100+100")
    root.mainloop()
    
def _9():
    #Menu
    root = Tk()
    root.title("My title")
    root.geometry("500x400")

    #Menu
    MyMenu = Menu()
    root.config(menu = MyMenu)

    #เพิ่ม Menu
    MyMenu.add_cascade(label="Menu 1")
    MyMenu.add_cascade(label="Menu 2")
    MyMenu.add_cascade(label="Menu 3")

    root.mainloop()

def _10():
    #Menu ย่อย
    root = Tk()
    root.title("My title")
    root.geometry("500x400")

    #Menu 
    MyMenu = Menu()
    root.config(menu = MyMenu)

    #Menu ย่อย
    menuitem = Menu()
    menuitem.add_command(label="New File")
    menuitem.add_command(label="Open")
    menuitem.add_command(label="Save")
    menuitem.add_command(label="About")
    menuitem.add_command(label="Exit")

    #เพิ่ม Menu หลัก
    MyMenu.add_cascade(label="Menu 1", menu=menuitem) #เพิ่มย่อยในหลัก
    MyMenu.add_cascade(label="Menu 2")
    MyMenu.add_cascade(label="Menu 3")

    root.mainloop()

def _11_1():
    window = Tk()
    window.title("หน้าต่างใหม่")
    window.geometry("400x500")
    window.mainloop()

def _11():
    #Menu command
    root = Tk()
    root.title("My title")
    root.geometry("500x400")

    MyMenu = Menu()
    root.config(menu = MyMenu)

    menuitem = Menu()
    menuitem.add_command(label="New Window",command = _11_1)
    menuitem.add_command(label="Open")
    menuitem.add_command(label="Save")
    menuitem.add_command(label="About")
    menuitem.add_command(label="Exit")

    MyMenu.add_cascade(label="File", menu=menuitem) #เพิ่มย่อยในหลัก
    MyMenu.add_cascade(label="Edit")
    MyMenu.add_cascade(label="View")

    root.mainloop()

def _12_1():
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรมม","By SkOT")

def _12():
    root = Tk()
    root.title("My title")
    root.geometry("500x400")

    MyMenu = Menu()
    root.config(menu = MyMenu)

    menuitem = Menu()
    menuitem.add_command(label="New Window",command = _11_1)
    menuitem.add_command(label="Open")
    menuitem.add_command(label="Save")
    menuitem.add_command(label="About",command=_12_1)
    menuitem.add_command(label="Exit")

    MyMenu.add_cascade(label="File", menu=menuitem) #เพิ่มย่อยในหลัก
    MyMenu.add_cascade(label="Edit")
    MyMenu.add_cascade(label="View")

    root.mainloop()

def _13_1():
    global root 
    confirm = tkinter.messagebox.askquestion("Yes","ต้องการออกจากโปรแกรมหรือไม่")
    if confirm == "Yes":
        root.destroy() #ทำงานได้เมื่อ 13 ไม่ใช่ฟังก์ชั่น

def _13():
    #Exit
    root = Tk()
    root.title("My title")
    root.geometry("500x400")

    MyMenu = Menu()
    root.config(menu = MyMenu)

    menuitem = Menu()
    menuitem.add_command(label="New Window",command = _11_1)
    menuitem.add_command(label="Open")
    menuitem.add_command(label="Save")
    menuitem.add_command(label="About",command=_12_1)
    menuitem.add_command(label="Exit",command=_13_1)

    MyMenu.add_cascade(label="File", menu=menuitem) #เพิ่มย่อยในหลัก
    MyMenu.add_cascade(label="Edit")
    MyMenu.add_cascade(label="View")

    root.mainloop()

def _14():
    #color choose
    pass

_6()