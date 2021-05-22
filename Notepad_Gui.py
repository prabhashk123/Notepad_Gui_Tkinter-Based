"""tut-28 Gui Based notepad"""
from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file#file ko global bana deta  or niche wala file ko used kr sakte h
    root.title("Untitled-Notepad")
    file=None
    Textarea.delete(1.0,END)# first line zeroth character mins sara hata do

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file==(""):
        file=None
    else:
        #here -notepad mins ki title change hoga and os module import
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",
                           filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
        #Save as new file
            f=open(file,'w')
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
    #save the  file mins old file save
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()

def quitApps():
    root.destroy()

def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Prabhash")

if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.geometry("644x700")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("Notepad_icon.png")

    #Add Textarea
    Textarea=Text(root,font="lucida 13")
    file=None #Becasue hamne koe file nhi khola hai
    Textarea.pack(expand=True,fill=BOTH)

    #Create menubar in notepad
    MenuBar=Menu(root)

    #Filemenu start
    FileMenu=Menu(MenuBar,tearoff=0)
    #To Open New File
    FileMenu.add_command(label="New",command=newFile,font="lucida 10 ")
    FileMenu.add_command(label="Open",command=openFile,font="lucida 10 ")
    #To Open Allready Exitising File
    FileMenu.add_command(label="Save",command=saveFile,font="lucida 10 ")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApps,font="lucida 10 ")
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #File menu ends h

    #Edit Menu starts here
    EditMenu=Menu(root,tearoff=0)
    #Feature of copy cut and paste
    EditMenu.add_command(label="Cut",command=cut,font="lucida 10 ")
    EditMenu.add_command(label="Copy",command=copy,font="lucida 10 ")
    EditMenu.add_command(label="Paste",command=paste,font="lucida 10 ")

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    #Edit menu ends here

    #Help menu start here
    HelpMenu=Menu(root,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about,font="lucida 10 ")

    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    #Help menu ends here
    root.config(menu=MenuBar)

    #Adding scrollbar
    Scroll=Scrollbar(Textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()