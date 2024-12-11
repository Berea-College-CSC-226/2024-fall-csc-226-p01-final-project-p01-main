import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.music_playlist = [
            "audio/iflooks.mp3",
            "audio/location.mp3"
        ]
        self.current_track_index = 0
        self.is_music_playing = False

    def play_current_track(self):
        try:
            track = self.music_playlist[self.current_track_index]
            if not os.path.exists(track):
                print(f"Music file not found: {track}")
                return
            pygame.mixer.music.load(track)
            pygame.mixer.music.play(-1)
            self.is_music_playing = True
        except pygame.error as e:
            print(f"Error playing {track}: {str(e)}")

    def check_music(self):
        if not pygame.mixer.music.get_busy():
            self.next_track()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.music_playlist)
        self.play_current_track()