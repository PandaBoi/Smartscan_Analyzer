#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 08, 2019 09:07:34 PM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import orbital_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = orbital (root)
    orbital_support.init(root, top)
    root.mainloop()

w = None
def create_orbital(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = orbital (w)
    orbital_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_orbital():
    global w
    w.destroy()
    w = None

class orbital:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.title("Orbital Volume")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Open Dir")

if __name__ == '__main__':
    vp_start_gui()




