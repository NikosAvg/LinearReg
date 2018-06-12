from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
style.use("fivethirtyeight")

def create_dataset(hm,variance,step=2,correlation=False):
	val=1
	ys = []
	for i in range(hm):
		y = val + rd.randrange(-variance, variance)
		ys.append(y)
		if correlation and correlation=='pos':
			val+=step
		elif correlation and correlation=='neg':
			val-=step;

	xs = [i for i in range(len(ys))]

	return np.array(xs,dtype=np.float64), np.array(ys,dtype=np.float64)

def best_fit_slope_intercept(xs,ys):
	m = ( ((mean(xs)*mean(ys)) - mean(xs*ys)) /
			((mean(xs)*mean(xs)) - mean(xs*xs)))
	b = mean(ys) - m* mean(xs)
	return m, b

def squared_error(ys_orig, ys_line):
	return sum((ys_line - ys_orig)**2)
		
def coefficient_of_determination(ys_orig,ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]	
	squared_error_reg = squared_error(ys_orig, ys_line)
	squared_error_y_mean = squared_error(ys_orig, y_mean_line)
	return 1-(squared_error_reg/squared_error_y_mean)

#create our testing dataset
xs, ys = create_dataset(40,40,2,correlation='pos') 

m, b = best_fit_slope_intercept(xs,ys)

#create the line for our data
regression_line = [(m*x)+b for x in xs]
rsq = coefficient_of_determination(ys,regression_line)

#Print r-squared
print(rsq)

#plot our data and the best fit line
plt.scatter(xs,ys,color="g")
plt.plot(xs,regression_line,color="r")
plt.show()

