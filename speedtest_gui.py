import speedtest
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()              
root.geometry("400x400")
root.title("Speedtest")
root.configure(bg="black")
font=("Arial",15,"bold")
font_cek_kecepatan = ("Vendara",15,"bold")

def check():
    messagebox.showinfo("Sedang berjalan","Tunggu")
    d.configure(text=str(st.download()//10**6)+" Mbps")
    u.configure(text=str(st.upload()//10**6)+" Mbps")
    p.configure(text=str(int(st.results.ping))+" MS")
    l.configure(text="Speedtest complete")

dspeed = tk.Label(root,text="Download speed:",bg="black",fg="yellow",font=font)
dspeed.place(x=10,y=10)
d = tk.Label(root,text="0 Mbps",bg="black",fg="yellow",font=font)
d.place(x=250,y=10)

uspeed = tk.Label(root,text="Upload speed:",bg="black",fg="yellow",font=font)
uspeed.place(x=10,y=50)
u = tk.Label(root,text="0 Mbps",bg="black",fg="yellow",font=font)
u.place(x=250,y=50)

ping = tk.Label(root,text="Ping:",bg="black",fg="yellow",font=font)
ping.place(x=10,y=90)
p = tk.Label(root,text="0 Ms",bg="black",fg="yellow",font=font)
p.place(x=250,y=90)

l = tk.Label(root,text="Klik disini untuk cek kecepatan",bg="black",fg="yellow",font=font_cek_kecepatan)
l.place(x=50,y=250)

b = tk.Button(root,text="Speed test",command=check,bg="yellow",fg="black",font=font_cek_kecepatan)
b.place(x=50,y=300,height=40,width=300)
root.mainloop()



