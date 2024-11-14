from time import sleep
import tkinter
import customtkinter as ctk
from pytubefix import YouTube
from CTkMessagebox import CTkMessagebox

def show_info(messsage:str):
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message=messsage,icon="check")
    
def show_error(messsage:str):
    # Show some error message
    CTkMessagebox(title="Error", message=messsage, icon="cancel")
    
def on_progress(stream:any,chunk:bytes, bytes_remaining:int):
    total= stream.filesize
    bytes_downloaded= total -bytes_remaining
    percentage= bytes_downloaded/total *100
    per=str(int(percentage))
    prgbar.set(float(percentage)/100)
    prgbar.update()
    
def startDownload():
    try:
        prgbar.configure(width=400,height=10)
        prgbar.update()
        lnk=link.get()
        ytObject= YouTube(lnk,on_progress_callback=on_progress)
        audio= ytObject.streams.get_audio_only()
        sleep(5)
        audio.download()
        show_info("Download successfull")
    except Exception as e:
        show_error("Error downloading")
        print("An error occurred:", e)
    finally:
        prgbar.configure(width=0,height=0)
        prgbar.update()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app= ctk.CTk()
app.geometry("520x300")
app.title("Youtube downloader")

label=ctk.CTkLabel(app,text="Insert the youtube link")
label.pack(padx=20,pady=10)

url_var=tkinter.StringVar()
link=ctk.CTkEntry(app,width=350, height=40,textvariable=url_var)
link.pack()

btn= ctk.CTkButton(app,text="Download", command=startDownload)
btn.pack(padx=10,pady=10)

prgbar= ctk.CTkProgressBar(app,width=0, height=0)
prgbar.set(0)
prgbar.pack(padx=10, pady=10)


app.mainloop()
