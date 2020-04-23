# License
'''
Code by Adyasa
April 23,2020
Released under GNU GPL
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

Num =[2000]
Den =[1,102,200,0]
s1 = signal.lti(Num,Den) 
w, mag, phase = signal.bode(s1)

fig=subplot(2,1,1)
plt.semilogx(w, mag)  
plt.axhline(y = 0,xmin=0,xmax= 4.25226694,linestyle='dashed')
plt.axvline(x = 4.252,ymin=0,linestyle='dashed')
plt.axvline(x = 14.1,ymin =0,linestyle='dashed')
plt.text(4.252,0,'(4.252,0)')
plt.xlabel('Magnitude Plot')
plt.grid()
fig=subplot(2,1,2)
plt.semilogx(w, phase) 
plt.axhline(y = -180,xmin=0,linestyle='dashed')
plt.axvline(x = 14.1,ymin =0,linestyle='dashed')
plt.axvline(x = 4.25226694,ymin=0,linestyle='dashed')
plt.text(14.1,-180,'(14.1,-180)')
plt.xlabel('Phase Plot')
plt.xlabel('Frequency')
plt.grid()
plt.show()
