__author__ = 'nrot'

import os, math
from mutagen.mp3 import MP3

#Constant
MUSIC = ["mp3"]
MUSIC_RETURN = "MUSIC"
PLAYLIST = "m3u"
PLAYLIST_RETURN = "PLAYLIST"
EXTM3U = "#EXTM3U"
EXTINF = "#EXTINF"


def EndingName(name):
    i = 3
    ending = ""
    while i>=1:
        ending += name[len(name)-i]
        i -= 1
    i = 0
    for el in MUSIC:
        if el==ending:
            return MUSIC_RETURN
    if ending==PLAYLIST:
        return PLAYLIST_RETURN
    else:
        return False


def main():
    massiv = os.listdir()
    ArrayOfIndex = []
    #print(massiv)
    i = 0
    FilePlaylist = open("playlist.m3u", "w")

    FilePlaylist.write(EXTM3U + '\n' + '\n')

    for element in massiv:
        #print(massiv[i])
        EndReturn = EndingName(massiv[i])
        if EndReturn==MUSIC_RETURN:
            ArrayOfIndex.append(i)

            audio = MP3(str(massiv[i]))

            info = EXTINF + ':' +str(math.ceil(audio.info.length)) + ', ' + audio.tags['TALB'].text[0] + ' - ' + audio.tags['TIT2'].text[0]
            #print(audio.info.length)

            FilePlaylist.write(info + '\n')
            FilePlaylist.write('./' + str(massiv[i]) + '\n' + '\n')
        #elif EndReturn==PLAYLIST_RETURN:
        #   os.remove(os.getcwd() + massiv[i])
        i += 1
    return


if __name__=="__main__":
    main()