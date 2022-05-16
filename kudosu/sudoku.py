from decart import *
from solver import *
from puzzle import *

class Sudoku(SudokuDecart):
    def solve(self, solver: SudokuSolver) -> None:
        solver(self).solve()

    def multi_solver(self, *solvers: SudokuSolver):
        pass

    def async_multi_solver(self, *solvers: SudokuSolver):
        pass

    def puzzle(self, puzzle: SudokuPuzzle) -> None:
        puzzle(self).create()

    def to_csv(self, path: str) -> None:
        with open(path,'a+') as file:
            for r in self.rowList:
                s = ','.join(['0' if i is None else str(i) for i in r]) # change None to 0 for save csv
                file.write('\n'); file.write(s)
