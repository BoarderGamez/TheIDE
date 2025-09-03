import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("300x300")

# Config
TextAreaMainFont = ("Helvetica", 20)

# Var
SettingsWindow = None

# Functions
def FileNew():
    pass
def FileOpen():
    pass
def FileSave():
    pass
def FileExit():
    pass
def FileSettings():
    global SettingsWindow
    if SettingsWindow and SettingsWindow.winfo_exists():
        SettingsWindow.lift()
        return
    SettingsWindow=tk.Toplevel(root)
    SettingsWindow.title("Settings")
    SettingsWindow.geometry("300x300")
    SettingsWindow.resizable(False, False)

def EditUndo():
    pass
def EditRedo():
    pass
def EditCut():
    pass
def EditCopy():
    pass
def EditPaste():
    pass

# Full Menu bar
MenuBar=tk.Menu(root)
root.config(menu=MenuBar)

#Text area
TextAreaMain = tk.Text(root,wrap=tk.WORD,font=TextAreaMainFont)
TextAreaMain.pack(expand=True,fill=tk.BOTH)
# File Menu
FileMenu=tk.Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=FileNew )
FileMenu.add_command(label="Open", command=FileOpen)
FileMenu.add_command(label="Save", command=FileSave)
FileMenu.add_command(label="Exit", command=FileExit)
FileMenu.add_command(label="Settings", command=FileSettings)
# Edit Menu
EditMenu=tk.Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Undo", command=EditUndo)
EditMenu.add_command(label="Redo", command=EditRedo)
EditMenu.add_command(label="Cut", command=EditCut)
EditMenu.add_command(label="Copy", command=EditCopy)
EditMenu.add_command(label="Paste", command=EditPaste)
root.mainloop()