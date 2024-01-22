import os
import scaper
import numpy as np
import argparse


def has_overlapping_events(annotation_list):
    for (s1, e1, c) in annotation_list:
        for (s2, e2, c) in annotation_list:
            q1 = (s1, e1)
            q2 = (s2, e2)
            if metrics.coverage(q1, q2) > 0 and metrics.coverage(q1, q2) < 1.0:
                return True
    return False

def main():
    parser = argparse.ArgumentParser(description='A data generation script.')
    parser.add_argument('--data_dir', help='The data dir containing the train and test source directories', required=True, type=str)
    parser.add_argument('--dataset_name', help='The name of the generated dataset', required=True, type=str)
    parser.add_argument('--snr', help='The signal-to-noise ratio (in LUFS)', required=True, type=float)
    parser.add_argument('--n_soundscapes', help='The number of soundscapes to generate', required=True, type=int)
    parser.add_argument('--bg_label', help='The backgrounds to use. Set to ''all'' if all should be used', required=False, type=str)
    parser.add_argument('--fg_label', help='The foregrounds to use. Set to ''all'' if all should be used', required=False, type=str)
    args = parser.parse_args()

    for idx_split, split in enumerate(['train', 'test']):
        print("Generating {} soundscapes ...".format(split))

        # OUTPUT FOLDER
        outfolder = os.path.join(args.data_dir, 'generated_datasets', args.dataset_name, '{}_soundscapes_snr_{}'.format(split, args.snr))

        if not os.path.exists(outfolder):
            os.makedirs(outfolder)

        # SCAPER SETTINGS
        fg_folder = '{}/sources/{}_sources/foreground/'.format(args.data_dir, split)
        bg_folder = '{}/sources/{}_sources/background/'.format(args.data_dir, split)

        # the reference dB level of the audio files
        ref_db = -20 # LUFS

        n_soundscapes = args.n_soundscapes

        # the duration in seconds of the soundscapes to generate
        duration = 30.0 

        # the minimum and maximum number of events per soundscape
        # if different we will randomly sample from this range
        min_events = 3
        max_events = 3

        source_time_dist = 'const'
        source_time = 0.0

        # the distribution of event lengths
        # NOTE: if event_duration_min is larger than the minimum length of
        # the source material, then the natural event lengths will be used.
        # Only use this if you want to introduce artificial event length
        # variation
        event_duration_dist = 'uniform'
        event_duration_min  = 4
        event_duration_max  = 4

        # the distribution of event start times
        event_time_dist = 'uniform'
        event_time_min  = 4
        event_time_max  = 26

        # the distribution of snr values
        snr_dist = 'uniform'
        snr_min = args.snr
        snr_max = args.snr

        # the distribution of pitch shift values
        pitch_dist = 'uniform'
        pitch_min = 0
        pitch_max = 0

        # the distribution of time stretch values
        time_stretch_dist = 'uniform'
        time_stretch_min = 1.0
        time_stretch_max = 1.0

        # the basename of the soundscape
        basename = 'soundscape'
            
        for n in range(n_soundscapes):
            
            print('Generating soundscape: {:d}/{:d}'.format(n+1, n_soundscapes))
            
            # create a scaper
            sc = scaper.Scaper(duration, fg_folder, bg_folder, random_state=n_soundscapes*idx_split + n)
            sc.protected_labels = []
            sc.ref_db = ref_db
            
            # add background
            if args.bg_label == 'all':
                bg_label = ('choose', [])
            else:
                bg_label = ('choose', [args.bg_label])

            sc.add_background(label=bg_label, 
                            source_file=('choose', []), 
                            source_time=('const', 0))

            # add random number of foreground events
            n_events = np.random.randint(min_events, max_events+1)

            if args.fg_label == 'all':
                fg_label = ('choose', [])
            else:
                fg_label = ('choose', [args.fg_label])
            for _ in range(n_events):
                sc.add_event(label=fg_label,
                            source_file=('choose', []), 
                            source_time=(source_time_dist, source_time), 
                            event_time=(event_time_dist, event_time_min, event_time_max), 
                            event_duration=(event_duration_dist, event_duration_min, event_duration_max), 
                            snr=(snr_dist, snr_min, snr_max),
                            pitch_shift=(pitch_dist, pitch_min, pitch_max),
                            time_stretch=(time_stretch_dist, time_stretch_min, time_stretch_max))
            
            # filepaths
            audiofile = os.path.join(outfolder, "{}_{:d}.wav".format(basename, n))
            jamsfile = os.path.join(outfolder, "{}_{:d}.jams".format(basename, n))
            txtfile = os.path.join(outfolder, "{}_{:d}.txt".format(basename, n))
            
            # loop until we get a soundscape without overlapping events
            # NOTE: remove this is you want to allow overlapping events
            overlapping_events = True
            while overlapping_events:
                sounscape_audio, soundscape_jam, annotation_list, event_audio_list = sc.generate(
                    audio_path            = audiofile,
                    jams_path             = jamsfile,
                    allow_repeated_label  = True,
                    allow_repeated_source = False,
                    reverb                = None, 
                    fix_clipping          = True, # TODO: is this reasonable?
                    peak_normalization    = False,
                    quick_pitch_time      = False,
                    save_isolated_events  = False,
                    isolated_events_path  = None,
                    disable_sox_warnings  = True,
                    no_audio              = True,
                    txt_path              = txtfile,
                )

                overlapping_events = has_overlapping_events(annotation_list)
                if overlapping_events:
                    print("OVERLAPPING: ", annotation_list)

            # TODO: generate audio from the jams file
            scaper.generate_from_jams(jams_infile = jamsfile, audio_outfile = audiofile)
