import tkinter as tk
from test.nw_map_test_data import init_nw_map
from tkinter import *

from network_map import Port, Switch

color = "#eff5f6"
ip_color = "#F5E1FD"
PADDING = 20


class PortFrame(tk.Frame):
    def __init__(self, root: Frame, port: Port):
        tk.Frame.__init__(self, root)
        self.port = port

        port_label = tk.Label(root, text=port.name, bg=color)
        port_label.pack()

        self.hover_text = tk.Label(root, text="", bg="brown")
        self.hover_text.pack(fill="x")
        self.hover_text.lift()

        port_label.bind("<Enter>", self.on_enter)
        port_label.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        if conn := self.port.connection:
            self.hover_text.configure(text=f"Connect to {conn}")

    def on_leave(self, enter):
        self.hover_text.configure(text="")


class SwitchFrame(tk.Frame):
    def __init__(self, root: tk.Tk, switch: Switch):
        tk.Frame.__init__(self, root)
        self.name_label = tk.Label(root, text=switch.name, bg=ip_color)
        self.name_label.pack(fill="x")
        self.ip_label = tk.Label(root, text=switch.ip_address, bg=ip_color)
        self.ip_label.pack(fill="x")

        for port in switch.ports:
            main_port_frame = Frame(root, bg="brown", width=200, height=50)
            PortFrame(main_port_frame, port)
            main_port_frame.pack(pady=PADDING / 2)
            main_port_frame.pack_propagate(False)


class BTNFrame(tk.Frame):
    def __init__(self, root: tk.Tk):

        self.btn = tk.Button(root, text="QUIT", command=root.destroy)
        self.btn.pack(side=tk.TOP)


class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Topology GUI")
        self.geometry("750x550")
        self.resizable(True, True)
        nw_map = init_nw_map()

        for switch in nw_map.switches:
            main_frame = tk.Frame(self, borderwidth=5, bg="brown")
            SwitchFrame(main_frame, switch)
            main_frame.pack(padx=PADDING, pady=PADDING * 5, side=LEFT, expand=True, fill="both")
        BTNFrame(self)

        # instead can create a main frame and add multiple frame on top of it for multi-page


if __name__ == "__main__":
    root = MainGUI()
    root.mainloop()
