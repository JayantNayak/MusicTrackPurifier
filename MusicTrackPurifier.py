#! python3
import eyed3
import glob
import os
files = glob.glob('*.mp3')
print('Starting renaming........\n')
for file in files:
	audiofile = eyed3.load(file)
	fileName = audiofile.tag.title
	album = audiofile.tag.album
	albumArtist = audiofile.tag.album_artist
	#print(trackNum)
	#print(artist)
	#print(album)
	#print(albumArtist)
	lastIndexToTrimName = 0
	if(fileName.find(' - DJMaza')>-1):
		lastIndexToTrimName = fileName.find(' - DJMaza')
	elif(fileName.find('- Songspk')>-1):
		lastIndexToTrimName = fileName.find('- Songspk')
	fileName = fileName[0:lastIndexToTrimName]
	if(album.find(' (')):
		lastIndexToTrimAlbum = album.find(' (')
	album = album[0:lastIndexToTrimAlbum]
	if(albumArtist.find(': ')):
		firstIndexAlbumArtist = albumArtist.find(': ')+2
	if(albumArtist.find(' | DJMaza')):
		lastIndexAlbumArtist = albumArtist.find(' | DJMaza')
	albumArtist = albumArtist[firstIndexAlbumArtist:lastIndexAlbumArtist]
	#print(albumArtist)	
	#print(album)
	#print(newFileName+'\n')
	
	audiofile.tag.title = fileName
	audiofile.tag.track_num = (None,None)
	audiofile.tag.album = album
	audiofile.tag.album_artist = albumArtist
	audiofile.tag.disc = (None,None)
	audiofile.tag.publisher = None
	audiofile.tag.save()
	os.rename(file,fileName+'.mp3')		
print('Done renaming all files')

