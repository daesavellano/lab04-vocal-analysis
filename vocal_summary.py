import numpy as np
import scipy.signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

#%%

(male, female) = (0,1)


def format_sample(sample: str):
    """Reformat text to numbers."""
    try:
        return float(sample)
    except:
        if sample=='M':
            return male
        elif sample =='F':
            return female
        else:
            return None

#%%

datafile = './assets/data/processed.csv'
header = True

datamat = np.array([]) # this will hold data in a matrix
variables = np.array([])


datalines = open(datafile, newline='\n').readlines()
for line in datalines:
  split_line = line.rstrip().split(',')
  if header:
    variables = np.append(variables,np.array(split_line))
    header = False
  else:
    datamat = np.append(datamat, np.array([format_sample(split_line[i]) for i in range(len(split_line))]))

ncols = len(variables)
nrows = int(len(datamat)/ncols)
   
datamat = np.resize(datamat, (nrows,ncols))

#%% define python variables for filtering

# TODO: If you added variables to `processed.csv`, also add them here
[
 filename,
 amplitude_limit,
 freq_limit,
 loudness_threshold,
 max_rms,
 max_cumu_freq,
 max_thresh_freq,
 ground_truth
] = np.arange(variables.size)

rows_male = np.squeeze(datamat[:,ground_truth]==male)
rows_female = np.squeeze(datamat[:,ground_truth]==female)

# create ground truth for emotion, assuming files are in order
rows_happy = np.array([True,True,True,True,True,True,True,True,True,True,True,True,
                       False,False,False,False,False,False,False,False,False,False,False,False])
rows_sad = ~rows_happy
ground_truth_emo = np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])


# rows_happy = np.array([])
# rows_sad = np.array([])
# ground_truth_emo = np.array([])
# for name in datamat[:,filename]:
#     if int(name) < 13:
#         rows_happy = np.append(rows_happy, True)
#         rows_sad = np.append(rows_sad, False)
#         ground_truth_emo = np.append(ground_truth_emo, 0)
#     else:
#         rows_happy = np.append(rows_happy, False)
#         rows_sad = np.append(rows_sad, True)
#         ground_truth_emo = np.append(ground_truth_emo, 1)
        

#%%

# Top Plot
fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.scatter(1+datamat[:,ground_truth], datamat[:,max_thresh_freq], marker='o');
plt.xlabel("Gender")
plt.ylabel("Frequency (Hz)")
plt.title("Peak Frequency by Gender above a loudness threshold")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[1] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()




fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.bar([1,2],(np.mean(datamat[rows_male,max_thresh_freq]), np.mean(datamat[rows_female,max_thresh_freq])));
plt.xlabel("Gender")
plt.ylabel("Frequency (Hz)")
plt.title("Mean Peak Frequency by Gender above a loudness threshold")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[2] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()




# Plots for cumulative freq
fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.scatter(1+datamat[:,ground_truth], datamat[:,max_cumu_freq], marker='o');
plt.xlabel("Gender")
plt.ylabel("Frequency (Hz)")
plt.title("Peak Frequency by Gender")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[1] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()



fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.bar([1,2],(np.mean(datamat[rows_male,max_cumu_freq]), np.mean(datamat[rows_female,max_cumu_freq])));
plt.xlabel("Gender")
plt.ylabel("Frequency (Hz)")
plt.title("Mean Peak Frequency by Gender")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[2] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()



# Plots for rms by gender
fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.scatter(1+datamat[:,ground_truth], datamat[:,max_rms], marker='o');
plt.xlabel("Gender")
plt.ylabel("RMS Amplitude (A.U.)")
plt.title("Peak RMS by Gender")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[1] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()



fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.bar([1,2],(np.mean(datamat[rows_male,max_rms]), np.mean(datamat[rows_female,max_rms])));
plt.xlabel("Gender")
plt.ylabel("RMS Amplitude (A.U.)")
plt.title("Mean Peak RMS by Gender")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[2] = 'Male'
labels[6] = 'Female'
ax.set_xticklabels(labels)
plt.show()



# Plots for rms by emotion
fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.scatter(1+ground_truth_emo, datamat[:,max_rms], marker='o');
plt.xlabel("Emotion")
plt.ylabel("RMS Amplitude (A.U.)")
plt.title("Peak RMS by Emotion")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[1] = 'Happy'
labels[6] = 'Sad'
ax.set_xticklabels(labels)
plt.show()



fig, ax = fig, ax = plt.subplots()
fig.canvas.draw()
plt.bar([1,2],(np.mean(datamat[rows_happy,max_rms]), np.mean(datamat[rows_sad,max_rms])));
plt.xlabel("Emotion")
plt.ylabel("RMS Amplitude (A.U.)")
plt.title("Mean Peak RMS by Emotion")
labels = ['' for item in ax.get_xticklabels()] # item.get_text()
labels[2] = 'Happy'
labels[6] = 'Sad'
ax.set_xticklabels(labels)
plt.show()









