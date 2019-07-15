import cv2
import numpy as np
from PIL import Image
import math

drawing=True # true if mouse is pressed
def input_file(path,pix = 0.388):

	
	PIXEL_SIZE = pix

	def draw_circle(event,former_x,former_y,flags,param):
		global current_former_x,current_former_y,drawing,distance
		if event == cv2.EVENT_LBUTTONDBLCLK:
			cv2.circle(img,(former_x,former_y),10,(255,0,0),-1)
			if drawing == False:
				cv2.line(img,(current_former_x,current_former_y),(former_x,former_y),(255,0,0),1)
				dx2= (current_former_x-former_x)**2
				dy2= (current_former_y-former_y)**2
				distance = math.sqrt(dx2 + dy2)
				distance = distance * .25 * PIXEL_SIZE
				print(distance)
				print("mm")
				# current_former_x,current_former_y=former_x,former_y
				drawing = True  
			else   :
				current_former_x,current_former_y=former_x,former_y
				drawing = False
	try:  
		im_np  = Image.open(path)  
		img = np.array(im_np)
	except IOError:
		pass
	cv2.namedWindow("Image")
	cv2.setMouseCallback('Image',draw_circle)

	while(1):
		cv2.imshow('Image',img)
		k=cv2.waitKey(1)&0xFF
		if k==27:
			break
	cv2.destroyAllWindows()
	return distance