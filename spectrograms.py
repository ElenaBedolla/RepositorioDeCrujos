from obspy import read
from obspy.core.stream import Stream
import matplotlib.pyplot as plt
import os

main_folder = 'Template/'
event_folders = os.listdir(main_folder)
for event_folder in event_folders:
    event_data = event_folder.split('-')
    event_path = os.path.join(main_folder, event_folder)
    stations = os.listdir(event_path)
    for station in stations:
        station_path = os.path.join(event_path, station)
        #st = read(station_path)
        channels = os.listdir(station_path)
        n_chans = len(channels)
        fig, axs = plt.subplots(n_chans)
        st = Stream()
        for i, channel in enumerate(channels):
            channel_path = os.path.join(station_path, channel)
            chan = read(channel_path)
            st.append(chan[0])
            chan.spectrogram(log=True, title='Canal: %s'%(channel), wlen=st[i].stats.sampling_rate/100.0, show=False, axes=axs[i])
        try:
            st.plot(outfile=os.path.join(station_path, 'seismograms_plot.png'))
            plt.savefig(os.path.join(station_path,'spectrograms_plot.png'))
        except IndexError:
            print("No data for station %s"%(station))
        plt.clf()
        plt.close()
