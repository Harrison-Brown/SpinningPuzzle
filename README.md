# SpinningPuzzle
Python code to solve a spinning number puzzle

The `data.py` file contains 5 arrays, each of which representing the rings of numbers on the puzzles. `None` values correspond to holes on the puzzle, allowing numbers below the top layer to show.

The `main.py` file takes the arrays, turn them into `Ring` classes which have the `rotate()` method to change the orientation of the numbers. The `Puzzle` class holds onto each `Ring`, rotating them in the `solve()` method until `checksol()` determines that all columns of numbers add up to 42.
