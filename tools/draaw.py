import cv2
import numpy as np
import glob 

drawing=False # true if mouse is pressed
mode=True # if True, draw rectangle. Press 'm' to toggle to curve
pixel_size = 0.388*0.388
# mouse callback function

cs ={}
# input the image path down here
def file_parse(folder_path):

    # print(path)
    lis = glob.glob(folder_path + '/*')
    # print(lis)

    for l in lis:
        file = l.split('/')[-1]
        number = file.split('.')[0]

        while number not in cs.keys():
            input_file(l)

    return cs
    
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
    pixels = pixels * (0.0625) * (pixel_size)

    return pixels    

def input_file(path):

    X =[]   
    Y =[]
   

    file = path.split('/')[-1]
    number = file.split('.')[0]
    print(number)
    def crop_image(event,former_x,former_y,flags,param):
        global current_former_x,current_former_y,drawing, mode

        if event==cv2.EVENT_LBUTTONDOWN:
            drawing=True
            current_former_x,current_former_y=former_x,former_y
            X.append(current_former_x)
            
            Y.append(current_former_y)


        elif event==cv2.EVENT_MOUSEMOVE:
            if drawing==True:
                if mode==True:
                    cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(255,0,0),3)
                    current_former_x = former_x
                    current_former_y = former_y
                    X.append(current_former_x)
                    
                    Y.append(current_former_y)

                    #print former_x,former_y
        elif event==cv2.EVENT_LBUTTONUP:
            drawing=False
            if mode==True:
                cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(255,0,0),3)
                current_former_x = former_x
                current_former_y = former_y
                X.append(current_former_x)
                
                Y.append(current_former_y)
        return former_x,former_y    

   

    temp =  []
    def mousecallback(event,x,y,flags ,param):

        
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print("click")
            for i in range(len(contours)):
                r = cv2.pointPolygonTest(contours[i],(x,y),False)
                if r>0:
                    print("in")
                    temp.append(cv2.contourArea(contours[i])*0.0625/1.39)
                    print("contour selected",i)
                    cv2.fillPoly(im_use,pts=[contours[i]],color= (0,255,0))
                    print('done')



    im = cv2.imread(path)
    cv2.namedWindow("Image")
    cv2.setMouseCallback('Image',crop_image)
    while(1):
        cv2.imshow('Image',im)
        k=cv2.waitKey(1)&0xFF
        if k==32:
            
            break
        elif k ==27:
            print("code terminated")
            exit(0)
    cv2.destroyAllWindows()

    
    try:
        x =np.array(X)
        y =np.array(Y)
        x_max = np.max(x)
        # x_idx_max= np.where(x_max)
        y_max =np.max(y)
        # y_idx_max= np.where(y_max)
        x_min = np.min(x)
        x_idx_min= np.where(x_min)
        y_min =np.min(y)
    # y_idx_min= np.where(y_min)
    except:
        print("please select a region")
        return 


    im_cropped = im[y_min-4:y_max+4,x_min-4:x_max+4]
    im_use =im_cropped.copy()
    img_black  = cv2.cvtColor(im_cropped, cv2.COLOR_BGR2GRAY)


    blur = cv2.GaussianBlur(img_black,(3,3),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    im2,contours,hierarchy = cv2.findContours(th3, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(im_use, contours, -1, (0,0,255), 3)



    cv2.namedWindow("cropaf")
    cv2.setMouseCallback("cropaf", mousecallback)
    while(1):
        cv2.imshow('cropaf',im_use)
        k=cv2.waitKey(1)&0xFF
        if k==32:
            
            cs[number] = count_pixel(im_use)
            # cs[number] = sum(temp)
            break
        elif k ==27:
            print('code terminated')
            exit(0)
    cv2.destroyAllWindows()
    

    print("areas", cs)
    return cs[number]
    
# print(len(x),len(y))
# file_parse('/home/rohan/codes/LVP/VolumeAnalyser/Image_proc/png_files-20190624T064213Z-001/png_files')
