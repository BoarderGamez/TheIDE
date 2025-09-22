import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
import os
import configparser
import subprocess
from tkinter.constants import NORMAL

# NEEDS INSTALL
# import ttkthemes
root = tk.Tk()
root.geometry("600x300")
config = configparser.ConfigParser()
CurrentFile=None
# Config
def ConfigCreate():
    global config


    config['General'] = {"Current_Font":'Arial'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
# if __name__ == "__main__":
#     ConfigCreate()
TextAreaMainFont = ("Helvetica", 13)
def LoadConfig():
    global config
    config = configparser.ConfigParser()
    if os.path.exists("config.ini"):
        config.read("config.ini")
    else:
        ConfigCreate()
        config.read("config.ini")
# Var
SettingsWindow = None

# Functions
def FileNew():
    TextAreaMain.delete(1.0,tk.END)
def FileOpen():
    global CurrentFile
    File=filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files","*.py"),("All files","*.*")])
    if File:
        CurrentFile = File
        try:
            with open(File, "r") as F:
                Content = F.read()
            TextAreaMain.config(state="normal")
            TextAreaMain.delete(1.0,tk.END)
            TextAreaMain.insert(tk.END, Content)
            TextAreaMain.edit_reset()
        except Exception as e:
            messagebox.showerror("Error", f"couldn't open file whomp whomp:\n{e}")
def FileSave():
    global CurrentFile
    if CurrentFile:
        with open(CurrentFile, "w") as F:
            F.write(TextAreaMain.get(1.0,tk.END))
    else:
        FileSaveAs()
def FileSaveAs():
    global CurrentFile
    File = filedialog.asksaveasfilename(defaultextension=".py",filetypes=[("Python Files", ".py"),("All files","*.*")])
    if File:
        CurrentFile = File
        with open(File, "w") as F:
            F.write(TextAreaMain.get(1.0,tk.END))
def FileExit():
    ExitConfirmation = messagebox.askyesno("Confirm Exit", "Do you want to exit?")
    if ExitConfirmation:
        root.destroy()
def ConfirmButtonSettings():
    SelectedFont = SettingsFontDropdown.get()
    FontSize = 13
    font = (SelectedFont, FontSize)
    TextAreaMain.config(font=font)
    config["General"]["Current_Font"] = SelectedFont
    with open("config.ini", "w") as configfile:
        config.write(configfile)
    SettingsWindow.destroy()
def TabThingy(event):
    TextAreaMain.insert(tk.INSERT," "*4)
    return "brek"
def Enterkeylinethingy(event):
    lineindex = TextAreaMain.index("insert linestart")
    linetext = TextAreaMain.get(lineindex,lineindex + "lineend")
    indent = len(linetext)- len(linetext.lstrip(" "))
    TextAreaMain.insert(tk.INSERT, "\n"+" " * indent)
    if linetext.strip().endswith(":"):
        TextAreaMain.insert(tk.INSERT," "*4)
    return "break"
def FileSettings():
    global SettingsWindow
    global FontOptions
    global SelectedFont
    global SettingsFontDropdown
    FontOptions = list(tkFont.families())
    if SettingsWindow and SettingsWindow.winfo_exists():
        SettingsWindow.lift()
        return
    SettingsWindow=tk.Toplevel(root)
    SettingsWindow.title("Settings")
    SettingsWindow.geometry("300x300")
    SettingsWindow.resizable(False, False)
    SettingsWindowTopLabelFrame = ttk.LabelFrame(SettingsWindow,text="Appearance Settings")
    SettingsWindowTopLabelFrame.grid(column=0, row=0)
    SettingsFontLabel = ttk.Label(SettingsWindowTopLabelFrame, text="Font")
    SettingsFontLabel.grid(row=0,column=0)
    SettingsFontDropdown = ttk.Combobox(SettingsWindowTopLabelFrame, values=FontOptions, state="readonly")
    SettingsFontDropdown.grid(row=0,column=1)
    SettingsFontDropdown.set("Arial")
    SettingsConfirmButton = ttk.Button(SettingsWindow, text="Confirm",command=ConfirmButtonSettings)
    SettingsConfirmButton.grid(row=1,column=0)
    SelectedFont = SettingsFontDropdown.get()
def FetchFont():
    global font
    print("there is literally no way you couldve found this like literally im so close to getting to 5h in siege week one theres no way Ill be motivated enough for siege week real"
          "aaaaaah"
          "AAAAAaH"
          "SAVE ME")
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
def RunRun():
    global CurrentFile
    if not CurrentFile:
        messagebox.showerror("Error","Please save file before running")
        return
    FileSave()
    OutputWindow =tk.Toplevel(root)
    OutputWindow.title(f"Output - {os.path.basename(CurrentFile)}")
    OutputWindow.geometry("500x300")
    OutputFrame = ttk.Frame(OutputWindow)
    OutputFrame.pack(expand=True, fill =tk.BOTH)
    OutputScrollbar = ttk.Scrollbar(OutputFrame, orient="vertical")
    OutputScrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    fetchfont = config["General"].get("Current_Font", "Arial")
    currentfont = (fetchfont, 13)
    OutputText = tk.Text(OutputFrame,wrap = tk.WORD,font=currentfont,yscrollcommand=OutputScrollbar.set,state=NORMAL)
    OutputText.pack(side=tk.LEFT,expand=True,fill =tk.BOTH)
    OutputScrollbar.config(command=OutputText.yview)

    try:
        precess = subprocess.Popen(["python", CurrentFile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout,stderr=precess.communicate()
        if stdout:
            OutputText.insert(tk.END,stdout)
        if stderr:
            OutputText.insert(tk.END,stderr)
    except Exception as e:
        messagebox.showerror("Run Error (make sure python is added to PATH)",str(e))
def LineUpdate(event=None):
    line, col = TextAreaMain.index(tk.INSERT).split(".")
    linelabel.config(text=f"Line: {line}")
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=0)
root.columnconfigure(0,weight=1)

LoadConfig()
fetchfont = config["General"].get("Current_Font","Arial")
currentfont = (fetchfont,13)
# Full Menu bar
MenuBar=tk.Menu(root)
root.config(menu=MenuBar)
#Frame
TextAMainFrame = ttk.Frame(root)
TextAMainFrame.grid(row=0 ,column=0,sticky="nsew")
#ScrollBar
ScrollbarMainRight = ttk.Scrollbar(TextAMainFrame, orient="vertical")
ScrollbarMainRight.pack(side=tk.RIGHT,fill=tk.Y)
#listbox
ListBoxFileName = tk.Listbox(TextAMainFrame, highlightcolor="black", highlightthickness=1, selectmode=tk.SINGLE, font=currentfont)

ListBoxFileName.pack(side=tk.LEFT,fill=tk.Y)
#Text area

TextAreaMain = tk.Text(TextAMainFrame, wrap=tk.WORD, font=currentfont, undo=True, yscrollcommand=ScrollbarMainRight.set)
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

RunMenu = tk.Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Run", menu=RunMenu)
RunMenu.add_command(label="Run", command=RunRun)
belowframe = ttk.Frame(root)
belowframe.grid(row=1, column=0,sticky="ew")
linelabel = ttk.Label(belowframe,text="Line:0")
linelabel.pack(side=tk.RIGHT,padx=5)
#binds
# TextAreaMain.bind("<Tab>", TabThingy)
TextAreaMain.bind("<Return>", Enterkeylinethingy)
TextAreaMain.bind("<KeyRelease>",LineUpdate)
TextAreaMain.bind("<ButtonRelease>",LineUpdate())
root.mainloop()




