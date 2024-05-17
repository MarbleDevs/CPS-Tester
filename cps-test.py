import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from time import sleep
from threading import Thread

started = False
block = False
time = 1
_passed_time = 1
clicks = 0

def cps_test():
    global clicks
    if not block:
        if started:
            clicks += 1
            cps_label.set(str(clicks))
        else:
            output_string.set("")
            passed_time.set(time)
            cps_label.set("1")
            Thread(target=cps_loop).start()
            clicks += 1

def cps_loop():
    global _passed_time, time, started, block
    started = True
    _passed_time = time

    while _passed_time != 0:
        sleep(1)
        _passed_time += -1
        passed_time.set(int(_passed_time))
    started = False
    block = True
    cps = clicks / time
    cps_label.set("Counting...")
    output_string.set(f"cps : {cps}")
    sleep(0.5)
    reset()

def reset():
    global clicks, block, started
    cps_label.set("Click here!")
    clicks = 0
    block = False
    started = False

def switch(value):
    global time
    time = value

# window
window = ttk.Window(themename = "vapor")
window.title("CPS Test")
window.geometry("500x350")

#Title
titel_string = tk.StringVar()
titel_label = ttk.Label(master = window, text = "🔥 CPS Test 🔥", font = "Calibri 24 bold")
titel_label.pack()

#Set Time
input_frame = ttk.Frame(master = window)

time1 = ttk.Button(master = input_frame, text = "1", command=lambda: switch(1))
time2 = ttk.Button(master = input_frame, text = "2", command=lambda: switch(2))
time5 = ttk.Button(master = input_frame, text = "5", command=lambda: switch(5))
time10 = ttk.Button(master = input_frame, text = "10", command=lambda: switch(10))
time30 = ttk.Button(master = input_frame, text = "30", command=lambda: switch(30))
time60 = ttk.Button(master = input_frame, text = "60", command=lambda: switch(60))
time100 = ttk.Button(master = input_frame, text = "100", command=lambda: switch(100))

time1.pack(side = "left",padx=10)
time2.pack(side = "left",padx=10)
time5.pack(side = "left",padx=10)
time10.pack(side = "left",padx=10)
time30.pack(side = "left",padx=10)
time60.pack(side = "left",padx=10)
time100.pack(side = "left",padx=10)

input_frame.pack(pady=10)

#Display time
passed_time = tk.StringVar()
passed_time.set(_passed_time)
time_label = ttk.Label(master = window, text = "0", font = "Calibri 24 bold", textvariable=passed_time)
time_label.pack()

#click box
style = ttk.Style()
style.configure("Custom.TButton", font=("Calibri", 22), width=20)

cps_label = tk.StringVar()
cps_label.set("Click here!")
cp = ttk.Button(master=window, text="CPS", command=cps_test, style="Custom.TButton", textvariable=cps_label)
cp.pack(pady=20)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "output", font = "Calibri 22", textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()
