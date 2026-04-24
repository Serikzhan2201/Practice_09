# Task 3: Moving Ball Game

## Objective
Create an interactive game with a moving red ball ensuring it never transitions beyond the window boundaries.

## Controls
- `UP Arrow`: Move up
- `DOWN Arrow`: Move down
- `LEFT Arrow`: Move left
- `RIGHT Arrow`: Move right

## How to Run
Ensure Pygame is installed and run:
```bash
python main.py
```

## File Description
- `main.py`: Initializes Pygame, creates the window, processes event loops (capturing arrow controls dynamically), redraws the ball, and caps framerates accurately utilizing `pygame.time.Clock()`.
- `ball.py`: Contains the standard `Ball` class mapping its internal state (`x`, `y`, `radius`) and rendering logic correctly avoiding window boundary collisions via strict bounds checking preventing edges from piercing walls.
