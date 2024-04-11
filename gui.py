import tkinter as tk
from tkinter import ttk, filedialog, Label, Button, Tk
import subprocess


adb_download = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
zip_file = "adb.zip"
extract_folder = "adb"
adb = "./adb/platform-tools/adb"
device_folder = "device/"

#run android-file-transfer
print("slect your phone's file transfer, set your phone to file transfer mode and enable usb debug mode in developer options.")
subprocess.run(["aft-mtp-mount", device_folder])


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
    print("Select file to push")
    sendedfile = filedialog.askopenfilename(initialdir="~/")
    print("Selected file: " + sendedfile)
    putfile = filedialog.askdirectory(initialdir=device_folder)
    print("The file will be sent to: " + putfile)
    subprocess.run(["cp",  sendedfile, putfile])


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
print("Closing and unmounting device")
subprocess.run(["fusermount", "-u", "device"])
