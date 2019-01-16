import math

def CalculateBAI(height,hip_circum): 
	bai = ((100 * hip_circum)/(height*math.sqrt(height)))-18
	print('Your Body Adiposity Index :',bai)
