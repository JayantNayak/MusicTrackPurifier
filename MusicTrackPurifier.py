#! python3
import eyed3
import glob
import os
files = glob.glob('*.mp3')
print('Starting renaming........\n')
for file in files:
	audiofile = eyed3.load(file)
	fileName = audiofile.tag.title
	if(fileName.find(' - DJMaza')>-1):
		lastIndexToTrim = fileName.find(' - DJMaza')
	elif(fileName.find('- Songspk')>-1):
		lastIndexToTrim = fileName.find('- Songspk')
	newFileName = fileName[0:lastIndexToTrim]
	#print(newFileName+'\n')
	audiofile.tag.title = newFileName
	audiofile.tag.save()
	os.rename(file,newFileName+'.mp3')	
print('Done renaming all files')

