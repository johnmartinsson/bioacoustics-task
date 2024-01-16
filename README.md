# Introduction
A description of the bioacoustics task for the advanced audio processing course at Tampere University. This is a sound event detection task, where the goal is to predict the onset and offset of bioacoustic sound events. Bioacoustics is sounds related to animals, and in this task we have three different datasets:

  1. Meerkat
  2. Dog
  3. Baby cry

These sound classes vary a bit in characteristic. The Meerkat sounds are consistently very short, and the baby cries vary more and are longer.

These are setup as three binary classification tasks.

# Data
The three datasets have been generated using Scaper.

## Pre-generated datasets

  wget <dropbox-link>
  unzip ...

## Generate own datasets
Students can get the source material and the code used to generate the datasets if they want to add more variability, change the SNR, or even generate a multi-label classification task.

  wget <dropbox-link>
  python generate_data.py

# Meerkat dataset

# Dog dataset

# Baby cry dataset
