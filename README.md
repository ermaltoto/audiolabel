# audiolabel
Utility to label audio files

usage: python audiolabel.py [-h] [--datapath DATAPATH]

optional arguments:
  -h, --help           show this help message and exit
  --datapath DATAPATH  Path of audio data to be labeled, default: ./
  
  
  ---------------
  
  script will play audio files from a given folder. The label can be written during the playback or after the file has been played. Playback will terminate when the enter button has been pressed, and the utility will move to the next file. The label will be added at the begining of the file, i.e: if the input file is 1234.wav and the label is jazz the file will be renamed as: jazz_1234.wav . Files can be labeled multiple times, and multiple labels will be appeneded at the begining of the file. 
  
Requires the following packages (tested in Python 3):
  
simpleaudio
os
argparse
