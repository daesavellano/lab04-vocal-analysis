# Lab 4 on Vocal Analysis


## Getting started

Before you start, ensure you have git, spyder, and an SSH key.

(VS Code, python, poetry, gatorgrade are not longer required. The 
tools above are much easier to get and use.)

On GitHub, click on the green button. Copy the SSH link.

In a terminal, navigate to the directory where you want to work on these files.
For this you can use the `cd` command. Clone the repo to your computer by typing:

`git clone ` and then the link that you copied.

In Spyder, go to project > new project 

Select existing directory and the directory that you just cloned

Follow along in lab session and check the starter repo README for updates.



This lab is in development, so updates will occur. 




To save your work after changes go to a terminal and navigate to the directory
for this project.

Type:

`git add .`

`git commit -m "Short message about what you have done"`

`git push origin main`

DO NOT USE A MIXTURE OF GIT AND GITHUB EDITING WITHOUT A FRIEND WHO KNOWS HOW
TO MIX THEM AND RESOLVE MERGE CONFLICTS. MY ADVICE IS TO STICK WITH GIT!

## New Instructions as of Feb. 11, 2024

Recall, this project involves analyzing audio data to find a story.

Objectives are to:

- practice exploring larger quanitites of data
- find a hidden story to tell (with the help of precoded figures)
- setting up a workflow with Spyder and git

DO NOT USE A MIXTURE OF GIT AND GITHUB EDITING WITHOUT A FRIEND WHO KNOWS HOW
TO MIX THEM AND RESOLVE MERGE CONFLICTS. MY ADVICE IS TO STICK WITH GIT!

### Check a Spyder setting

Everyone, please verify a certain Sypder setting: 
TODO: click Spyder>preferences>editor>advanced settings>End-of-line characters
TODO: ensure that both little boxes are checked for `fix automatically` and
`convert on save`. 
TODO: ensure the drop down menu is set to `LF (unix)`
TODO: click `Apply` and `OK`

### Familiarize yourself with Spyder

Spyder is an IDE or Integrated Development Environment for data analysis. By
default, you will see files in your project listed in the left-most pannel. If
you click on a file, the central panel will display it. The bottom right panel
is where text outputs will appear after running code cells. The top right
panel is where variables and plots will appear after running plotting code
cells. 

On the upper right, there is a bar that displays a path. This path should be
set to the directory that you cloned from git. If you see messages that files
are not found, ensure that the path is correct.

There is a very helpful button near the top center of the IDE that looks like a
split screen (next to the wrench). Click to maximize or minimize a window in
focus (or hover over that button to learn the keyboard short cut).

There is another helpful button above the plots that looks like an X. That will
close all of the open figures.

Spyder often tries to guess what you are typing. If you don't need its
suggestions, simply hit the escape key.

### What to do after cloning the repo and opening it as a Spyder project

After cloning the Lab 4 repo for vocal analysis and opening it as a Spyder
project (see the first 20 lines of this README), please navigate
to the `vocal_analysis.py` file. This file consists of code cells. You should
read the comments that appear in green and in grey and run each code cell. To
run a code cell, either use the _second_ play button in the top menu, or the
keyboard command of [shift + enter].

TODOs are located throughout the file. You can edit those lines of code to give
a better view into the audio data.


### Specifics on **creating** processed.csv

As you explore the audio data using the code cells provided in
`vocal_analysis.py`, please collect information about each of the audio files
located in assest/audio. The information you collect will be stored in
the csv file called `processed.csv`.


The file called `processed.csv` has comma-separated headers already inside the
file. Everything you add should be comma-separated. Do not use spaces. The
headers are:

```
filename,amplitude_limit,freq_limit,loudness_threshold,max_rms,max_cumu_freq,max_thresh_freq,ground_truth
```

Your job is to add observations for each audio file after exploring/choosing
suitable visualization limits. Please note that the observations you add may
not literally be located beneath the headings. CSV files are organized
using commas to keep track of columns and new lines to make a new observation.
New lines are made by hitting [enter].

- For `filename`: write `01` for 01.wav, `02` for 02.wav etc
- For `amplitude_limit`: write only the larger value in the limit. For example,
  if the limit is (-0.6, 0.6), just write `0.6`
- For `freq_limit`: write on the larger value in the limit. For example, if the
  limit is (0, 200), just write `200`
- For `loudness_threshold`: write the loudness threshold, for example `-20`
- For `max_rms`: look at the audio waveform and note down the highest amplitude
  of the orange RMS line.
- For `max_cumu_freq`: look at the cumulative loudness plot and note down the
  peak frequency value.
- For `max_thresh_freq`: look at the cumulative loudness above threshold plot
  and note down the peak frequency value.
- For `ground_truth`: listen to the audio and write `M` for male and `F` for
  female.

Normally explorations generate a lot of data, however for this lab, please only
save one observation per audio file. For a given audio file, the work flow may
be to pre-explore the plots to make sure you see reasonable peaks/values. When
you are satisfied with your visualization settings, record them in
`processed.csv`. 

Optionally, add one or more variables to the csv file that you think might be
useful to separate happy and sad audio files.

### How to **use** processed.csv and what to put in your blog post

That data collected and stored in `processed.csv` will be used by a script
called `vocal_summary.py` to crfeate additional figures. Run each of the code
cells in `vocal_summary.py`. Examine the figures to see if any of them nicely
separate your data by gender.

### Create a blog post

In `blogpost.md` please recap what you did in this lab. The data in this lab
was audio, but highlight general principles that you learned by using audio as
an example. Think about and write up what you learned about obtaining data,
preparation/exploration, storytelling with data, and numerical bias. 
This should be minimum of three paragraphs with minimum of three figures that
illustrate your point. Cite references in line and in a sections at the bottom
of the blot post. Use good Markdown styling that you have practiced in previous
blog posts.

### Push your work to GITHUB

Before the deadline of Feb 16th at 11:59pm, transfer your completed lab to
GitHub by using `git`.

In a terminal, use `cd` to change directories into the directory for this lab.
Then type:

- `git add .`
- `git commit -m "Short message about your work (5-10 words)"`
- `git push origin main`

DO NOT USE A MIXTURE OF GIT AND GITHUB EDITING WITHOUT A FRIEND WHO KNOWS HOW
TO MIX THEM AND RESOLVE MERGE CONFLICTS. MY ADVICE IS TO STICK WITH GIT!

### Optional workflow improvement

Optionally, update various configuration files on your computer so that you
don't have to repeatedly type your ssh key passphrase when using git. 
[Instructions for Mac](https://apple.stackexchange.com/questions/48502/how-can-i-permanently-add-my-ssh-private-key-to-keychain-so-it-is-automatically)
[Instructions for Windows](https://stackoverflow.com/questions/18683092/how-to-run-ssh-add-on-windows)






