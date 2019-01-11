import matplotlib.pyplot as plt
import numpy as np
f1=5
Fs=5000
n=np.arange(0,2000,50)
x=np.sin(2*np.pi*f1*n/Fs)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.stem(n,x,'r')
plt.show()
