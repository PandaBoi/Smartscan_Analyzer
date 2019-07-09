





# "Sharpen" an image by  multiplying every pixel by 2, and then subtracting
# the average value of the neighborhood from it.

#See slide number 22 from IrfanEssa-CP-02-5-Filtering.pdf

#
# Jay Summet 2015
#
#Python 2.7, OpenCV 2.4.x
#

# import cv2
# import numpy as np


# #Linux window/threading setup code.
# cv2.startWindowThread()
# cv2.namedWindow("Original")
# cv2.namedWindow("Sharpen")

# #Load source / input image as grayscale, also works on color images...
# imgIn = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Original", imgIn)


# #Create the identity filter, but with the 1 shifted to the right!
# kernel = np.zeros( (9,9), np.float32)
# kernel[4,4] = 2.0   #Identity, times two! 

# #Create a box filter:
# boxFilter = np.ones( (9,9), np.float32) / 81.0

# #Subtract the two:
# kernel = kernel - boxFilter


# #Note that we are subject to overflow and underflow here...but I believe that
# # filter2D clips top and bottom ranges on the output, plus you'd need a
# # very bright or very dark pixel surrounded by the opposite type.

# custom = cv2.filter2D(imgIn, -1, kernel)
# cv2.imshow("Sharpen", custom)


# cv2.waitKey(0)










from vtk import *
import glob
import cv2

def converter(folder_path,out_path):

    lis = glob.glob(folder_path +"/*")
    tis = glob.glob(folder_path+"/*.pkl")
    lis.remove(tis[0])

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



