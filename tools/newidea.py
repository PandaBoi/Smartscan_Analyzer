








import sys
sys.path.append('../')

from vtk import *
import glob
import cv2
import pydicom
import pickle
from tools import draaw,find_area

def converter(folder_path,out_path):

    lis = glob.glob(folder_path +"/*")
    tis = glob.glob(folder_path+"/*.pkl")
    print(tis)
    print(lis)
    for t in tis:
        lis.remove(t)

    for file_path in lis:
        lis = file_path.split('/')
        print("converting",lis[-1])
        reader = vtkDICOMImageReader()
        reader.SetFileName(file_path)
        reader.Update()
        image = reader.GetOutput()

        ###########################################################
        # ww = 100
        # wl = 3
        ww = 95
        wl = 25
        greymap = vtkScalarsToColors()
        greymap.SetRange(wl-0.5*ww, wl+0.5*ww)

        applymap = vtkImageMapToColors()
        applymap.SetInputConnection(reader.GetOutputPort())
        applymap.SetLookupTable(greymap)

        applymap.SetOutputFormatToRGB()
        applymap.Update()
        ###########################################################

        writer = vtkPNGWriter()
        write_path = out_path+ lis[-1]+ '.png'
        writer.SetFileName(write_path)
        writer.SetInputConnection(applymap.GetOutputPort())
        writer.Write()
        img = cv2.imread(write_path)
        img = cv2.resize(img,(2048,2048),cv2.INTER_LINEAR)
        cv2.imwrite(write_path,img)

    print("done")


def caliberate(file_path,out_path):

    data = pydicom.dcmread(file_path)
    pixel = data[0x28,0x30].value
    draaw.PIXEL_SIZE = pixel[0]*pixel[1]
    slic = data[0x18,0x50].value
    space = data[0x18,0x88].value
    # find_area.THICKNESS = slic + space
    x = slic + space
    q = {'pixel_size':pixel[0],'thickness': x}

    storing = out_path + 'param.pkl'
    with open(storing, 'wb') as f:
        pickle.dump(q, f)
        f.close()







