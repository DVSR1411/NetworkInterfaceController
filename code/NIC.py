from tkinter import *
from tkinter import messagebox
import subprocess as sb
import pyuac
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
def get_interfaces():
    output = sb.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    lines = output.stdout.split("\n")
    interfaces = []
    for line in lines[3:]:
        tokens = line.split()
        if tokens:
            interfaces.append(tokens[-1])
    return interfaces
def change_interface(state):
    interface = scrollbar.get(scrollbar.curselection())
    sb.run(["netsh", "interface", "set", "interface", interface, f"admin={state}"])
    messagebox.showinfo("Result", f"Interface {interface} is {state}d")
root = Tk()
root.title("Network Interface Controller")
root.geometry("400x300")
label = Label(root, text="Select an interface and click a button to enable or disable it")
label.pack(side=TOP)
scrollbar = Listbox(root)
scrollbar.pack(side=LEFT, fill=Y)
for interface in get_interfaces():
    scrollbar.insert(END, interface)
enable_button = Button(root, text="Enable", command=lambda: change_interface("enable"))
enable_button.place(x=200, y=50)
disable_button = Button(root, text="Disable", command=lambda: change_interface("disable"))
disable_button.place(x=200, y=100)
root.mainloop()