from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import pygame as pg
from tkinter.messagebox import showerror, showwarning, showinfo

#Function to always clear the page and remove all widgets
def clear_page(root):
    for widget in root.winfo_children():
        widget.destroy()

#Definition to check the health of the plants
def health(root):
    #Create a new window
    root = tk.Tk()
    root.title('PlantyPoppins Health Check')
    root.resizable(False,False)
    root.geometry('500x300')

    #First option to evaluate the plants health
    ttk.Button(root,
            text='The leaves, I must say, have developed quite the curious brown spots...',
            command=lambda: showerror(
            title='S.O.S',
            message="It appears your plant is in need of some nourishment. Do use a fertilizer, if you please!") #This message appears on the screen
            ).place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    #Second option to evaluate the plants health
    ttk.Button(root,
            text="The leaves are green. The plant is reaching towards the sun",
            command=lambda: showinfo(
            title='Good job!',
            message='Keep taking good take of your plant!') #This message appears on the screen
            ).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #Third option to evaluate the plants health
    ttk.Button(root,
                text='Oh dear, the leaves have yellow spots and are curling',
                command=lambda: showinfo(
                title='Warning',
                message="Your plant is quite thirsty. Please give it a good drink!") #This message appears on the screen
               ).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

#Definiton for the Water Function
def water(root):
    global pb
    #Create a new window
    root = tk.Tk()
    root.geometry('350x300')
    root.title("Grab a can and water the plant")

    #Initialize pygame for the music
    pg.init()
    pg.mixer.music.load("music/Supercalifragilisticexpialidocious.mp3")

    #Initialize the Progressbar
    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='indeterminate',
        length=250
    )
    pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

    #Start button
    start_button = ttk.Button(root,
                              text='Watering now',
                              command=lambda: start_watering(pb)
                              )
    start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

    #Stop button
    stop_button = ttk.Button(root,
                             text='Done watering',
                             command=lambda: stop_progress()
                             )
    stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

#Definitions for the Water-Buttons
#Definiton for the Start-Button
def start_watering(pb):
    # Start the progress bar
    pb.start()
    # Start playing the music
    pg.mixer.music.play()

#Definition for the Stop-Button
def stop_progress():
    global pb
    #When the User clicks on "Done watering", the Progress bar stops moving and the Music stops playing
    if pb:
        pb.stop()
    pg.mixer.music.stop()

    #The message box appears which complements the User for taking care of his plant
    messagebox.showinfo("Watering Completed", "You've watered your plant. Good job!")