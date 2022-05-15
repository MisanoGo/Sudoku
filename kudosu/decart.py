from random import randint
from typing import Generator ,List ,Tuple ,Dict
from itertools import product

from utils import checkListDepublicate as cld,noneable

class SudokuDecart:
    range10 = range(1,10)
    cleanSudoku = {(x,y):None for x,y in product(range10,range10)}

    def __init__(self, decart= None) -> None:
        self.decart: Dict[Tuple[int,int]:int]= noneable(decart,self.cleanSudoku)

    def insert(self, x: int, y: int, num: int):
        xy = (x,y)
        decart_copy = self.decart.copy()
        self.decart[xy] = num

        if not self.checkCoordDepublicate(x,y):
            self.decart = decart_copy
            # TODO : raise Exception of depublicate value

    def randInsert(self, x: int = None, y: int = None, n: int = None):
        x = noneable(x, randint(1,9))
        y = noneable(y, randint(1,9))
        n = noneable(n, randint(1,9))

        self.insert(x,y,n)

    def get(self, x: int, y: int) -> int:
        xy = (x,y)
        return self.decart[xy]

    def getList(self, *coord: Tuple[int,int]) -> List[int]:
        return [self.get(*xy) for xy in coord]

    def remove(self, x: int, y: int) -> int:
        xy = (x,y)
        n = self.get(x,y)

        self.decart[xy] = None
        return n

    def clean(self):
        self.decart = self.cleanSudoku

    def row(self, y: int) -> List[int]:
        if y in self.range10:
            return [self.decart[(x,y)] for x in self.range10]

    def rowList(self) -> Generator[List[int],None,None]:
        for y in self.range10:
            yield self.row(y)

    def column(self, x: int) -> List[int]:
        if x in self.range10:
            return [self.decart[(x,y)] for y in self.range10]

    def columnList(self) -> Generator[List[int],None,None]:
        for x in self.range10:
            yield self.column(x)

    def area(self, x: int, y: int) -> List[int]:
        """ return list of numbers in area of 3*3"""
        # get the area index in decart coordination
        ax = int(x//3.5)+1
        ay = int(y//3.5)+1
        return self.nArea(ax,ay)

    def nArea(self, ax: int, ay: int) -> List[int]:
        # get the start and stop coordination of area
        sx,sy = (ax*3)-2,(ay*3)-2
        dx,dy = ax*3,ay*3
        # get all of items coords in area and get theres numbers
        return self.getList(*product(range(sx,dx+1),range(sy,dy+1)))

    def areaList(self) -> Generator[List[int],None,None]:
        range3 = range(1,3)
        for ax in range3:
            for ay in range3:
                yield self.barea(ax,ay)

    @property
    def check(self) -> bool:
        ivl = self.decart.values() # item value list

        if not any([iv is not None for iv in ivl]):
            if sum(ivl) == (9*(9+1)//2)*9:
                return self.checkDepublicate
        return False

    @property
    def checkDepublicate(self) -> bool:
        nl = list(self.rowList()) + list(self.columnList()) + list(self.areaList())
        return cld(*nl)

    def checkCoordDepublicate(self, x: int, y: int) -> bool:
        return cld(self.row(y),self.column(x),self.area(x,y))
