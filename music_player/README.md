# Task 2: Music Player with Keyboard Controller

## Objective
Build an interactive music player with keyboard controls, fully capable of recognizing and reading standard tracks targeting particular folders successfully.

## Controls
- `P` = Play
- `S` = Stop
- `N` = Next track
- `B` = Previous track
- `Q` = Quit

## How to Run
1. Place standard `.mp3` or `.wav` format files actively into the explicitly linked `music/sample_tracks/` directory.
2. Assure `pygame` operates directly targeting identical configurations.
3. Run the interactive interface manually:
```bash
python main.py
```

## File Description
- `main.py`: Generates the target `pygame.init()` handling, initializes the explicit `pygame.mixer.init()` dependency natively, updates text font variables appropriately resolving explicit controls mapped directly across.
- `player.py`: Covers the strict `MusicPlayer` class tracking audio directory states directly. Assures operations covering `next_track()`, `previous_track()`, explicit boundaries handling and visual tracker indicators (like "Track 1 of X") fallback cleanly if times stall out properly.
