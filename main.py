# pip3 install pydub. Will also need to run  sudo apt install ffmpeg.
from pydub import AudioSegment
from pydub.playback import play
from random import randint
import os
import glob

path = "white_noise"
files = os.listdir(path)

sounds = []


# Load all .wav files from the 'white_noise' directory
def load_sounds_from_directory():
    print('Loading white noise files from directory...')

    try:
        for filename in glob.glob(os.path.join(path, '*.wav')):
            sounds.append(filename)
        print("Successfully loaded white noise files.")
    except:
        print("Couldn't load white noise files!")


def generate_random_number():
    return randint(0, len(sounds) - 1)


# Pick a random white noise file and play it
def play_white_noise():
    while True:
        random_white_noise = sounds[generate_random_number()]
        white_noise = AudioSegment.from_wav(random_white_noise)
        print("Playing " + random_white_noise)
        play(white_noise)


if __name__ == '__main__':
    load_sounds_from_directory()
    play_white_noise()
