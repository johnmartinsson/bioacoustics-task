# Introduction
A description of the bioacoustics task for the advanced audio processing course at Tampere University. This is a sound event detection task, where the goal is to predict the onset and offset of bioacoustic sound events. Bioacoustics is sounds related to animals, and in this task we have three different datasets:

  1. Meerkat
  2. Dog
  3. Baby cry

These sound classes vary a bit in characteristic. The Meerkat sounds are consistently very short, and the baby cries vary more and are longer.

These are setup as three binary classification tasks.

The datasets are split into training and test data. The file structure is pairs of audio and annotations (<filename>.wav, <filename>.txt). Only annotations of the event class of interest are provided. E.g., for the Meerkat sounds we provide annotations for all onset and offset Meerkat sounds in <filename>.txt which corresponds to the audio file <filename>.wav. The format is

    <onset_1>  <offset_1>  <event_label_1>
    <onset_2>  <offset_2>  <event_label_2>
    .
    .
    .
    <onset_n>  <offset_n>  <event_label_n>

for the n events in the audio file. In these datasets n=3, that is, there are always exactly 3 events in each soundscape. However, we could make this more difficult if desired.

## Meerkat dataset

![Meerkat reference labels](examples/meerkat_reference_labels.png)

An audio and annotation example is provided in 'examples/meeerkat_soundscape_15.txt', and 'examples/meeerkat_soundscape_15.wav'.

## Dog dataset

![Dog reference labels](examples/dog_reference_labels.png)

## Baby cry dataset

![Baby reference labels](examples/baby_reference_labels.png)

# Data
The three datasets have been generated using Scaper.

## Pre-generated datasets
Download using dropbox link: https://www.dropbox.com/scl/fi/28i35xxwlozzpnnmsdy2m/bioacoustics-tasks.zip?rlkey=ff68wyvuy1h1lv12nc3yqew3l&dl=0
  
  unzip bioacoustics-tasks.zip

## Generate own datasets
Students can get the source material and the code used to generate the datasets if they want to add more variability, change the SNR, or even generate a multi-label classification task.

Dowload the source material: https://www.dropbox.com/scl/fi/ay0w0lb2y2zogjh7779us/bioacoustics-sources.zip?rlkey=sxm8dpp13473a9ewi6vefw22v&dl=0

  unzip bioacoustics-sources.zip
  python generate_data.py


