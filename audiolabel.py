import simpleaudio as sa
import os
import argparse

datapath = './'
parser = argparse.ArgumentParser()
parser.add_argument("--datapath", help="Path of audio data to be labeled, default: ./")
args = parser.parse_args()
if args.__dict__["datapath"]  is not None:
    datapath = args.__dict__["datapath"]

for inputFile in os.listdir(datapath):
	existingFilePath = datapath + "/" + inputFile
	wave_obj = sa.WaveObject.from_wave_file(existingFilePath)
	play_obj = wave_obj.play()
	#play_obj.wait_done()
	label = input()
	play_obj.stop()
	newFile = label + "_" + inputFile
	newFilePath =  datapath + "/" + newFile
	print("Labeling: " + inputFile + " as :" + newFile)
	os.rename(existingFilePath,newFilePath)