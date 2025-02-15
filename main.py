import tkinter
import tkinter.messagebox
root = tkinter.Tk()

root.title("Calculator")
root.resizable(False, False)
userEntryVar = tkinter.StringVar()
userEntryVar.set("")
userEntry = tkinter.Entry(root)
userEntry.config(textvariable=userEntryVar, font="Arial 15", state="readonly")

userEntry.place(x=0, y=0, width=253, height=48)
root.geometry("253x200")
row = 5
column = 0

def me():
    try:
        userEntryVar.set(eval(doProc(userEntryVar.get())))
    except Exception as e:
        tkinter.messagebox.showerror("Error", e)

def doProc(s):
    x = s.replace(" ", "")
    y = x.replace("÷", "/")
    z = y.replace("x", "*")
    return z

buttons = [ {"Name": "x", "Callback":
#multiply
 lambda: addNum(" x ")
 },{"Name": "+", "Callback":
 
 #add
 lambda: addNum(" + ")
 },{"Name": "÷", "Callback": 

#divide
 lambda: addNum(" ÷ ")
 },{"Name": "-", "Callback":

    #subtract
 lambda: addNum(" - ")
 }, {"Name": "=", "Callback":

    #eval
 lambda: me(),
 }, {"Name": "C", "Callback":
     
 lambda: userEntryVar.set(""),
 
 }]
isFirst = True
maxOnRow = 3
onRow = 0
#symbols
for i, button in enumerate(buttons):
    btn = tkinter.Button(root)
    root.grid_rowconfigure(0, minsize=50) 
    btn.config(text=button["Name"],width=2,height=1, font="Arial 14 bold", command=button["Callback"])
    btn.grid(column=column, row=row )
        
    onRow +=1
    if onRow == maxOnRow:
        onRow = 0
        column = 0
        row+=1
    else:
        column+=1
    
    
    
    isFirst = False

isFirstN = True
maxOnRowN = 3
onRowN = 0
rowN = 5
columnN = 7
def addNum(e):
    userEntryVar.set(str(userEntryVar.get()) + str(e))
for i in range(10):
    btn = tkinter.Button(root)
    root.grid_rowconfigure(0, minsize=50)
    root.grid_columnconfigure(3, minsize=50)
    m = i
    btn.config(text=m,width=2,height=1, font="Arial 14 bold")
    btn.config( command=lambda m=m: addNum(m))
    
    btn.grid(column=columnN, row=rowN )
       
        
    onRowN +=1
    if onRowN == maxOnRowN:
        onRowN = 0
        
        
       
        rowN+=1
        columnN = 7
    else:
        #rowN+=1
        columnN+=1
    
    
    
  

tkinter.mainloop()