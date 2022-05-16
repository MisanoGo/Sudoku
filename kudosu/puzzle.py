from pathlib import Path
from random import choice, randint
from glob import glob

from decart import SudokuDecart


class SudokuPuzzle:
    def __init__(self,sd: SudokuDecart) -> None:
        self.sdecart = sd

    @staticmethod
    def create(self):
        """ TODO : write doc for abstract create puzzle function"""

class CSVPuzzle(SudokuPuzzle):
    def create(self):
        csv = self.rand_csv
        x,y = 1,1

        for l in csv.splitlines():
            for n in l.split(',') :
                n = int(n)
                if n > 0 and n < 10 :
                    self.sdecart.set(x,y,n)
                x += 1
            x,y = 1,y+1

    @property
    def rand_csv(self):
        p = str(Path(__file__).parent.joinpath('puzzles/**.csv'))
        rp = choice(glob(p,recursive=True)) # random puzzle
        with open(rp,'r') as csv :
            return csv.read()