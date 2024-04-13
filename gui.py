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
def push ():
    print("Select file to push")
    pushedfile = filedialog.askopenfilename(initialdir="~/")
    print("Selected file: " + pushedfile)
    wherepushed = filedialog.askdirectory(initialdir=device_folder)
    print("The file will be pushed to: " + wherepushed)
    subprocess.run(["cp",  pushedfile, wherepushed])
#adb pull
def pull():
    print("Select file to pull")
    pulledfile = filedialog.askopenfilename(initialdir=device_folder)
    print("Selected file: " + pulledfile)
    wherepulled = filedialog.askdirectory(initialdir="~/")
    print("The file will be pulled to: " + wherepulled)
    subprocess.run(["cp",  pulledfile, wherepulled])

#adb reboot
def rebootdevice():
    subprocess.run([adb, "reboot"])
def rebootrecovery():
    subprocess.run([adb, "reboot", "recovery"])
def rebootbootloader():
    subprocess.run([adb, "reboot", "bootloader"])



#"tkinter"
root = Tk()


# This is the section of code which creates the main window
root.geometry('700x500')
root.configure(background='#8B4513')
root.title('ADB Tools')

Label(root, text='ADB Tools', bg='#8B4513', font=('arial', 14, 'normal')).place(x=2, y=5)

Button(root, text='ADB Devices', bg='#FFFFFF', font=('arial', 12, 'normal'), command=adb_devices).place(x=2, y=40)

Button(root, text='ADB Push', bg='#FFFFFF',font=('arial', 12, 'normal'), command=push).place(x=2, y=75)

Button(root, text='ADB Pull', bg='#FFFFFF', font=('arial', 12, 'normal'), command=pull).place(x=2, y=110)

#yok
Label(root, text='ADB Download', bg='#8B4513', font=('arial', 14, 'normal')).place(x=2, y=160)

Button(root, text='Restart Device', bg='#FFFFFF', font=('arial', 12, 'normal'), command=rebootdevice).place(x=2, y=195)

Button(root, text='Reboot Recovery', bg='#FFFFFF', font=('arial', 12, 'normal'), command=rebootrecovery).place(x=2, y=230)

Button(root, text='Reboot Bootloader', bg='#FFFFFF', font=('arial', 12, 'normal'), command=rebootbootloader).place(x=2, y=265)


Button(root, text='Download ADB', bg='#FFFFFF', font=('arial', 12, 'normal'), command=download_adb).place(x=550, y=5)

root.mainloop()
print("Closing and unmounting device")
subprocess.run(["fusermount", "-u", "device"])
print("Unmounted device")