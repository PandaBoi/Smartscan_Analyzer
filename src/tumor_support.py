#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 08, 2019 08:52:17 PM IST  platform: Linux

import sys
sys.path.append('../')
from tkinter import filedialog, messagebox
from tools import newidea,draaw,find_area
import os
import glob
import re
import pickle


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

import os
from pathlib import Path
import sys

p = sys.executable
path = Path(p)

initial = path.anchor
file_list = {}

def tumor_dir():
    # try:
    global file_list,out_path,directory
    # print("working")
    directory = filedialog.askdirectory(title = "select directory")
    check = glob.glob(directory+"/*.pkl")
    file_lis = glob.glob(directory+"/*")
    out_path = directory.strip(directory.split('/')[-1]) + "converted_images/"
    newidea.caliberate(file_lis[-1],out_path)
   
    if check[-1].split('/')[-1] == 'result.pkl':
        with open(check[-1],'rb') as f:
            file_list = pickle.load(f)
            print(file_list)
            file_lis.remove(check[-1])

    
    
    
    all_files = [x.split('/')[-1] for x in file_lis ]
    

    if len(check) ==0:
        for l in all_files:
            file_list[l] = 0.0



    
    

    try:
        os.mkdir(out_path)
    except:
        pass

    newidea.converter(directory,out_path)

    messagebox.showinfo('Done',"All files are converted!")

    # except:
    #     messagebox.showinfo('Error',"Please select a proper Directory!")

def draw_on_it(name):

    file_path = out_path + name + '.png'
    res = draaw.input_file(file_path)
    file_list[name] = res

    return res

def save_stuff():

    with open(directory + '/result.pkl','wb') as f:
        pickle.dump(file_list, f)

    messagebox.showinfo('Saved!',"The results until now have been saved!")

  


def calc_vol():

    f = glob.glob(out_path + 'param.pkl')
    try:
        with open(f,'rb') as x:
            temp = pickle.load(x)
        result_vol = find_area.find_volume(file_list,temp['thickness'])
    except:
        result_vol = find_area.find_volume(file_list)

    messagebox.showinfo("Result","Volume is" + str(result_vol) + "mm^3")




    




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
    import tumor
    tumor.vp_start_gui()


