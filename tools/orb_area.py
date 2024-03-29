
import cv2
import numpy as np 
import glob
import pickle

drawing=False # true if mouse is pressed
mode=True # if True, draw rectangle. Press 'm' to toggle to curve

# mouse callback function
x =[]
y =[]




def count_pixel(img):
	
	# cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	# g1,g2 = 100,140
	img =np.array(img)
	# green  = img[:,:,1]
	# green = green/255
	# pixels = green.sum()

	green = [0,255,0]
	pixels = np.count_nonzero(np.all(img==green,axis =2))
	
	# (512/2048)^2 for size management 
	pixels = pixels * (0.0625) * (PIXEL_SIZE)

	return pixels  

	

# cs = []
# def mousecallback(event,x,y,flags ,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print("click")
#         for i in range(len(contours)):
#             r = cv2.pointPolygonTest(contours[i],(x,y),False)
#             if r>0:
#                 print("in")
#                 cs.append(cv2.contourArea(contours[i]))
#                 print("contour selected",i)
#                 cv2.fillPoly(im_use,pts=[contours[i]],color= (0,0,0))
#                 print('done')


def random_area(img_path,pix = 0.1505):
	global x,y,PIXEL_SIZE
	x =[]
	y =[]
# input the image path down here
	PIXEL_SIZE = pix
	
	def crop_image(event,former_x,former_y,flags,param):
		global current_former_x,current_former_y,drawing, mode

		if event==cv2.EVENT_LBUTTONDOWN:
			drawing=True
			current_former_x,current_former_y=former_x,former_y
			x.append(current_former_x)
			y.append(current_former_y)


		elif event==cv2.EVENT_MOUSEMOVE:
			if drawing==True:
				if mode==True:
					cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(255,0,0),5)
					current_former_x = former_x
					current_former_y = former_y
					x.append(current_former_x)
					y.append(current_former_y)

					#print former_x,former_y
		elif event==cv2.EVENT_LBUTTONUP:
			drawing=False
			if mode==True:
				cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(255,0,0),1)
				current_former_x = former_x
				current_former_y = former_y
				x.append(current_former_x)
				y.append(current_former_y)
		return former_x,former_y
	im = cv2.imread(img_path)
	cv2.namedWindow("Image")
	cv2.setMouseCallback('Image',crop_image)
	while(1):
		cv2.imshow('Image',im)
		k=cv2.waitKey(1)&0xFF
		if k==27:
			break
	cv2.destroyAllWindows()

	lineThickness = 1
	im_use = im.copy()*0
	for i in range(len(y)-1):
		# print(i,x[i],y[i])
		cv2.line(im_use, (x[i], y[i]), (x[i+1], y[i+1]), (255,255,255), lineThickness)
	x =np.array(x)
	y =np.array(y)
	x_max = np.max(x)
	# x_idx_max= np.where(x_max)
	y_max =np.max(y)
	# y_idx_max= np.where(y_max)
	x_min = np.min(x)
	x_idx_min= np.where(x_min)
	y_min =np.min(y)
	# y_idx_min= np.where(y_min)
	
	im_cropped = im_use[y_min-4:y_max+4,x_min-4:x_max+4]
	# print(im_cropped.shape)
	# print(img_black.shape)
	# im_use =im_cropped.copy()
	
	img_black1  = cv2.cvtColor(im_use, cv2.COLOR_BGR2GRAY)


	blur = cv2.GaussianBlur(img_black1,(3,3),0)
	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	im2,contours,hierarchy = cv2.findContours(img_black1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(im_use, contours, -1, (0,255,0), -1)
	area = count_pixel(im_use)


	# cv2.namedWindow("cropaf")
	# while(1):
	# 	cv2.imshow('cropaf',im_cropped)
	# 	k=cv2.waitKey(1)&0xFF
	# 	if k==27:
	# 		break
	# cv2.destroyAllWindows()

	# print("total area is",area)
	return area
# print(len(x),len(y))  

