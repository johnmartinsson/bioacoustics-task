# Introduction
A description of the bioacoustics task for the advanced audio processing course at Tampere University. This is a sound event detection task, where the goal is to predict the onset and offset of bioacoustic sound events. Bioacoustics is sounds related to animals, and in this task we have three different datasets:

  1. Meerkat
  2. Dog
  3. Baby cry

These sound classes vary a bit in characteristic. The Meerkat sounds are consistently very short, and the baby cries vary more and are longer.

These are setup as three binary classification tasks.

## Meerkat dataset

![Meerkat reference labels](https://github.com/johnmartinsson/bioacoustics-task/tree/main/examples/meerkat_reference_labels.png)

## Dog dataset

## Baby cry dataset

# Data
The three datasets have been generated using Scaper.

## Pre-generated datasets
Download using dropbox link: https://www.dropbox.com/scl/fi/28i35xxwlozzpnnmsdy2m/bioacoustics-tasks.zip?rlkey=ff68wyvuy1h1lv12nc3yqew3l&dl=0
  
  unzip bioacoustics-tasks.zip

## Generate own datasets
Students can get the source material and the code used to generate the datasets if they want to add more variability, change the SNR, or even generate a multi-label classification task.

Dowload the source material: https://www.dropbox.com/scl/fi/ay0w0lb2y2zogjh7779us/bioacoustics-sources.zip?rlkey=sxm8dpp13473a9ewi6vefw22v&dl=0

  unzip bioacoustics-sources.zip
  python generate_soundscapes.py --dataset_name=$dataset_name --snr=$snr --bg_label=$bg_label --fg_label=$fg_label --n_soundscapes=$n_soundscapes --data_dir=$data_dir

Please see the comments and in the generate_soundscape.py file to understand what it does.

## Generate own source material

I have not fully described this yet, but this is the script used to generate the source material. That is, to extract the background sounds and foreground sounds from other openly available strongly labeled sound event detection datasets.

    python generate_source_material.py --source_output_dir=<output_dir>