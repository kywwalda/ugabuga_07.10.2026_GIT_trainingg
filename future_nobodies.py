song1 = "Fear & Loathing"
song2 = "Solo Contigo"
song3 = "She Hates All the Drugs I Do"
song4 = "Pity Party"
song5 = "Fever Dream"
song6 = "Unloveable"
song7 = "Attachment Issues"

playlist_1 = []
playlist_2 = []

def add_to_playlist(song, playlist):
    playlist.append(song)
    return playlist


add_to_playlist(song2, playlist_2)
add_to_playlist(song6, playlist_2)
add_to_playlist(song7, playlist_2)

add_to_playlist(song1, playlist_1)
add_to_playlist(song3, playlist_1)
add_to_playlist(song4, playlist_1)
add_to_playlist(song5, playlist_1)

print(f"{playlist_1} эти помню")
print(f"{playlist_2} эти не помню")

