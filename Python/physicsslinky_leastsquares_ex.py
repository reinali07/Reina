#least squares fit, error bars, residuals, chi square. Data from wave propagation in a slinky
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:25:12 2019

@author: reina
"""
filename="mydata.txt"


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from pylab import loadtxt

import numpy as np


def linear(x, b, c):
    return x*b-c


#xdata = np.array([1.9557,1.7557,1.5557,1.3557,1.1557,0.9557,0.7557,0.5557,0.3557,0.0557])
#ydata = np.array([5.01/100,3.42/100,2.66/100,1.89/100,0.72/100,0.4/100,0.31/100,0.11/100,0.08/100,0])
#xerror = np.array([0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005])
#yerror = np.array([0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005])

data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)

# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y
B = 0.333

xdata=data[0]
xerror=data[1]
ydata=data[2]
yerror=data[3]

start=min(xdata)
stop=max(xdata)  

popt1, pcov1 = curve_fit(linear, xdata, ydata)
#popt2, pcov2 = curve_fit(exp2, xdata, ydata)


plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt="b.")

#print(popt1,[pcov1[0,0]**0.5],[pcov1[1,1]**0.5])
print("(" + str(popt1[0]) + " +/- " + str(pcov1[0,0]**0.5) + ")" + "x" + " - " + str(popt1[1]) + " +/- " + str(pcov1[1,1]**0.5))
#print(popt2,[pcov2[0,0]**0.5],[pcov2[1,1]**0.5])
#(0.09 +/- 0.03)*exp((2.1 +/- 0.2)*x)
#(0.08 +/- 0.02)*(exp((2.1 +/- 0.2)*x)+exp((-2.1 +/- 0.2)*x))

domain = np.linspace(start,stop,1000)

plt.plot(domain, linear(domain,*popt1), 'g-')
plt.xlabel("f [Hz]")
plt.ylabel("eVstop [V]")
plt.title("eVstop vs f")

chi1 = stats.chisquare(list(ydata),linear(xdata,*popt1))
#print(chi1[0]/(len(xdata)-2))
#chi = sum((list(ydata)-linear(xdata,*popt1))*(list(ydata)-linear(xdata,*popt1))/linear(xdata,*popt1))
print("reduced chi square:" + str(chi1[0]/(len(xdata)-2)))

plt.show()

#plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt="b.")
#plt.plot(domain, exp2(domain,*popt2), 'r-')

#plt.xlabel("x [m]")
#plt.ylabel("y [m]")
#plt.title("Decay of Amplitudes Across Slinky")

#chi2 = stats.chisquare(list(ydata),exp2(xdata,*popt2))
#print(chi2[0]/8)

#plt.show()

residual=ydata-linear(xdata,*popt1)
zeroliney=[0,0]
zerolinex=[start,stop]
plt.errorbar(xdata,residual,yerr=yerror,xerr=xerror,fmt=".")
plt.plot(zerolinex,zeroliney)

plt.xlabel("f [Hz]")
plt.ylabel("residuals of eVstop [V]")
plt.title("Residuals of the fit")

plt.show()

#residual=ydata-exp2(xdata,*popt2)
#zeroliney=[0,0]
#zerolinex=[start,stop]
#plt.errorbar(xdata,residual,yerr=yerror,xerr=xerror,fmt=".")
#plt.plot(zerolinex,zeroliney)

#plt.xlabel("x [m]")
#plt.ylabel("residuals of y [m]")
#plt.title("Residuals of the fit")

#plt.show()