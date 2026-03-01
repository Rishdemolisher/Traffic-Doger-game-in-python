from tkinter import *
import tkinter as tk
import subprocess
import pygame
root=tk.Tk()
canvas = Canvas(root, width=730, height=400)
canvas.pack()
def run_script():
    subprocess.Popen(["python","Traffic Dodger.py"])
image=tk.PhotoImage(file='login page photo.png',width=800,height=600)
label=tk.Label(root,image=image)
label.pack()
label.place(x=0,y=0)
button=tk.Button(root, text="Play Game",width=20,height=1, bg='red',command=run_script)
button.pack()
button.place(x=300,y=250)
exit_button=tk.Button(root,text='Exit',width=20,height=1,bg='red', command=root.destroy)
exit_button.pack()
exit_button.place(x=300,y=300)

# Initialize Pygame
pygame.mixer.init()

# Load Music File
pygame.mixer.music.load("stylish-rock-beat-trailer.mp3")

# Play Music Button
play_button = tk.Button(root, text="Play music", command=pygame.mixer.music.play)
play_button.pack(side=tk.LEFT)
# Stop Music Button
stop_button = tk.Button(root, text="Stop music", command=pygame.mixer.music.stop)
stop_button.pack(side=tk.LEFT)

# Mainloop
root.mainloop()
