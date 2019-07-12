#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 11, 2019 01:31:38 AM IST  platform: Linux

import sys

sys.path.append('../')
from tools import orb_area
from tkinter import filedialog as fd,messagebox
import glob,pickle
from tools import find_area

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

	import tkinter.ttk as ttk
	py3 = True


files_list = {}

def open_file():
	global dir_path,file_path,files_list
	files_list = {}
	file_path = fd.askopenfilenames(initialdir = '/home/rohan/codes/LVP' , title = 'select Files')
	names = [f.split('/')[-1] for f in file_path]
	dir_path = file_path[0].strip(file_path[0].split('/')[-1])
	check = glob.glob(dir_path+"orb_vol.pkl")
	
	if len(check)==0:
		for f in file_path:
			name = f.split('/')[-1]
			files_list[name] = 0.0
	else:
		try:
			with open(check[0],'rb') as f:
				temp = pickle.load(f)
			for n in names:
				if n in temp.keys():
					files_list[n] = temp[n]
				else:
					files_list[n] = 0.0
		except EOFError:
			for n in names:
				files_list[n] =0.0




	files = list(file_path)

	if len(files) ==0:
		messagebox.showinfo("Error", "Please select atleast one file!")

	else:
		pass

def draw_orb(img_name):

	using_path = dir_path + img_name 
	# print("using" , using_path)
	res = orb_area.random_area(using_path)
	files_list[img_name] = res

	return res

def save_stuff():

	with open(dir_path + 'orb_vol.pkl','wb') as f:
		pickle.dump(files_list, f)

	messagebox.showinfo('Saved!',"The results until now have been saved!")

  
def calc_vol():
	
	res = find_area.find_volume(files_list)
	messagebox.showinfo("result","Volume is " + str(res) + "mm^3")


def init(top, gui, *args, **kwargs):
	global w, top_level, root
	w = gui
	top_level = top
	root = top

def destroy_window():
	# Function which closes the window.
	global top_level
	top_level.destroy()
	top_level = None

if __name__ == '__main__':
	import orbital
	orbital.vp_start_gui()



