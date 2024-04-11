import tkinter as tk
from tkinter import ttk, filedialog, Label, Button, Tk
import subprocess

#const
adb_download = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
zip_file = "adb.zip"
extract_folder = "adb"
adb = "./adb/platform-tools/adb"

#def

#downlaod adb
def download_adb():
    # Dosyayı indirme
    download_process = subprocess.Popen(["wget", "-N", adb_download, "-O", zip_file])
    download_process.communicate() 
    
    if download_process.returncode == 0:
        unzip_process = subprocess.Popen(["unzip", "-o", zip_file, "-d", extract_folder])
        unzip_process.communicate()
        print("downloaded successfully")
        subprocess.run(["rm", zip_file])


#adb tools
#adb devices
def adb_devices():
    subprocess.run([adb, "devices"])
#adb push
def adb_push ():
    filename = filedialog.askopenfilename()


#"tkinter"
root = Tk()


# This is the section of code which creates the main window
root.geometry('632x295')
root.configure(background='#8B4513')
root.title('ADB Tools')

Label(root, text='ADB Tools', bg='#8B4513', font=('arial', 14, 'normal')).place(x=2, y=5)

Button(root, text='ADB Devices', bg='#FFFFFF', font=('arial', 12, 'normal'), command=adb_devices).place(x=2, y=40)

Button(root, text='ADB Push', bg='#FFFFFF',font=('arial', 12, 'normal'), command=adb_push).place(x=2, y=75)

Button(root, text='Download ADB', bg='#FFFFFF', font=('arial', 12, 'normal'), command=download_adb).place(x=502, y=5)

root.mainloop()