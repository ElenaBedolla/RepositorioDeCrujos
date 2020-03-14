from obspy import read
from obspy.core.stream import Stream
import matplotlib.pyplot as plt

ste = read('Template/20190704224221.78/CI.GSC.HNE')
stn = read('Template/20190704224221.78/CI.GSC.HNN')
stz = read('Template/20190704224221.78/CI.GSC.HNZ')

st = Stream([ste[0], stn[0], stz[0]])
channels = ['E', 'N', 'Z']
#print(st)
#print(st[0].stats)
fig, axs = plt.subplots(3) 
for i in range(3):
    st[i].spectrogram(log=False, title='Canal: %s'%(channels[i]), wlen=st[0].stats.sampling_rate/100.0, per_lap=0.999, show=False, axes=axs[i])
#st.plot()
plt.show()
