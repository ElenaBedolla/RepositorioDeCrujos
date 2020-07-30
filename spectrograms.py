import matplotlib
matplotlib.use('Agg')

from obspy import read
from obspy.core.stream import Stream
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import numpy as np
from os import path
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

j = cm.get_cmap('jet')
cur_path = os.path.dirname(__file__)
rel_main_folder = 'Template/'
main_folder = os.path.join(cur_path, rel_main_folder)
event_folders = os.listdir(main_folder)
for event_folder in event_folders:
    event_data = event_folder.split('-')
    event_path = os.path.join(main_folder, event_folder)
    stations = os.listdir(event_path)
    for station in stations:
        station_path = os.path.join(event_path, station)
        #st = read(station_path)
        channels = os.listdir(station_path)
        n_chans = float(len(channels))
        axs = []
        fig = plt.figure(figsize=(8,8))
        for i in range(int(n_chans)):
            if i == 0:
                ax2 = fig.add_axes([0.1, 0.1+(i*0.8)/n_chans, 0.7, 0.8/n_chans])
                axs.append(ax2)
            else:
                axs.append(fig.add_axes([0.1, 0.1+(i*0.8)/n_chans, 0.7, 0.8/n_chans], sharex=axs[i-1]))
        axs.append(fig.add_axes([0.83, 0.1, 0.03, 0.8]))
        #fig, axs = plt.subplots(n_chans)
        st = Stream()
        for i, channel in enumerate(channels):
            channel_path = os.path.join(station_path, channel)
            chan = read(channel_path)
            st.append(chan[0])
            ax2 = chan.spectrogram(title='Canal: %s'%(channel), show=False, axes=axs[i], cmap=j)
        #print(ax2[0].images[0])
        #canvas = FigureCanvas(fig2)
        #image = np.fromstring(canvas.tostring_rgb(), dtype='uint8')
        #print(list(axs[0]y.get_images()))
        mappable = ax2[0].images[0]
        plt.colorbar(mappable=mappable, cax=axs[-1])
        try:
            if not path.exists(os.path.join(station_path, 'seismograms_plot.png')):
                st.plot(outfile=os.path.join(station_path, 'seismograms_plot.png'))
            if path.exists(os.path.join(station_path,'spectrograms_plot.png')):
                os.remove(os.path.join(station_path,'spectrograms_plot.png'))
            plt.savefig(os.path.join(station_path,'spectrograms_plot.png'))
        except IndexError:
            print("No data for station %s"%(station))
        plt.clf()
        plt.close()
