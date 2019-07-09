import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
def func(file_path,save_path =None):	
	#-----Reading the image-----------------------------------------------------
	img = cv2.imread(file_path, 1)
	print(img.shape)
	lis = file_path.split('/')
	# cv2.imshow("img",img) 

	#-----Converting image to LAB Color model----------------------------------- 
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	# cv2.imshow("lab",lab)

	#-----Splitting the LAB image to different channels-------------------------
	l, a, b = cv2.split(lab)
	# cv2.namedWindow('l_channel',cv2.WINDOW_NORMAL)
	# cv2.imshow( 'l_channel',l)
	# cv2.namedWindow('a_channel',cv2.WINDOW_NORMAL)
	# cv2.imshow( 'a_channel',a)
	# cv2.namedWindow('b_channel',cv2.WINDOW_NORMAL)
	# cv2.imshow('b_channel', b)
	 
	#-----Applying CLAHE to L-channel-------------------------------------------
	clahe = cv2.createCLAHE(clipLimit=50, tileGridSize=(3,3))
	cl = clahe.apply(l)
	# cv2.namedWindow('CLAHE output',cv2.WINDOW_NORMAL)
	# cv2.imshow( 'CLAHE output',cl)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
	limg = cv2.merge((cl,a,b))
	# cv2.namedWindow('limg',cv2.WINDOW_NORMAL)
	# cv2.imshow( 'limg',limg)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	#-----Converting image from LAB Color model to RGB model--------------------
	final_1 = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
	imghsv = cv2.cvtColor(final_1, cv2.COLOR_BGR2HSV).astype("float32")
	(h, s, v) = cv2.split(imghsv)
	s = s*5
	s = np.clip(s,0,255)
	imghsv = cv2.merge([h,s,v])
	final  = cv2.cvtColor(imghsv.astype("uint8"),cv2.COLOR_HSV2BGR)
	final = cv2.cvtColor(final,cv2.COLOR_BGR2GRAY)
	# final = cv2.bilateralFilter(final, 5, 50, 50)
	# final = cv2.Canny(final,60,120)

	# cv2.imwrite(save_path+'cont_'+lis[-1],final_1)
	# final  = cv2.cvtColor(final_1,cv2.COLOR_BGR2GRAY)
	# ret,thr = cv2.threshold(final, 0, 255, cv2.THRESH_OTSU)
	# cv2.imwrite(save_path+'otsu_'+lis[-1],thr)
	# graph = image.img_to_graph(thr)
	# print(thr.shape)
	
	cv2.namedWindow('final',cv2.WINDOW_NORMAL)

	cv2.imshow( 'final',final)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#_____END_____#


def folder_scan(folder_path):
	lis = glob.glob(folder_path +'/*')
	parts = folder_path.split('/')
	save_path = folder_path.strip(parts[-1]) + 'contrasted_imgs/'
	try:
		os.mkdir(save_path)
	except:
		pass
	print(save_path)


	for l in lis:
		func(l,save_path)


# folder_scan('/home/rohan/codes/LVP/VolumeAnalyser/Image_proc/png_files-20190624T064213Z-001/png_files')

import cv2
img = cv2.imread("output.png")
img = cv2.resize(img, (2048,2048),interpolation = cv2.INTER_NEAREST)
cv2.imwrite("zoomed.png", img)
func("zoomed.png")