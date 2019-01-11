import matplotlib.pyplot as plt
import numpy as np
f1=1
f2=2
Fs=2000
sample=8000
n=np.arange(sample)
x=np.sin(2*np.pi*f1*n/Fs)
plt.subplot(311)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(n,x,'r')
y=np.sin(2*np.pi*f2*n/Fs)
plt.subplot(312)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(n,y,'b')
z=x+y
plt.subplot(313)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(n,z,'k')
plt.show()
