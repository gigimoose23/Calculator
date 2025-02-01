import tkinter
root = tkinter.Tk()

root.title("Calculator")
root.resizable(False, False)
userEntryVar = tkinter.IntVar()
userEntryVar.set(0)
userEntry = tkinter.Entry(root)
userEntry.config(textvariable=userEntryVar, font="Arial 15", state="readonly")

userEntry.place(x=0, y=0, width=220, height=48)
root.geometry("220x200")
row = 5
column = 0

buttons = [ {"Name": "x", "Callback":
#multiply
 lambda: print("Pressed multiply")
 },{"Name": "+", "Callback":
 
 #add
 lambda: print("Pressed add")
 },{"Name": "÷", "Callback": 

#divide
 lambda: print("Pressed divide")
 },{"Name": "-", "Callback":


 lambda: print("Pressed subtract")
 }]
isFirst = True
maxOnRow = 2
onRow = 0
for i, button in enumerate(buttons):
    btn = tkinter.Button(root)
    root.grid_rowconfigure(0, minsize=50)
    btn.config(text=button["Name"],width=2,height=1, font="Arial 14 bold", command=button["Callback"])
    if isFirst:
        btn.grid(column=column, row=row )
    else:
       
        btn.grid(column=column, row=row )
    onRow +=1
    if onRow == maxOnRow:
        row+=1
        column -=1
    else:
        column+=1
    
    
    
    isFirst = False

isFirstN = True
maxOnRowN = 3
onRowN = 0
rowN = 5
columnN = 7
def hi(e):
    print(e)
for i in range(10):
    btn = tkinter.Button(root)
    root.grid_rowconfigure(0, minsize=50)
    root.grid_columnconfigure(3, minsize=50)
    m = i
    btn.config(text=m,width=2,height=1, font="Arial 14 bold")
    btn.config( command=lambda: hi(btn.configure()["text"]) )
    
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