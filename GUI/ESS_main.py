import serial
from time import sleep
from ESS_GUI_module_0 import *
from ESS_GUI_module_1 import *
from ESS_GUI_module_2 import *
from ESS_GUI_module_3 import *
from ESS_GUI_module_4 import *
from ESS_GUI_module_5 import *
from ESS_GUI_module_6 import *
from ESS_GUI_module_7 import *

import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont

# error popup box
def spectrometer_disconnect():
    root = Tk()
    root.geometry('800x480')
    root.title("ESS System Interface")
    root.configure(bg = 'sky blue')
    message = Label(root, text = 'Spectrometer Not connected, Connect and try again', bg = 'sky blue', anchor = "center").pack()
    quit_button = Button(root, text = 'QUIT', command = root.destroy, fg = 'red').pack()

def run_program():
    print("[ESS_main] run_program start")
    sleep(2.5) # wait for a little to initialize serial connection

    try:
        print("[ESS_main] Requesting module id from spectrometer")
        ser.write(b'module\n')
    except Exception as exc:
        print(f"[ESS_main] Failed to write module request: {exc}")
        raise
    # module = int(ser.readline().decode()) # read in the module number
    module = 1
    print(f"[ESS_main] Module id detected: {module}")
    root = Tk()
    print("[ESS_main] Tk root window created")
    

    if module == 0:
        print("[ESS_main] Initializing Module_0 GUI")
        app = Module_0(root)
        
    elif module == 1:
        print("[ESS_main] Initializing Module_1 GUI")
        app = Module_1(root)

    elif module == 2:
        print("[ESS_main] Initializing Module_2 GUI")
        app = Module_2(root)
        
    elif module == 3:
        print("[ESS_main] Initializing Module_3 GUI")
        app = Module_3(root)
        
    elif module == 4:
        print("[ESS_main] Initializing Module_4 GUI")
        app = Module_4(root)
        
    elif module == 5:
        print("[ESS_main] Initializing Module_5 GUI")
        app = Module_5(root)
        
    elif module == 6:
        print("[ESS_main] Initializing Module_6 GUI")
        app = Module_6(root)
        
    elif module == 7:
        print("[ESS_main] Initializing Module_7 GUI")
        app = Module_7(root)
    else:
        print(f"[ESS_main] Unsupported module id: {module}")
    
    print("[ESS_main] Entering Tk mainloop")
    root.mainloop()
    print("[ESS_main] Tk mainloop exited")
    
# open up a serial to allow for reading in of module attachment
port = "/dev/ttyUSB0"
port2 = "/dev/ttyUSB1"
run_it = 0 # handler for starting programs


try:
    print(f"[ESS_main] Attempting to open serial port {port}")
    ser = serial.Serial(port, baudrate = 115200, timeout = 3)
    run_it = 1
    print(f"[ESS_main] Serial connection established on {port}")
    run_program()
except:
    print(f"[ESS_main] Serial connection failed on {port}")
#check for spectrometer connection if it doesn work 
if run_it == 1:
    pass
else:
    try:
        print(f"[ESS_main] Attempting to open serial port {port2}")
        ser = serial.Serial(port2, baudrate = 115200, timeout =3)
        print(f"[ESS_main] Serial connection established on {port2}")
        run_program()
    except serial.serialutil.SerialException:
        print(f"[ESS_main] Unable to establish serial connection on {port2}")
        spectrometer_disconnect()

 
