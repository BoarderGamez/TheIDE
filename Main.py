import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
root = tk.Tk()
root.geometry("300x300")

# Config
TextAreaMainFont = ("Helvetica", 20)

# Var
SettingsWindow = None

# Functions
def FileNew():
    TextAreaMain.delete(1.0,tk.END)
def FileOpen():
    File=filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt"),("All files","*.*")])
    if File:
        with open(File, "r") as F:
            Content = F.read()
        TextAreaMain.delete(1.0,tk.END)
        TextAreaMain.insert(tk.END, Content)
def FileSave():
    File = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All files", "*.*")])
    if File:
        with open(File, "w") as F:
            F.write(TextAreaMain.get(1.0,tk.END))
def FileExit():
    ExitConfirmation = messagebox.askyesno("Confirm Exit", "Do you want to exit?")

    if ExitConfirmation:
        root.destroy()
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
    TextAreaMain.event_generate("<<Undo>>")
def EditRedo():
    TextAreaMain.event_generate("<<Redo>>")
def EditCut():
    TextAreaMain.event_generate("<<Cut>>")
def EditCopy():
    TextAreaMain.event_generate("<<Copy>>")
def EditPaste():
    TextAreaMain.event_generate("<<Paste>>")

# Full Menu bar
MenuBar=tk.Menu(root)
root.config(menu=MenuBar)
#Frame
TextAMainFrame = ttk.Frame(root)
TextAMainFrame.pack(expand=True, fill = tk.BOTH)
#ScrollBar
ScrollbarMainRight = ttk.Scrollbar(TextAMainFrame, orient="vertical")
ScrollbarMainRight.pack(side=tk.RIGHT,fill=tk.Y)
#Text area
TextAreaMain = tk.Text(TextAMainFrame, wrap=tk.WORD, font=TextAreaMainFont, undo=True, yscrollcommand=ScrollbarMainRight.set)
TextAreaMain.pack(side=tk.LEFT, expand=True,fill=tk.BOTH)
ScrollbarMainRight.config(command=TextAreaMain.yview)
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