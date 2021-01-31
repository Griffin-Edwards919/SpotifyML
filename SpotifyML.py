import csv, random

class Song:
    def __init__(self, a, t, y, e, d, n, l, o, s, p):
        self.artist = a
        self.name = t
        self.year = y
        self.isExplicit = e
        self.duration = d
        self.danceability = n
        self.liveness = l
        self.loudness = o
        self.speechiness = s
        self.popularity = p

    def __str__(self):
        return self.artist + ' ' + self.name + ' ' + self.year + ' ' + self.popularity


if __name__ == '__main__':
    # Code used to import and shuffle data:

    # dataset = open('data.csv')
    # songlist = []
    # for song in csv.reader(dataset):
    # songlist.append(Song(song[1], song[12], song[18], song[5], song[3], song[2], song[9], song[10], song[15], song[13]))
    # dataset.close()
    # shuffled = open('ShuffledData', 'w')
    # random.shuffle(songlist)
    # for song in songlist[:-1]:
    # shuffled.write(song.artist+','+song.name+','+song.year+','+song.isExplicit+','+song.duration+','+song.danceability+','+song.liveness+','+song.loudness+','+song.speechiness+','+song.popularity+'\n')
    # shuffled.write(songlist[-1].artist + ',' + songlist[-1].name + ',' + songlist[-1].year + ',' + songlist[-1].isExplicit + ',' + songlist[-1].duration + ',' + songlist[-1].danceability + ',' + songlist[-1].liveness + ',' + songlist[-1].loudness + ',' + songlist[-1].speechiness + ',' + songlist[-1].popularity)
    # shuffled.close()

    #Code used to separate data (80% for teaching, 20% for testing):

    #data = open('ShuffledData', 'r')
    #practice = open('PracticeData', 'w')
    #test = open('TestData', 'w')
    #x = 0
    #for line in data:
        #if x > 139512:
            #test.write(line)
        #else:
            #practice.write(line)
        #x += 1
    #data.close()
    #practice.close()
    #test.close()


