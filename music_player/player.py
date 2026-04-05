import pygame
import os


class MusicPlayer:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = []
        self.current_index = 0
        self.is_playing = False

        for f in sorted(os.listdir(music_folder)):
            if f.lower().endswith(('.mp3', '.wav', '.ogg')):
                self.playlist.append({
                    'path': os.path.join(music_folder, f),
                    'name': os.path.splitext(f)[0][:35]
                })

    def play(self):
        if not self.playlist:
            return
        pygame.mixer.music.load(self.playlist[self.current_index]['path'])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        if self.is_playing:
            self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        if self.is_playing:
            self.play()

    def get_name(self):
        return self.playlist[self.current_index]['name'] if self.playlist else "No tracks"

    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000 if self.is_playing else 0

    def get_volume(self):
        return pygame.mixer.music.get_volume()

    def set_volume(self, v):
        pygame.mixer.music.set_volume(max(0.0, min(1.0, v)))

    def finished(self):
        return self.is_playing and not pygame.mixer.music.get_busy()
