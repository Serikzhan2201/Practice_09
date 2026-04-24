import pygame
import os

class MusicPlayer:
    def __init__(self):
        self.tracks = []
        self.current_idx = 0
        self.is_playing = False
        
        self.load_tracks()

    def load_tracks(self):
        # Scan predefined folder dynamically 
        music_dir = os.path.join(os.path.dirname(__file__), "music", "sample_tracks")
        os.makedirs(music_dir, exist_ok=True)
        
        self.tracks = []
        for f in sorted(os.listdir(music_dir)):
            if f.lower().endswith((".mp3", ".wav")):
                self.tracks.append(os.path.join(music_dir, f))
                
        self.current_idx = 0
                
    def play(self):
        if not self.tracks:
            return
        
        try:
            # Assure clean reload if finished prior naturally
            if not self.is_playing or not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(self.tracks[self.current_idx])
                pygame.mixer.music.play()
                self.is_playing = True
        except pygame.error:
            pass

    def stop(self):
        if not self.tracks:
            return
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.tracks:
            return
        
        self.current_idx = (self.current_idx + 1) % len(self.tracks)
        
        # Ensure continuity if running naturally
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.play()

    def previous_track(self):
        if not self.tracks:
            return
        
        self.current_idx = (self.current_idx - 1) % len(self.tracks)
        
        # Resume directly via preceding sequence gracefully
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.play()

    def get_info_text(self):
        # Display clear message when files missing avoiding crashed states
        if not self.tracks:
            return "No audio tracks! Drop some in music/sample_tracks/"
        
        filename = os.path.basename(self.tracks[self.current_idx])
        status = "Playing" if self.is_playing else "Stopped"
        
        # Show time / fallback strictly safely
        pos = pygame.mixer.music.get_pos()
        if pos == -1 or not self.is_playing:
            pos_str = "0:00"
        else:
            seconds = pos // 1000
            pos_str = f"{seconds // 60}:{seconds % 60:02d}"
            
        return f"Track {self.current_idx + 1} of {len(self.tracks)}: {filename} [{status}] ({pos_str})"
