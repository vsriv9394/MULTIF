import _meshutils_module
import ctypes
import numpy as np
import pylab

#knots = np.array([1.2, 2.5, 3.1, 4.5, 5.1, 6.945]);
#knots = np.array(1.2, 2.5, 3.1, 4.5, 5.1, 6.945);

coefs = [0.0000, 0.0000, 0.1500, 0.1700, 0.1900, 0.2124, 0.2269, 0.2734, 0.3218, 0.3218, 0.3230, 0.3343, 0.3474, 0.4392, 0.4828, 0.5673, 0.6700, 0.6700, 0.3255, 0.3255, 0.3255, 0.3255, 0.3255, 0.3238, 0.2981, 0.2817, 0.2787, 0.2787, 0.2787, 0.2797, 0.2807, 0.2936, 0.2978, 0.3049, 0.3048, 0.3048];
knots = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 15.0, 15.0, 15.0];

x    = [];
y    = [];
dydx = [];

nx = 100;
k  = len(knots);
c  = len(coefs)/2;

_meshutils_module.py_BSplineGeo3 (knots, coefs, x, y, nx);

for i in range(0,len(x)):
	print "%lf %lf" % (x[i], y[i]);
	
