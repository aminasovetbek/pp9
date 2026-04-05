# Music Player 🎵

A Pygame-based interactive music player with keyboard controls.

## Controls
| Key | Action |
|-----|--------|
| P | Play current track |
| S | Stop playback |
| N | Next track |
| B | Previous (Back) track |
| ↑ | Volume up |
| ↓ | Volume down |
| Q | Quit |

## How to Run
```bash
pip install pygame
py -3.12 main.py
```

## File Structure
```
music_player/
├── main.py      # Entry point, UI and game loop
├── player.py    # MusicPlayer class, playlist logic
├── music/       # Put your MP3/WAV files here
│   ├── md_beatz-night-life-464686.mp3
│   ├── theorienvibes-one-life-233086.mp3
│   └── music_for_video-forest-lullaby-110624.mp3
└── README.md
```
