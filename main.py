import scipy.io as scio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filepath = "C:/Users/haobin/Desktop/individual/wykht8y7tg-1\Panasonic 18650PF Data/0degC/5 pulse/05-20-17_10.44 0degC_5pulse_HPPC_Pan18650PF.mat"

data=scio.loadmat(filepath)
list=['TimeStamp', 'Voltage', 'Current', 'Ah', 'Wh', 'Power', 'Battery_Temp_degC','Time','Chamber_Temp_degC']
data1=data['meas']
t = np.arange(len(data1[0,0][list[0]]))

fig, ax = plt.subplots()
for i in range(len(list)-3):
       test=data1[0, 0][list[i+1]].flatten()
       ax.plot(t, test,label = list[i+1])
ax.legend()
ax.set(xlabel='time ', ylabel='value',
       title='power features')
ax.grid()
fig.savefig("test.png")
plt.show()
