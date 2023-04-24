def song_decoder(song):
    l=song.split('WUB')

    a=' '.join(l)

    l=a.split()

    a=' '.join(l)
    return a

s = input()
print(song_decoder(s))