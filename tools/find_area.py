from draaw import *
import re
import numpy as np
from math import *
# areas = file_parse('/home/rohan/codes/LVP/VolumeAnalyser/Image_proc/png_files-20190624T064213Z-001/png_files')
areas = {'IM188': 110.02877697841727, 'IM131': 147.7158273381295, 'IM184': 127.2841726618705, 'IM172': 124.11510791366906, 'IM187': 142.37769784172662, 'IM130': 418.7985611510791, 'IM141': 97.30935251798562, 'IM171': 116.43884892086331, 'IM179': 114.23381294964028, 'IM157': 140.5791366906475, 'IM183': 119.20863309352518, 'IM122': 31.503597122302157}
THICKNESS = 2.00

def preprocess(areas):

	sorted_slices = sorted(areas.keys())

	numb = []
	for slice in sorted_slices:

		numb.append(int(re.search(r'\d+', slice).group()))

	h =[]
	for i in range(len(numb)-1):
		h.append(numb[i+1] - numb[i])


	h = np.array(h)*THICKNESS
	print(h)


	return sorted_slices,h


def find_volume(areas):

	slices , h = preprocess(areas)

	slice_area = [areas[s] for s in slices]
	print(slices)

	# print(slice_area)

	V = 0
	for i in range(len(slice_area) -1 ):

		V += (h[i]/3)*(slice_area[i] + slice_area[i+1] + (sqrt(slice_area[i]*slice_area[i+1])))


	print("volume of tumor(approx) is ",V,"mm^3")


# find_volume(areas)





