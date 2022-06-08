import scipy.io as scio
import pandas as pd
import numpy as np
filepath = "C:/Users/haobin/Desktop/individual/wykht8y7tg-1\Panasonic 18650PF Data/0degC/5 pulse/05-20-17_10.44 0degC_5pulse_HPPC_Pan18650PF.mat"
data=scio.loadmat(filepath)
print(data)
print(type(data))
print(data.keys())
data1=data['meas']
print(data1)
print(data1[0,0]['TimeStamp'])
print(data1[0,0]['TimeStamp'].shape)
print(data1[0,0]['Voltage'])
print(data1[0,0]['Ah'])

