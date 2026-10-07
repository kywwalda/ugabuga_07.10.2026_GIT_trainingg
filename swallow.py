song1 = "Cherry Stars Collide"
song2 = "Head in a Cave"
song3 = "Tastes Like Honey"

playlist = []

def add_to_playlist(song):
    playlist.append(song)
    return playlist


add_to_playlist(song2)
add_to_playlist(song1)

print(playlist)
