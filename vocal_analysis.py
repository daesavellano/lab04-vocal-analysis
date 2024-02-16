#%%


"""
The goals of this project are

1. practice exploring larger quanitites data
2. find a hidden story to tell (with the help of precoded figures)
3. setting up a workflow with spyder and git


As you change things, don't forget to rerun blocks of code that might depend 
on your changes. Also don't forget to save this file with file>save (or use
the typical keyboard shortcut for saving a file). You can tell if changes
have been made by looking for the little * that appears on the tab at the top
of this window.

You can also look at variables in the Variable Explorer -------------------->
One of the most useful ones to reference is probably filename so you can recall
which file you are working on.


Vocab
0. frequency is similar to pitch (high vs low). High pitch is a higher number
1. amplitude is similar to volume setting (high or low, like in your car)
2. loudness is perceived loudness (loud or soft)

Note on loudness
- The LOUDEST thing is 0 dB
- The SOFTEST thing is -60 dB
- Threshold (something you will set below) will be best between -60 and 0

"""




#%%


import numpy as np
import scipy.signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

#%%

# TODO: specify the file to explore. Note that it starts with ./
filename = './assets/audio/01.wav'

#%% apply transformations!

# reading in the data
fs, y = wavfile.read(filename)
t = np.arange(len(y))/fs


# scaling by dividing by a particular large number
y = y.astype(np.float32, order='C') / 32768.0
# smoothing the data with a moving average
rms = np.sqrt(np.convolve(np.power(y,2), 0.001*np.ones(1000), mode="same"))

# transform the audio amplitudes to pitch with Fourier Transform
F, T, Y = scipy.signal.stft(y, fs, nperseg=2048,  padded=True, noverlap=1024)
# transforming the pitch volume to loudness by applying log transform and scaling by 20
Y_dB = 20*np.log10(np.abs(Y)/np.amax(np.amax(np.abs(Y))));


#%%

"""
Data Exploration
Using the code below, try to measure and record points on the figures that allow
you to determine the gender of the speaker (and optionally their emotion).
For the purposes of this exercise, the gender is either female or male
(and the emotion is either happy or sad).

Record your measurements in ./assets/data/processed.csv

- remeber, do not use spaces
- separate everything by one comma


"""
#%%

# Controls for Visualizations

# TODO: change these as needed to explore your data up close or zoomed out
time_limit = (1, 2.75) # bounds on time range in seconds

# TODO: change these as needed to explore your data up close or zoomed out
amplitude_limit = (-0.6, 0.6) # bounds on audio sample height

# TODO: change these as needed to explore your data up close or zoomed out
freq_limit = (0, 200) # bounds on pitch range in Hz

# TODO: update loudness threshold as needed for exploration between -60 and 0
loudness_threshold = -20

# TODO: update figure size as needed for exploration
figure_size = (10,5)

# Summary
print("----------------------")
print("Summary for: ", filename)
print("----------------------")
print("time limit is ", time_limit)
print("amplitude limit is ", amplitude_limit)
print("frequency limit is ", freq_limit)
print("loudness threshold is ", loudness_threshold)
print("figure size is ", figure_size) 

#%%

print("----------------------")
print(f"Now plotting exploratory views of {filename}")
print("----------------------")

# Plotting
plt.close('all')

# Top Plot
plt.figure(figsize=figure_size)
plt.plot(t, y)
plt.grid()
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title(f"Waveform of {filename}")
plt.xlim(time_limit)
plt.ylim(amplitude_limit)
plt.plot(t, rms)
plt.plot(t[np.argmax(rms)], rms[np.argmax(rms)], 'r*');
plt.annotate(f"({t[np.argmax(rms)]},{rms[np.argmax(rms)]})", (t[np.argmax(rms)], rms[np.argmax(rms)]))

# 2nd Plot
plt.figure(figsize=figure_size)
plt.imshow(Y_dB,
           origin='lower',
           vmin = -60, vmax = 0,
           aspect='auto',
           cmap='jet',
           interpolation='spline16',
           extent=[T[0], T[-1], F[0], F[-1]])
cbar = plt.colorbar(location="bottom")
cbar.ax.set_xlabel('<----softer.............Loudness (dB).............louder---->', labelpad=-35)
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.title(f"Pitches Contained in Utterance {filename}")
plt.xlim(time_limit)
plt.ylim(freq_limit)

# 3rd Plot
# spectrum_full = np.sum(Y_dB, axis=1)
spectrum_full = np.ma.masked_invalid(Y_dB).sum(axis=1)
plt.figure(figsize=figure_size)
plt.plot(F, spectrum_full)
plt.plot(F[np.argmax(spectrum_full)], spectrum_full[np.argmax(spectrum_full)], 'r*');
plt.annotate(f"({F[np.argmax(spectrum_full)]},{spectrum_full[np.argmax(spectrum_full)]})", (F[np.argmax(spectrum_full)], spectrum_full[np.argmax(spectrum_full)]))
plt.title(f"Cumulative Loudnesses in {filename}")
plt.xlabel("Frequency (Hz)")
plt.xlim(freq_limit)
plt.ylabel("Sum over Data Points (A.U.)")

# 4th Plot
Y_dB_loud = Y_dB >= loudness_threshold
plt.figure(figsize=figure_size)
plt.imshow(Y_dB_loud,
           origin='lower',
           vmin = 0, vmax = 1,
           aspect='auto',
           cmap='gray',
           interpolation='None',
           extent=[T[0], T[-1], F[0], F[-1]])
cbar = plt.colorbar(location="bottom")
cbar.ax.set_xlabel('Black: soft............White: loud')
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.title(f"Loud Pitches Contained in Utterance {filename}")
plt.xlim(time_limit)
plt.ylim(freq_limit)

# Bottom Plot
spectrum = np.sum(Y_dB_loud, axis=1)
plt.figure(figsize=figure_size)
plt.plot(F, spectrum)
plt.plot(F[np.argmax(spectrum)], spectrum[np.argmax(spectrum)], 'r*');
plt.annotate(f"({F[np.argmax(spectrum)]},{spectrum[np.argmax(spectrum)]})", (F[np.argmax(spectrum)], spectrum[np.argmax(spectrum)]))
plt.title(f"Cumulative Loudnesses Above Threshold of {loudness_threshold} in {filename}")
plt.xlabel("Frequency (Hz)")
plt.xlim(freq_limit)
plt.ylabel("Sum over Loud Data Points (A.U.)")

#%%

# GROUND TRUTH - listen to the file
# TODO: in processed.csv add M for male, F for female

#%%

"""
Check the starter later for info about what to write in the blogpost.
For now, just gather data and save your work!
"""
