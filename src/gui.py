#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 08, 2019 04:34:23 PM IST  platform: Linux

import sys
sys.path.append('../')
# import second

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

import gui_support

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = Toplevel1 (root)
	gui_support.init(root, top)
	root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = tk.Toplevel (root)
	top = Toplevel1 (w)
	gui_support.init(w, top, *args, **kwargs)
	return (w, top)

def destroy_Toplevel1():
	global w
	w.destroy()
	w = None



class Toplevel1:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'
		font9 = "-family Saab -size 20 -weight bold -slant roman "  \
			"-underline 0 -overstrike 0"

		top.geometry("600x450+654+218")
		top.title("New Toplevel")

		self.Frame1 = tk.Frame(top)
		self.Frame1.place(relx=0.067, rely=0.044, relheight=0.9, relwidth=0.875)
		self.Frame1.configure(relief='groove')
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief="groove")
		self.Frame1.configure(width=525)

		self.Label1 = tk.Label(self.Frame1)
		self.Label1.place(relx=0.19, rely=0.198, height=141, width=309)
		self.Label1.configure(font=font9)
		self.Label1.configure(text='''DICOM ANALYZER''')
		self.Label1.configure(width=309)

		self.Button1 = tk.Button(self.Frame1)
		self.Button1.place(relx=0.076, rely=0.617, height=81, width=121)
		self.Button1.configure(text='''Calculate Length''')
		self.Button1.configure(disabledforeground="#b8a786")
		self.Button1.configure(command = gui_support.create_l_window)
		self.Button1.configure(width=121)

		self.Button2 = tk.Button(self.Frame1)
		self.Button2.place(relx=0.362, rely=0.617, height=81, width=121)
		self.Button2.configure(text='''Tumor Volume''')
		self.Button2.configure(width=121)
		self.Button2.configure(command = gui_support.create_t_window)

		self.Button3 = tk.Button(self.Frame1)
		self.Button3.place(relx=0.648, rely=0.617, height=81, width=131)
		self.Button3.configure(text='''Orbital Volume''')
		self.Button3.configure(width=131)
		self.Button3.configure(command = gui_support.create_o_window)

if __name__ == '__main__':
	vp_start_gui()





