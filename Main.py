import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
import os
import configparser
import subprocess
# NEEDS INSTALL
import ttkthemes
root = tk.Tk()
root.geometry("300x300")
config = configparser.ConfigParser()
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
        with open(File, "r") as F:
            Content = F.read()
        TextAreaMain.delete(1.0,tk.END)
        TextAreaMain.insert(tk.END, Content)
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
def FileSettings():
    global SettingsWindow
    global FontOptions
    global SelectedFont
    global SettingsFontDropdown
    FontOptions = ["Arial",
                   "Calibri",
                   "Verdana",
                   "Roman",
                   "TINspireKeys",
                   "TINspireKeysCX",
                   "System",
                   "Terminal",
                   "Fixedsys",
                   "Modern",
                   "Roman Script",
                   "Courier",
                   "MS Serif",
                   "MS Sans Serif",
                   "Small Font Marlett",
                   "Arial",
                   "Arabic Transparent",
                   "Arial Baltic",
                   "Arial CYR",
                   "Arial Greek",
                   "Arial TUR",
                   "Arial Black",
                   "Bahnschrift SemiBold",
                   "Bahnschrift Light SemiCondensed",
                   "Bahnschrift SemiLight SemiCondensed",
                   "Bahnschrift SemiCondensed",
                   "Bahnschrift Semibold",
                   "Bahnschrift SemiBold Condensed",
                   "Malgun Gothic",
                   "Microsoft Yi Baiti",
                   "Mingliu-ExtB",
                   "MingLiU_HKSCS-ExtB",
                   "Times New Roman",
                   "Sitka Banner",
                   "Segoe UI",
                   "Nirmala UI",
                   "Nirmala UI Semilight",
                   "Yu Gothic Medium",
                   "Gabriola",
                   "Myanmar Text",
                   "Nirmala UI",
                   "Nirmala UI Semilight",
                   "Microsoft Yahei Light",
                   "MS PGothic",
                   "Sgoe UI",
                   "SimSun",
                   "Yu Gothic Medium",
                   "Yu Gothic",
                   "Yu GothicUI",
                   "Sylfaen",
                   "Symbol",
                   "Cascadia Mono SemiBold",
                   "Cascadia Mono,"
                   "Cascadia Mono SemiLight",
                   "Cascadia Mono Light,"
                   "Cascadia Mono ExtraLight",
                   "Cascadia Code SemiBold",
                   "Cascadia Code",
                   "TINspireKeysChinese",
                   "Glass Gauge T182T",
                   "SimSun-ExtB",
                   "Cambria Math",
                   "Courier new CE"]
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
    pass

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
LoadConfig()
fetchfont = config["General"].get("Current_Font","Arial")
font = (fetchfont,13)
TextAreaMain = tk.Text(TextAMainFrame, wrap=tk.WORD, font=font, undo=True, yscrollcommand=ScrollbarMainRight.set)
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
root.mainloop()

