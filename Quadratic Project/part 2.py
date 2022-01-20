import math

int_a=0
int_b=2
int_c=1

def Calculation_V01():
	# calculating discriminant using formula
	dis = (int_b * int_b - 4 * int_a * int_c)
	sqrt_val = math.sqrt(abs(dis))
	
	# checking condition for discriminant
	if dis > 0:
		print(" real and different roots ")
		print((-int_b + sqrt_val)/(2 * int_a))
		print((-int_b - sqrt_val)/(2 * int_a))
	
	elif dis == 0:
		print(" real and same roots")
		print(-int_b / (2 * int_a))
	
	# when discriminant is less than 0
	else:
		print("Complex Roots")
		print(- int_b / (2 * int_a), " + i", sqrt_val)
		print(- int_b / (2 * int_a), " - i", sqrt_val)