import os

def play_music():
    """Play the first music file found in the music folder."""
    music_folder = "C:/Users/aDMIN/Music"
    valid_extensions = ('.mp3', '.wav', '.aac', '.flac', '.m4a')

    try:
        songs = [f for f in os.listdir(music_folder) if f.lower().endswith(valid_extensions)]
        if songs:
            os.startfile(os.path.join(music_folder, songs[0]))
            return f"Playing {songs[0]}..."
        return "No music files found."
    except FileNotFoundError:
        return "Music folder not found."
