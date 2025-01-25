import tkinter
root = tkinter.Tk()

root.title("Calculator")
root.resizable(False, False)
root.geometry("300x400")
row = 5
column = 0
buttons = [ {"Name": "X", "Callback": lambda: print("Pressed multiply")},{"Name": "+", "Callback": lambda: print("Pressed add")},{"Name": "+", "Callback": lambda: print("Pressed add")}  ]
isFirst = True
maxOnRow = 2
onRow = 0
for i, button in enumerate(buttons):
    btn = tkinter.Button(root)
    root.grid_rowconfigure(0, minsize=50)
    btn.config(text=button["Name"],width=5,height=2, font="Arial 14 bold", command=button["Callback"])
    if isFirst:
        btn.grid(column=column, row=row, padx=25, pady=25 )
    else:
       
        btn.grid(column=column, row=row )
    onRow +=1
    if onRow == maxOnRow:
        row+=1
        column -=1
    else:
        column+=1
    
    
    
    isFirst = False

tkinter.mainloop()