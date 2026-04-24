# Task 1: Mickey's Clock Application

## Objective
Create a digital-style clock using Mickey Mouse hand graphics (or simple geometric hands as a fallback) to display the system time (minutes and seconds).

## Controls
- There are no interactive controls. The application will track the local system time automatically.
- Close the window to exit.

## How to Run
Ensure Pygame is installed and run:
```bash
python main.py
```

## File Description
- `main.py`: Sets up Pygame, opens the window, and runs the display update loop.
- `clock.py`: Contains the `Clock` class that loads assets, retrieves the system time, calculates angles, handles missing assets safely, and draws everything to the screen.
- `images/`: Folder configured to hold the `mickey_hand.png`.

## Requirements Verification
- Displays minutes and seconds synchronized with system clock correctly.
- Calculates appropriate rotation angles from system time applying `pygame.transform.rotate`.
- Handles edge cases if images are missing by drawing basic line hands.
- Split cleanly between `main.py` and `clock.py` conforming to modular practices.
