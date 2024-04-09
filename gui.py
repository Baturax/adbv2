import tkinter as tk
import subprocess

#const
adb_download = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
zip_file = "adb.zip"
extract_folder = "adbb"


#def
def download_adb():
    # Dosyayı indirme
    download_process = subprocess.Popen(["./wget", "-N", adb_download, "-O", zip_file])
    download_process.communicate() 
    
    if download_process.returncode == 0:
        unzip_process = subprocess.Popen(["unzip", "-o", zip_file, "-d", extract_folder])
        unzip_process.communicate()
        print("downloaded successfully")
        subprocess.run(["rm", zip_file])

#tkinter
main = tk.Tk()

button = tk.Button(main, text="Download ADB", bg="white", fg="#282C34", command=download_adb)
button.pack()

# configs
main.tk_setPalette("#282C34")
main.mainloop()
