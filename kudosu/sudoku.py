from decart import *
from solver import *
from puzzle import *

class Sudoku(SudokuDecart):
    def solve(self, solver: SudokuSolver)  -> None: ...

    def puzzle(self, puzzle: SudokuPuzzle) -> None: ...

    def to_csv(self, path: str) -> None: ...